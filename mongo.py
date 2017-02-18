import pymongo
uri="mongodb://[userName]:[passWord]@ds137759.mlab.com:37759/mytasklist";
client=pymongo.MongoClient(uri);
db=client.get_default_database();
tks=db["tasks"];
def find_one():
    cursers=tks.find({"title":"lundery"});
    return(cursers);
    #for c in cs:
     #   print(c.get("isDone"));
    
def find_all():
    cursers=tks.find();
    for curser in cursers:
        print(curser);
def update():
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
def delete_record():
    tks.delete_one({"title":"reading"});
    
    
    


if __name__=="__main__":
    find_all();
    update();
    delete_record();
    find_one();
    
        
    
    
    
    
    

