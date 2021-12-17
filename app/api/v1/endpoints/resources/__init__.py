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


from app.utils.web3 import (
	w3,
	Web3,
)


from web3.extensions import InvalidAddress


from app.security import (
	create_token,
	verify_token,
)


from pydantic import BaseModel



router = APIRouter()





def verify_contract_by_address(
	address: str,
) -> str:
	# --

	try:
		bytecode = w3.eth.get_code(address).hex()
	except InvalidAddress as e:
		raise HTTPException(
			status=400,
			detail='This is an invalid address! Try again!',
		)
	except Exception as e:
		raise HTTPException(
			status=500,
			detail='Error! Try again!',
		)
	else:
		if bytecode != settings.CONTRACT_BYTE_CODE.get_secret_value():
			raise HTTPException(
				status=400,
				detail='This is an invalid contract!',
			)

	return bytecode





class ContractAddressIn(BaseModel):
	contract_address: str




@router.post(
	'/verify-contract',
	# response_model=schemas.MsgSchema,
)
@limiter.limiter('10/minute')
async def verify_contract(
	request: Request,
	*,
	contract_address_in: ContractAddressIn,
) -> Any:
	# --

	bytecode = verify_contract_by_address(contract_address_in.contract_address)


	slug = create_token(
		subject=bytecode,
	)

	return slug





@router.get(
	'/validate-contract/{slug}',
	response_model=schemas.MsgSchema,
)
@limiter.limiter('10/minute')
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
			status=404,
			detail='Packet not found!',
		)


	verify_contract_by_address(contract_address_in.contract_address)


	return {
		'msg': 'Address is valid!',
	}





class AcceptPacketIn(BaseModel):
	address: str


@router.post(
	'/accept-packet/{slug}',
)
@limiter.limiter('10/minute')
async def accept_packet(
	request: Request,
	*,
	slug: str,
	accept_packet_in: AcceptPacketIn,
) -> Any:
	# --

	if not Web3.isAddress(accept_packet_in.address):
		raise HTTPException(
			status='400',
			detail='Invalid address!',
		)


	address = verify_token(
		token=slug,
	)

	if address is None:
		raise HTTPException(
			status=404,
			detail='Packet not found!',
		)


	verify_contract_by_address(address)



	contract_instance = w3.eth.contract(
		abi=settings.CONTRACT_ABI.get_secret_value(),
		address=address,
	)


	estimated_gas = contract_instance.functions.receive_packet(accept_packet_in.address, 0).estimateGas()


	txn = contract_instance.functions.receive_packet(accept_packet_in.address, 0).buildTransaction({
		'from': settings.CELO_ADDRESS.get_secret_value(),
		'gasPrice': w3.eth.gas_price,
		'nonce': w3.eth.get_transaction_count(settings.CELO_ADDRESS.get_secret_value()),
	})


	signed_txn = w3.eth.account.sign_transaction(
		txn,
		private_key=settings.CELO_ADDRESS_PRIVATE_KEY.get_secret_value(),
	)


	w3.eth.send_raw_transaction(signed_txn.rawTransaction)

	# wait ..








# @router.post(
# 	'/accept-packet-phone/{slug}',
# )
# @limiter.limiter('10/minute')
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
# 			status=404,
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






