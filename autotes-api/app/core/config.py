import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    MONGODB_URI: str = os.getenv("MONGODB_URI")
    DB_NAME: str = os.getenv("DB_NAME")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME")


settings = Settings()
