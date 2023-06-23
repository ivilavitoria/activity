from pymongo import MongoClient
from bson.objectid import ObjectId

TASK_COLLECTION_NAME = "tasks"

def get_database():
    # Fornecer a URL do mongodb atlas para conectar python ao mongodb usando pymongo (add string de conexão com meu banco de dados)
    CONNECTION_STRING = "mongodb+srv://admin:fgRsevzWmrupxkD5@product-manager.lor6uci.mongodb.net/?retryWrites=true&w=majority"

    # Conexão usando MongoClient

    client = MongoClient(CONNECTION_STRING)

    # Criando o banco de dados 
    return client ['task-manager']

def list_tasks():
    dbTaskManager = get_database()
    collection_name = dbTaskManager[TASK_COLLECTION_NAME]
    
    item_details = collection_name.find()
    #for item in item_details:
        #print(item)

    return item_details

#usuário pode cadastrar sua task 
def save_task(task):
    dbTaskManager = get_database()
    collection_name = dbTaskManager[TASK_COLLECTION_NAME]
    
    collection_name.insert_one(task)

def delete_task(id):
    dbTaskManager = get_database()
    collection_name = dbTaskManager[TASK_COLLECTION_NAME]

    myquery = { "_id": ObjectId(id) }
    
    collection_name.delete_one(myquery)