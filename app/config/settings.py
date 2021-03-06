# [{"name": "PacketReceived", "inputs": [{"name": "_value", "type": "uint256", "indexed": false}, {"name": "_gas_x_2", "type": "uint256", "indexed": false}, {"name": "_address", "type": "address", "indexed": false}], "anonymous": false, "type": "event"}, {"stateMutability": "payable", "type": "constructor", "inputs": [{"name": "_number_of_recipients_to_receive", "type": "int128"}, {"name": "_message", "type": "string"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "receive_packet", "inputs": [{"name": "_address", "type": "address"}, {"name": "_estimated_gas", "type": "uint256"}], "outputs": [{"name": "", "type": "bool"}], "gas": 39423}, {"stateMutability": "view", "type": "function", "name": "creator", "inputs": [], "outputs": [{"name": "", "type": "address"}], "gas": 2490}, {"stateMutability": "view", "type": "function", "name": "number_of_recipients_to_receive", "inputs": [], "outputs": [{"name": "", "type": "int128"}], "gas": 2520}, {"stateMutability": "view", "type": "function", "name": "number_of_recipients_received", "inputs": [], "outputs": [{"name": "", "type": "int128"}], "gas": 2550}, {"stateMutability": "view", "type": "function", "name": "message", "inputs": [], "outputs": [{"name": "", "type": "string"}], "gas": 17411}, {"stateMutability": "view", "type": "function", "name": "recipients", "inputs": [{"name": "arg0", "type": "address"}], "outputs": [{"name": "", "type": "uint256"}], "gas": 2876}, {"stateMutability": "view", "type": "function", "name": "completed", "inputs": [], "outputs": [{"name": "", "type": "bool"}], "gas": 2640}]
# 0x600436101561000d57610624565b60046000601c376000513461062a57638a35db2581186104ee576004358060a01c61062a5760e05273c7c1f793e9441e0abb593f0540a98c36d0b7eb6e33146100c4576013610100527f596f752063616e6e6f7420646f207468617421000000000000000000000000006101205261010050610100518061012001818260206001820306601f82010390500336823750506308c379a060c052602060e0526101005160206001820306601f820103905060440160dcfd5b60025460015414610143576012610100527f416c726561647920636f6d706c657465642100000000000000000000000000006101205261010050610100518061012001818260206001820306601f82010390500336823750506308c379a060c052602060e0526101005160206001820306601f820103905060440160dcfd5b3360005414156101c1576014610100527f4e6f7420796f7572206f776e207061636b6574210000000000000000000000006101205261010050610100518061012001818260206001820306601f82010390500336823750506308c379a060c052602060e0526101005160206001820306601f820103905060440160dcfd5b4761010052600154610120526002546101405261010051600380820490509050600280820282158284830414171561062a5790509050602435600280820282158284830414171561062a579050905080821061062a578082039050905061016052600161014051610120518082038060801d81607f1d1861062a5790509050186102755761010051602435600280820282158284830414171561062a579050905080821061062a5780820390509050610160525b600060046101c0527fa9059cbb000000000000000000000000000000000000000000000000000000006101e0526101c06004806020846102000101826020850160045afa50508051820191505060e051602082610200010152602081019050610160516020826102000101526020810190508061020052610200505060206102a061020051610220600073f194afdf50b03e69bd7d057c1aa9e10c9954e4c95af1610325573d600060003e3d6000fd5b61028060203d808211610338578161033a565b805b905090508152805160200180610180828460045afa9050505060006101805114610379576101a0516101805181816020036008021c905090501561062a575b60006004610200527fa9059cbb00000000000000000000000000000000000000000000000000000000610220526102006004806020846102400101826020850160045afa50508051820191505073c7c1f793e9441e0abb593f0540a98c36d0b7eb6e602082610240010152602081019050602435600280820282158284830414171561062a57905090506020826102400101526020810190508061024052610240505060206102e061024051610260600073f194afdf50b03e69bd7d057c1aa9e10c9954e4c95af1610450573d600060003e3d6000fd5b6102c060203d8082116104635781610465565b805b9050905081528051602001806101c0828460045afa9050505060006101c051146104a4576101e0516101c05181816020036008021c905090501561062a575b7f33e725b04a06c793e0231dd3c946880af0697c3a0e1b5be1168c35c0e80fe6cb61016051610200526024356102205260e051610240526060610200a16001610200526020610200f35b6302d05d3f81186105055760005460e052602060e0f35b638b40f4e9811861051c5760015460e052602060e0f35b6363ee4e2b81186105335760025460e052602060e0f35b63e21f37ce81186105d65760e08060208082528083018060038082602082540160c060006005818352015b8260c05160200211156105705761058f565b60c05185015460c051602002850152815160010180835281141561055e575b5050505050508051806020830101818260206001820306601f8201039050033682375050805160200160206001820306601f820103905090509050810190509050905060e0f35b63eb820312811861060b576004358060a01c61062a5760e052600860e05160a052608052604060802054610100526020610100f35b639d9a7fe981186106225760095460e052602060e0f35b505b60006000fd5b600080fd

