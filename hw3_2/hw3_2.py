import argparse

from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb://localhost:27017/'

client = MongoClient(uri, server_api=ServerApi('1'))
db = hw3.mds

parser = argparse.ArgumentParser(description="Aplication cats")
parser.add_argument("--action", help="create, update, read, delete")
parser.add_argument("--id", help="id")
parser.add_argument("--name", help="name")
parser.add_argument("--age", help="age")
parser.add_argument("--features", help="features", nargs="+")

args = vars(parser.parse_args())
action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]

def read():
    return db.hw3.find()

def create(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return db.hw3.insert_one(cat)

def update(pk, name, age, features):
    new_cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return db.hw3.update_one({"_id": ObjectId(pk)}, {"$set": new_cat})

def delete(pk):
    return db.hw3.delete_one({"_id": ObjectId(pk)})

if __name__ == "__main__":
    match action:
        case "read":
           results = read()
           [print(cat) for cat in results]

        case "create":
            result = create(name, age, features)
            print(var(result))

        case "update":
            result = update(pk, name, age, features)
            print(result)

        case "delete":
            result = delete(pk)
            print(result)

        case _:
            print("Invalid action")








