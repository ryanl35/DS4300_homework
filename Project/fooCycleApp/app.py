from flask import Flask, render_template, request
import json
import os
from pymongo import MongoClient, errors

# Starting Flask with socketio
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates');

# Connecting to MongoDB
print("Connecting to database...")
try:
    client = MongoClient(
        host = "mongodb:27017",
        serverSelectionTimeoutMS = 3000 # 3 second timeout
    )
    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])
    # get the database_names from the MongoClient()
    database_names = client.list_database_names()
except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    client = None
    database_names = []
    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)
print ("\ndatabases:", database_names)
print("Connected to DB")

@app.route('/')
def hello():
    return render_template()

# localhost:5000/postFood?foodName=Chocolate Cake?food_cal=500
@app.route('/postFood')
def post_food():
    mydb = myclient["foodpool"]
    mycol = mydb["posts"]
    # get number of all posts, then add one, make that the post id??
    food_name = input("Enter food name: ")
    food_name = request.args.get('foodName'):
    food_description = input("Describe your food!: ")
    food_price = input("Enter price of food: ")
    user_id = input("Enter your user id: ")

    post = {
        'post_id' : len([i for i in mycol.find()]) + 1,
        'food_name' : food_name,
        'food_descr': food_description,
        'food_price' : food_price,
        'user_id' : user_id,
    }

    mycol = mydb["posts"]
    mycol.insert_one(post)


@app.route('/files')
def files():
    if request.args.get('dirName'):
        path = request.args.get('dirName') + '/'
    else:
        path = 'user_files/'
    print(path)
    fileNames = []
    for root, directories, files in os.walk(path):
        print(root)
        print(directories)
        print(files)
        break
    # lines = getFileContents()
    return render_template('files.html', root = root, directories = directories, files = files)


if __name__ == '__main__':
    app.run()
