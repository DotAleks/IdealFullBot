import os

from dotenv import load_dotenv


class Config():
    """"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if getattr(self, '_initialized', False):
            return
        
        load_dotenv()
        
        self.BOT_TOKEN = self._get_required('BOT_TOKEN')

        self.WEBHOOK_URL = self._get_required('WEBHOOK_URL')
        self.WEBHOOK_HOST = self._get_required('WEBHOOK_HOST')
        self.WEBHOOK_PATH = self._get_required('WEBHOOK_PATH','/webhook')
        self.WEBHOOK_PORT = self._get_required('WEBHOOK_PORT')
        
        self.WEBAPP_HOST = self._get_required('WEBAPP_HOST','127.0.0.1')
        self.WEBAPP_PORT = int(self._get_required('WEBAPP_PORT','8000'))

        self.DB_DRIVER = self._get_required('DB_DRIVER')
        self.DB_HOST = self._get_required('DB_HOST')
        self.DB_PORT = self._get_required('DB_PORT')
        self.DB_NAME = self._get_required('DB_NAME')
        self.DB_USER = self._get_required('DB_USER')
        self.DB_PASSWD = self._get_required('DB_PASSWD')
        self.DB_URL = f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

        self.REDIS_SCHEME = self._get_required('REDIS_SCHEME')
        self.REDIS_USER = self._get_required('REDIS_USER')
        self.REDIS_HOST = self._get_required('REDIS_HOST')
        self.REDIS_PORT = int(self._get_required('REDIS_PORT'))
        self.REDIS_PASSWD = self._get_required('REDIS_PASSWD')
        self.REDIS_DB = self._get_required('REDIS_DB')
        

        
        self._initialized = True
    @property
    def REDIS_URL(self):
        if self.REDIS_SCHEME == 'unix':
            return f'{self.REDIS_SCHEME}://{self.REDIS_HOST}?db={self.REDIS_DB}'

        return f'{self.REDIS_SCHEME}://{self.REDIS_USER}:{self.REDIS_PASSWD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}'
    
    def _get_required(self, var_name:str,default: str | None = None) -> str:
        """"""
        value = os.getenv(var_name,default=default)
        if value is None:
            raise ValueError(f'Required enviroment variable {var_name} not set!')
        return value.strip()

config = Config()