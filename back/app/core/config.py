from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class GSConfig(BaseModel):
    id: str


class FASTApiConfig(BaseModel):
    host: str
    port: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../../.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        env_nested_delimiter='__' 
    )

    GS: GSConfig
    FASTApi: FASTApiConfig

settings = Settings()