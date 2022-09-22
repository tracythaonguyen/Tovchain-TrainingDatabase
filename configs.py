import os

from dotenv import load_dotenv

load_dotenv()


class MongoDBConfig:
    MONGODB_HOST = os.environ.get("MONGODB_HOST", 'localhost')
    MONGODB_PORT = os.environ.get("MONGODB_PORT", '27017')
    USERNAME = os.environ.get("MONGODB_USERNAME", 'admin')
    PASSWORD = os.environ.get("MONGODB_PASSWORD", 'admin123')
    # CONNECTION_URL = f'mongodb://{USERNAME}:{PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}'
    # CONNECTION_URL = f'mongodb://admin:admin123@localhost:27017'
    CONNECTION_URL = f'mongodb://admin:admin123@localhost:27017/?authMechanism=DEFAULT&authSource=trainingDB'
