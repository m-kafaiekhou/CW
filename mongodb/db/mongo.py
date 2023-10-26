# import json
# from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient("mongodb://root:root@0.0.0.0:27017/")

db = client['library']





# with open('data.json') as f:
#     file_data = json.load(f)

# # # if pymongo < 3.0, use insert()
# # collection_users.insert(file_data)
# # # if pymongo >= 3.0 use insert_one() for inserting one document
# # collection_users.insert_one(file_data)
# # if pymongo >= 3.0 use insert_many() for inserting many documents
# collection_users.insert_many(file_data)

# client.close()

# for i in collection_users.find():
#     print(i)


# count_city_most = collection_users.aggregate([
#     { '$group': { '_id': "$location.city", 'count': {'$sum': 1}} },
#     { '$sort': { 'count': -1}},
#     { '$limit': 1 }
# ])

# print([i for i in count_city_most])


# count_city_least = collection_users.aggregate([
#     { '$group': { '_id': "$location.city", 'count': {'$sum': 1}} },
#     { '$sort': { 'count': 1}},
#     { '$limit': 1 }
# ])

# print([i for i in count_city_least])


# avg_age_tehran = collection_users.aggregate([
#     { '$group': { '_id': "$location.city", 'count': {'$sum': 1}} },
#     { '$sort': { 'count': 1}},
#     { '$limit': 1 }
# ])