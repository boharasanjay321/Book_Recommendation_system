import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
 
DATA_FILE_PATH1="/config/workspace/Book_System/Books.csv"
DATA_FILE_PATH2="/config/workspace/Book_System/Ratings.csv"
DATA_FILE_PATH3="/config/workspace/Book_System/Users.csv"

DATABASE_NAME="book_reco_system"
COLLECTION_NAME1="book"
COLLECTION_NAME2="rating"
COLLECTION_NAME3="users"


if __name__=="__main__":

    books=pd.read_csv(DATA_FILE_PATH1)
    rating=pd.read_csv(DATA_FILE_PATH2)
    users=pd.read_csv(DATA_FILE_PATH3)


    books.reset_index(drop=True,inplace=True)
    rating.reset_index(drop=True,inplace=True)
    users.reset_index(drop=True,inplace=True)
    books=list(json.loads(books.T.to_json()).values())
    rating=list(json.loads(rating.T.to_json()).values())
    users=list(json.loads(users.T.to_json()).values())


    client[DATABASE_NAME][COLLECTION_NAME1].insert_many(books)
    client[DATABASE_NAME][COLLECTION_NAME2].insert_many(rating)
    client[DATABASE_NAME][COLLECTION_NAME3].insert_many(users)



    
    

#convert dataframe to json and dump data in mongodb

