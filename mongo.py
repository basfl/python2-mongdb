import pymongo
uri="mongodb://[userName]:[passWord]@ds137759.mlab.com:37759/mytasklist";
def find_all(tks):
    cursers=tks.find();
    for curser in cursers:
        print(curser);
def update(tks):
    data=[
        {
            "title":"lundery",
            "isDone":"true"
        },
        {
            "title":"reading",
            "isDone":"true"
        },
        ];
    tks.insert_many(data);
def delete_record(tks):
    tks.delete_one({"title":"reading"});
    
    
    


if __name__=="__main__":
    client=pymongo.MongoClient(uri);
    db=client.get_default_database();
    tks=db["tasks"];
    find_all(tks);
    update(tks);
    delete_record(tks);
    
    
    
    

