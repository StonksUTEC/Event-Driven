from pymongo import MongoClient
import json
def insert_data(str_data):
    client = MongoClient("mongodb://admin:password@localhost:27017/")
    db = client["mydabase"]
    collection = db.my_gfg_collection
     
    # emp_rec1 = {
    #         "name":"Mr.Geek",
    #         "eid":24,
    #         "location":"delhi"
    #         }
    # emp_rec2 = {
    #         "name":"Mr.Shaurya",
    #         "eid":14,
    #         "location":"delhi"
            # }

     
    # Insert Data
    rec_id = collection.insert_one(json.load(str_data))
     
    print("Data inserted with record ids",rec_id)
     
    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)
