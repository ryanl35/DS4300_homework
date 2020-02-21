# for DataFrame and dictionaries
import pandas as pd

#import python-mongodb connector
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')


# Part 1
#products.productCatalog.find({diameter: "44mm", brand: "Tommy Hilfiger", color: "beige"})


# Part 2 - Search API

class MongoDBClass:

    # def addPeopleToDatabase(self, name, age):
    #     # # create the two lists
    #     # names = ["Vivian", "Hiren", "Ryan", "John", "ChanMin"]
    #     # ages = ["13", "13", "18", "22", "100"]

    #     # # create a Data Frame from a dictionary that has the above information in it
    #     # names_ages = {"Name": name, "Age": age}
    #     # ds4300 = pd.DataFrame(names_ages)

    #     # assign db to the database "assignment3"
    #     db = client["assignment3"]
    #     # assign assignment3 to the collection inside of db "assignment3" titled "names"
    #     assignment3 = db["names"]


    #     # add the name and age into the MongoDB database
    #     # for index, row in ds4300.iterrows():
    #     #     mydict = { "Name": row["Name"], "Age" : row["Age"] }
    #     #     x = assignment3.insert_one(mydict)

    #     # inserts the parameters into a dictionary
    #     mydict = { "Name": name, "Age" : age }
    #     # inserts the dictionary into the database
    #     x = assignment3.insert_one(mydict)

    def addProductToDatabase(self, product, attribute, attibuteValue):

        # assign db to the database "assignment3"
        db = client["assignment3"]
        # assign assignment3 to the collection inside of db "assignment3" titled "names"
        assignment3 = db["products"]

        # inserts the parameters into a dictionary
        # the dictionary contains the input parameter "attribute" as what the value is describing
        mydict = { "Product": product, attribute : attibuteValue }
        # inserts the dictionary into the database
        x = assignment3.insert_one(mydict)

    def queryDatabase(self, dbname, colname, field, query):
        
        # dbname is the name of the database the user wishes to query from
        db = client[dbname]

        # colname is the name of the collection within that database that the user wishes to query from
        assignment3 = db[colname]

        myfind = assignment3.find({field: query})

        for x in myfind:
            print(x)



# Testing to make sure it works
# MongoDBClass.addPeopleToDatabase(MongoDBClass, "Vivian", 13)
# MongoDBClass.queryDatabase(MongoDBClass, "Name", "Vivian")

# MongoDBClass.addProductToDatabase(MongoDBClass, "Table", "Weight", "44lbs")
MongoDBClass.queryDatabase(MongoDBClass, "assignment3", "products", "Weight", "44lbs")


