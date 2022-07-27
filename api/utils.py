from pymongo import MongoClient

connection_string = '####################################'

client = MongoClient(connection_string)

db = client['TaskListManager']

collection = db['Lists']
