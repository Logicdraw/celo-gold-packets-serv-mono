from web3 import Web3


from app.config.settings import settings



w3 = Web3(Web3.HTTPProvider(settings.WEB3_HTTP_PROVIDER_STR))



