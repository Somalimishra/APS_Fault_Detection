import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv" #r8 click on csv file and copy the path
DATABSE_NAME="aps" # database name
COLLECTION_NAME="sensor" # table name

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)  #reading csv file
    print(f"Rows and Columns: {df.shape}") # check the shape of file

    #convert dataframe to json so that we can dump these record in mongodb
    df.reset_index(drop=True,inplace=True)             #resetting the index

    json_record=list(json.loads(df.T.to_json()).values())   ##converting the file into json
    print(json_record[0])

    #insert converted json record to mongo db
    client[DATABSE_NAME][COLLECTION_NAME].insert_many(json_record)




