import os

from pydantic import BaseModel, BaseSettings, Field, SecretStr


class Dirs(BaseModel):
    pwd = os.getcwd()
    log_dir = Field(default=os.path.join(pwd, 'logs'))
    raw_data_dir = Field(default=os.path.join(pwd, 'raw_data'))
    data_dir = Field(default=os.path.join(pwd, 'data'))


class Preferences(BaseSettings):
    # file system
    dirs: Dirs = Dirs()

    # env_file = '.env'
    api_key: SecretStr = Field(..., env='API_KEY')
    log_level: str = Field('DEBUG', env='LOG_LEVEL')
    log_file: str = Field(os.path.join(dirs.log_dir, 'price_checker.log'))
