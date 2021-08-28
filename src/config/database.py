import os

from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "database": os.getenv("DATABASE"),
    "port": os.getenv("PORT"),
    "user": os.getenv("USERDB"),
    "password": os.getenv("PASSWDDB")
}
