from typing import (
	Any,
	List,
	Optional,
)

from fastapi import (
	APIRouter,
	Depends,
	Query,
	Request,
	HTTPException,
)


from app import (
	schemas,
)


from app.api import deps


from app.extensions import limiter


from app.config.settings import settings


# from app.utils.web3 import (
# 	w3,
# 	# Web3,
# )



from app.security import (
	create_token,
	verify_token,
)


from pydantic import BaseModel



from app.config.settings import settings


import httpx


from web3 import Web3



w3 = Web3(Web3.HTTPProvider(settings.WEB3_HTTP_PROVIDER_STR))


from web3.exceptions import *





router = APIRouter()





def verify_contract_by_address(
	address: str,
) -> str:
	# --

	try:
		bytecode = w3.eth.get_code(w3.toChecksumAddress(address)).hex()
	except InvalidAddress as e:
		print('1')
		print(e)
		raise HTTPException(
			status_code=400,
			detail='This is an invalid address! Try again!',
		)
	except Exception as e:
		print('2')
		print(e)
		raise HTTPException(
			status_code=500,
			detail='Error! Try again!',
		)
	else:
		if bytecode != settings.CONTRACT_BYTE_CODE.get_secret_value():
			print('3')
			print('apple...')
			raise HTTPException(
				status_code=400,
				detail='This is an invalid contract!',
			)

	return bytecode





class ContractAddressIn(BaseModel):
	contract_address: str




@router.post(
	'/verify-contract',
	# response_model=schemas.MsgSchema,
)
@limiter.limit('10/minute')
async def verify_contract(
	request: Request,
	*,
	contract_address_in: ContractAddressIn,
) -> Any:
	# --

	bytecode = verify_contract_by_address(contract_address_in.contract_address)


	slug = create_token(
		subject=contract_address_in.contract_address,
	)

	return slug





@router.get(
	'/validate-contract/{slug}',
	response_model=schemas.MsgSchema,
)
@limiter.limit('10/minute')
async def validate_contract(
	request: Request,
	*,
	slug: str,
) -> Any:
	# --

	address = verify_token(
		token=slug,
	)

	if address is None:
		raise HTTPException(
			status_code=404,
			detail='Packet not found!',
		)


	verify_contract_by_address(address)


	return {
		'msg': 'Address is valid!',
	}





class AcceptPacketIn(BaseModel):
	address: str


@router.post(
	'/accept-packet/{slug}',
)
@limiter.limit('10/minute')
async def accept_packet(
	request: Request,
	*,
	slug: str,
	accept_packet_in: AcceptPacketIn,
) -> Any:
	# --
	# Double collect?
	# later resolve this ...

	if not w3.isAddress(accept_packet_in.address):
		raise HTTPException(
			status='400',
			detail='Invalid address!',
		)


	address = verify_token(
		token=slug,
	)

	if address is None:
		raise HTTPException(
			status_code=404,
			detail='Packet not found!',
		)


	verify_contract_by_address(address)



	contract_instance = w3.eth.contract(
		abi=settings.CONTRACT_ABI.get_secret_value(),
		address=address,
	)


	estimated_gas = contract_instance.functions.receive_packet(accept_packet_in.address, 0).estimateGas({
		'from': settings.CELO_ADDRESS.get_secret_value(),
	}) * w3.eth.gas_price


	txn = contract_instance.functions.receive_packet(accept_packet_in.address, estimated_gas).buildTransaction({
		'from': settings.CELO_ADDRESS.get_secret_value(),
		'gasPrice': w3.eth.gas_price,
		'nonce': w3.eth.get_transaction_count(settings.CELO_ADDRESS.get_secret_value()),
	})


	signed_txn = w3.eth.account.sign_transaction(
		txn,
		private_key=settings.CELO_ADDRESS_PRIVATE_KEY.get_secret_value(),
	)


	try:
		w3.eth.send_raw_transaction(signed_txn.rawTransaction)
	except:
		raise HTTPException(
			status=500,
			detail='Error!',
		)


	txn = w3.toHex(w3.keccak(signed_txn.rawTransaction))


	return {
		'txn': f'{txn}',
	}




