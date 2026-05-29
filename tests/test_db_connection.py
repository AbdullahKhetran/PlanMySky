import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError

load_dotenv()

def test_mongo_connection():
    uri = os.getenv("MONGO_URI")

    if not uri:
        print("Missing MONGO_URI in .env")
        return

    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)

        client.admin.command("ping")

        print("Connection successful")

        dbs = client.list_database_names()
        print("Databases:", dbs)

    except ConfigurationError as e:
        print("Configuration error:", str(e))

    except ConnectionFailure as e:
        print("Connection failed:", str(e))

    finally:
        try:
            client.close()
        except:
            pass


if __name__ == "__main__":
    test_mongo_connection()