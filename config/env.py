from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    BRAVE_SEARCH_KEY: str
    OPENAI_API_KEY: str


settings = Settings()
