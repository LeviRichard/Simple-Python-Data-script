import json
import os

DB_FILE = 'database.json'

def load_database():
    try:
        if not os.path.exists(DB_FILE):
            with open(DB_FILE,'w') as db:
               json.dump({"PetStoreInventory":[]}, db)
        with open(DB_FILE,'r') as db:
            return json.load(db)
    except Exception as e:
        print(f"Failed to load database {e}")
        return None

def save_database(data):
    try:
        with open(DB_FILE,'w') as db:
            json.dump(data,db, indent=4)
        return True
    except Exception as e:
        print(f"Failed to save database: {e}")
        return False