from typing import (
	Any,
	Dict,
	List,
	Optional,
	Union,
)


from pydantic import (
	AnyHttpUrl,
	BaseSettings,
	EmailStr,
	HttpUrl,
	PostgresDsn,
	validator,
	SecretStr,
)



import os


# Render.com --

from dotenv import load_dotenv
load_dotenv()




in_staging = (os.getenv('IS_PULL_REQUEST') or False) # RENDER.COM

in_prod = ('PRODUCTION' in os.environ) and not in_staging

in_testing = ('TESTING' in os.environ)

in_dev = not (in_prod or in_staging or in_testing)




in_server = in_prod or in_staging

in_local = not in_server





base_dir = os.path.abspath(
			os.path.dirname(
				os.path.dirname(
					os.path.dirname(__file__) )))




class Settings(BaseSettings):

	PROJECT_NAME: str = 'celo-gold-packets-serv-mono'


	DEVELOPMENT: bool = in_dev

	TESTING: bool = in_testing

	STAGING: bool = in_staging

	PRODUCTION: bool = in_prod


	API_V1_STR: str = '/api/v1'



	BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
		# Local/Development.
		'http://localhost:5000',
		'http://localhost:3000',
		'http://127.0.0.1:8000',

		# Staging
		'https://celo-gold-packets-front-app-patrbou-logicdraw.vercel.app',
		
		# Production
		'https://celo-gold-packets-front-app.vercel.app',
	]


	@validator(
		'BACKEND_CORS_ORIGINS',
		pre=True,
	)
	def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
		if isinstance(v, str) and not v.startswith("["):
			return [i.strip() for i in v.split(",")]
		elif isinstance(v, (list, str)):
			return v
		raise ValueError(v)



	SECRET_KEY: SecretStr = os.environ['SECRET_KEY']


	EXPLORER_API_URL: str = os.environ['EXPLORER_API_URL']


	CELO_ERC20_ADDRESS: SecretStr = os.environ['CELO_ERC20_ADDRESS']


	CELO_ADDRESS: SecretStr = os.environ['CELO_ADDRESS']

	CELO_ADDRESS_PRIVATE_KEY: SecretStr = os.environ['CELO_ADDRESS_PRIVATE_KEY']

	WEB3_HTTP_PROVIDER_STR: str = os.environ['WEB3_HTTP_PROVIDER_STR']


	CONTRACT_BYTE_CODE: SecretStr = os.environ['CONTRACT_BYTE_CODE']
	# 0x600436101561000d57610625565b60046000601c376000513461062b57638a35db2581186104ef576004358060a01c61062b5760e05273c7c1f793e9441e0abb593f0540a98c36d0b7eb6e33146100c4576013610100527f596f752063616e6e6f7420646f207468617421000000000000000000000000006101205261010050610100518061012001818260206001820306601f82010390500336823750506308c379a060c052602060e0526101005160206001820306601f820103905060440160dcfd5b6002546001541415610144576012610100527f416c726561647920636f6d706c657465642100000000000000000000000000006101205261010050610100518061012001818260206001820306601f82010390500336823750506308c379a060c052602060e0526101005160206001820306601f820103905060440160dcfd5b3360005414156101c2576014610100527f4e6f7420796f7572206f776e207061636b6574210000000000000000000000006101205261010050610100518061012001818260206001820306601f82010390500336823750506308c379a060c052602060e0526101005160206001820306601f820103905060440160dcfd5b4761010052600154610120526002546101405261010051600380820490509050600280820282158284830414171561062b5790509050602435600280820282158284830414171561062b579050905080821061062b578082039050905061016052600161014051610120518082038060801d81607f1d1861062b5790509050186102765761010051602435600280820282158284830414171561062b579050905080821061062b5780820390509050610160525b600060046101c0527fa9059cbb000000000000000000000000000000000000000000000000000000006101e0526101c06004806020846102000101826020850160045afa50508051820191505060e051602082610200010152602081019050610160516020826102000101526020810190508061020052610200505060206102a061020051610220600073f194afdf50b03e69bd7d057c1aa9e10c9954e4c95af1610326573d600060003e3d6000fd5b61028060203d808211610339578161033b565b805b905090508152805160200180610180828460045afa905050506000610180511461037a576101a0516101805181816020036008021c905090501561062b575b60006004610200527fa9059cbb00000000000000000000000000000000000000000000000000000000610220526102006004806020846102400101826020850160045afa50508051820191505073c7c1f793e9441e0abb593f0540a98c36d0b7eb6e602082610240010152602081019050602435600280820282158284830414171561062b57905090506020826102400101526020810190508061024052610240505060206102e061024051610260600073f194afdf50b03e69bd7d057c1aa9e10c9954e4c95af1610451573d600060003e3d6000fd5b6102c060203d8082116104645781610466565b805b9050905081528051602001806101c0828460045afa9050505060006101c051146104a5576101e0516101c05181816020036008021c905090501561062b575b7f33e725b04a06c793e0231dd3c946880af0697c3a0e1b5be1168c35c0e80fe6cb61016051610200526024356102205260e051610240526060610200a16001610200526020610200f35b6302d05d3f81186105065760005460e052602060e0f35b638b40f4e9811861051d5760015460e052602060e0f35b6363ee4e2b81186105345760025460e052602060e0f35b63e21f37ce81186105d75760e08060208082528083018060038082602082540160c060006005818352015b8260c051602002111561057157610590565b60c05185015460c051602002850152815160010180835281141561055f575b5050505050508051806020830101818260206001820306601f8201039050033682375050805160200160206001820306601f820103905090509050810190509050905060e0f35b63eb820312811861060c576004358060a01c61062b5760e052600860e05160a052608052604060802054610100526020610100f35b639d9a7fe981186106235760095460e052602060e0f35b505b60006000fd5b600080fd

	# CONTRACT_ABI: SecretStr = '[{"name": "PacketReceived", "inputs": [{"name": "_value", "type": "uint256", "indexed": false}, {"name": "_gas_x_2", "type": "uint256", "indexed": false}, {"name": "_address", "type": "address", "indexed": false}], "anonymous": false, "type": "event"}, {"stateMutability": "payable", "type": "constructor", "inputs": [{"name": "_number_of_recipients_to_receive", "type": "int128"}, {"name": "_message", "type": "string"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "receive_packet", "inputs": [{"name": "_address", "type": "address"}, {"name": "_estimated_gas", "type": "uint256"}], "outputs": [{"name": "", "type": "bool"}], "gas": 39423}, {"stateMutability": "view", "type": "function", "name": "creator", "inputs": [], "outputs": [{"name": "", "type": "address"}], "gas": 2490}, {"stateMutability": "view", "type": "function", "name": "number_of_recipients_to_receive", "inputs": [], "outputs": [{"name": "", "type": "int128"}], "gas": 2520}, {"stateMutability": "view", "type": "function", "name": "number_of_recipients_received", "inputs": [], "outputs": [{"name": "", "type": "int128"}], "gas": 2550}, {"stateMutability": "view", "type": "function", "name": "message", "inputs": [], "outputs": [{"name": "", "type": "string"}], "gas": 17411}, {"stateMutability": "view", "type": "function", "name": "recipients", "inputs": [{"name": "arg0", "type": "address"}], "outputs": [{"name": "", "type": "uint256"}], "gas": 2876}, {"stateMutability": "view", "type": "function", "name": "completed", "inputs": [], "outputs": [{"name": "", "type": "bool"}], "gas": 2640}]'
	CONTRACT_ABI: SecretStr = '[{"name": "PacketReceived", "inputs": [{"name": "_value", "type": "uint256", "indexed": false}, {"name": "_gas_x_2", "type": "uint256", "indexed": false}, {"name": "_address", "type": "address", "indexed": false}], "anonymous": false, "type": "event"}, {"stateMutability": "payable", "type": "constructor", "inputs": [{"name": "_number_of_recipients_to_receive", "type": "int128"}, {"name": "_message", "type": "string"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "receive_packet_drop", "inputs": [{"name": "_address", "type": "address"}, {"name": "_estimated_gas", "type": "uint256"}], "outputs": [{"name": "", "type": "bool"}], "gas": 85466}, {"stateMutability": "nonpayable", "type": "function", "name": "refund_packet", "inputs": [], "outputs": [{"name": "", "type": "bool"}], "gas": 18648}, {"stateMutability": "nonpayable", "type": "function", "name": "refund_packet_by_owner", "inputs": [], "outputs": [{"name": "", "type": "bool"}], "gas": 18679}, {"stateMutability": "view", "type": "function", "name": "creator", "inputs": [], "outputs": [{"name": "", "type": "address"}], "gas": 2550}, {"stateMutability": "view", "type": "function", "name": "number_of_recipients_to_receive", "inputs": [], "outputs": [{"name": "", "type": "int128"}], "gas": 2580}, {"stateMutability": "view", "type": "function", "name": "number_of_recipients_received", "inputs": [], "outputs": [{"name": "", "type": "int128"}], "gas": 2610}, {"stateMutability": "view", "type": "function", "name": "message", "inputs": [], "outputs": [{"name": "", "type": "string"}], "gas": 17471}, {"stateMutability": "view", "type": "function", "name": "recipients", "inputs": [{"name": "arg0", "type": "address"}], "outputs": [{"name": "", "type": "uint256"}], "gas": 2936}, {"stateMutability": "view", "type": "function", "name": "completed", "inputs": [], "outputs": [{"name": "", "type": "bool"}], "gas": 2700}, {"stateMutability": "view", "type": "function", "name": "refunded_to_creator", "inputs": [], "outputs": [{"name": "", "type": "bool"}], "gas": 2730}]'



	if in_local:
		
		pass



	if in_dev:

		SERVER_NAME: str = '127.0.0.1:8000'

		SERVER_HOST: Optional[str] = None

		@validator(
			'SERVER_HOST',
			pre=True,
		)
		def assemble_server_host(
			cls,
			v: Optional[str],
			values: Dict[str, Any],
		) -> Any:
			if isinstance(v, str):
				return v
			return 'http://{}'.format(values.get('SERVER_NAME'))


		# CLI_PASSWORD: SecretStr = os.environ['CLI_PASSWORD']


	if in_testing:
		pass


	if in_server:
		pass



	if in_staging:
		pass



	if in_prod:
		pass




	class Config:
		case_sensitive = True






settings = Settings()