class Recipient(BaseModel):
	hash: Any
	value: Any
	to: Any
	timeStamp: Any



@router.get(
	'/packet-leaderboard/{slug}',
	response_model=List[Recipient],
)
@limiter.limit('120/minute')
async def read_packet_leaderboard(
	request: Request,
	*,
	slug: str,
) -> Any:
	# --
	
	address = verify_token(
		token=slug,
	)

	if address is None:
		raise HTTPException(
			status_code=404,
			detail='Packet not found!',
		)


	verify_contract_by_address(address)


	url = f'https://alfajores-blockscout.celo-testnet.org/api'

	params = {
		'module': 'account',
		'action': 'tokentx',
		'address': address,
	}

	try:
		async with httpx.AsyncClient() as a_client:
			resp = await a_client.request(
				method='GET',
				url=url,
				params=params,
			)
	except Exception as err:
		raise HTTPException(
			status=500,
			detail='Error! Try aagain!'
		)

	recipients = []

	for tokentx in resp.json()['result']:
		# --
		if (tokentx['from'].lower() == address.lower()) and (tokentx['contractAddress'].lower() == '0xf194afdf50b03e69bd7d057c1aa9e10c9954e4c9'.lower()):

			if tokentx['to'].lower() == '0xc7c1f793E9441e0abB593f0540a98c36d0b7Eb6E'.lower():
				continue

			params = {
				'module': 'transaction',
				'action': 'gettxreceiptstatus',
				'txhash': tokentx['hash'],
			}

			try:
				async with httpx.AsyncClient() as a_client:
					resp = await a_client.request(
						method='GET',
						url=url,
						params=params,
					)
			except Exception as err:
				raise HTTPException(
					status=500,
					detail='Error! Try aagain!'
				)

			# Invalid txn...
			# if resp.json()['result']['status'] != '1':
				# continue


			recipients.append(
				{
					'hash': tokentx['hash'],
					'value': tokentx['value'],
					'to': tokentx['to'],
					'timeStamp': tokentx['timeStamp'],
				},
			)



	return recipients





# @router.post(
# 	'/accept-packet-phone/{slug}',
# )
# @limiter.limit('10/minute')
# async def accept_packet_phone(
# 	request: Request,
# 	*,
# 	slug: str,
# 	accept_packet_in: AcceptPacketIn,
# ) -> Any:
# 	# --

# 	if not w3.utils.isAddress(accept_packet_in.address):
# 		raise HTTPException(
# 			status='400',
# 			detail='Invalid address!',
# 		)


# 	address = verify_token(
# 		token=slug,
# 	)

# 	if address is None:
# 		raise HTTPException(
# 			status_code=404,
# 			detail='Packet not found!',
# 		)


# 	verify_contract_by_address(address)



# 	contract_instance = w3.eth.contract(
# 		abi=settings.CONTRACT_ABI.get_secret_value(),
# 		address=address,
# 	)


# 	estimated_gas = contract_instance.functions.receive_packet(accept_packet_in.address, 0).estimateGas()


# 	txn = contract_instance.functions.receive_packet(accept_packet_in.address, 0).buildTransaction({
# 		'from': settings.CELO_ADDRESS.get_secret_value(),
# 		'gasPrice': w3.eth.gas_price,
# 		'nonce': w3.eth.get_transaction_count(settings.CELO_ADDRESS.get_secret_value()),
# 	})


# 	signed_txn = w3.eth.account.sign_transaction(
# 		txn,
# 		private_key=settings.CELO_ADDRESS_PRIVATE_KEY.get_secret_value(),
# 	)


# 	w3.eth.send_raw_transaction(signed_txn.rawTransaction)






