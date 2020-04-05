from flask import Flask, render_template, request, redirect
import json
import os
import random
from pymongo import MongoClient, errors
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Starting Flask with socketio
app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates');
app.config['SECRET_KEY'] = 'randomSecretKey'


# Connect to the database
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# Connecting to MongoDB
print("Connecting to database...")
try:
    myclient = MongoClient(
        host = "localhost:27017",
        serverSelectionTimeoutMS = 3000 # 3 second timeout
    )
    # print the version of MongoDB server if connection successful
    print ("server version:", myclient.server_info()["version"])
    # get the database_names from the MongoClient()
    database_names = myclient.list_database_names()
except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    myclient = None
    database_names = []
    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)
print ("\ndatabases:", database_names)
print("Connected to DB")

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

# ORGANIZED BY CRUD OPERATION

# C(REATE) OPERATIONS
# Create a community, post a food item, register a user

class createCommunity(FlaskForm):
    """Start a new community!"""
    zipcode = StringField("Community's zipcode:", [DataRequired()])
    community = StringField('Name of your community:', [ DataRequired()])

@app.route('/createCommunity', methods=('GET', 'POST'))
def create_community():
    form = createCommunity()
    return render_template('/createCommunity.html', form = form)

@app.route('/createCommunity')
def create_community_submit():
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))
        if (key == "zipcode"):
            zipcode = value
        elif (key == "community"):
            community = value

    print("Found community info:", zipcode, community)

    mydb = myclient["foodpool"]
    mycol = mydb["communities"]

    community_name = {
        'zipcode' : zipcode,
        'comm_name': community,
    }

    mycol.insert_one(community_name)
    return redirect('/home')

class postFood(FlaskForm):
    """Post a Food Item."""
    food_name = StringField('Name of Food', [DataRequired()])
    food_description = StringField('Describe your food!')
    food_price = StringField('Price', [DataRequired()])
    user_id = StringField('User ID')
    submit = SubmitField('Register')

@app.route('/postFood', methods=('GET', 'POST'))
def post_food():
    form = postFood()
    return render_template('/postFood.html', form = form)

@app.route('/postFoodSubmit', methods=('GET', 'POST'))
def post_food_submit():
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))
        if (key == "food_name"):
            food_name = value
        elif (key == "food_description"):
            food_description = value
        elif (key == "food_price"):
            food_price = value
        elif (key == "user_id"):
            user_id = value

    print("Found food info:", food_name, food_description, food_price, user_id)

    mydb = myclient["foodpool"]
    mycol = mydb["posts"]

    # get number of all posts, then add one, make that the post id??
    food_name = input("Enter food name: ")
    food_description = input("Describe your food!: ")
    food_price = input("Enter price of food: ")
    user_id = input("Enter your user id: ")

    post_id = genID(8)

    while post_id in [i['post_id'] for i in mycol.find()]:
        post_id = genID(8)

    post = {
        'post_id' : len([i for i in mycol.find()]) + 1,
        'food_name' : food_name,
        'food_descr': food_description,
        'food_price' : food_price,
        'user_id' : user_id,
    }

    mycol.insert_one(post)
    return redirect('/home')


class registerUser(FlaskForm):
    """Register user form."""
    user_name = StringField('Name', [DataRequired()])
    verified = BooleanField('Are you verified?')
    zipcode = StringField('Zipcode', [DataRequired()])
    submit = SubmitField('Register')

@app.route('/registerUser', methods=('GET', 'POST'))
def add_user():
    form = registerUser()
    return render_template('/registerUser.html', form = form)

@app.route('/registerUserSubmit', methods=('GET', 'POST'))
def add_user_submit():
    for key, value in request.form.items():
        print("key: {0}, value: {1}".format(key, value))
        if (key == "user_name"):
            user_name = value
        elif (key == "verified"):
            verified = value
        elif (key == "zipcode"):
            zipcode = value
    print("Found user info:", user_name, verified, zipcode)

    # Mongo code for inserting data into our database
    mydb = myclient["foodpool"]
    mycol = mydb["users"]
    user_id = genID(8)

    while user_id in [i['user_id'] for i in mycol.find()]:
        user_id = genID(8)

    user_record = {
        'user_id' : user_id,
        'user_name' : user_name,
        'verified' : verified,
        'zipcode' : zipcode,
    }

    mycol.insert_one(user_record)
    return redirect('/home')

@app.route('/totalPosts')
def totalPosts():
    mydb = myclient["foodpool"]
    mycol = mydb["posts"]

    print("\nTotal number of posts: " + len([i for i in mycol.find()]))

@app.route('/allUsers')
def allUsers():
    mydb = myclient["foodpool"]
    mycol = mydb["users"]
    totalPosts = len([i for i in mycol.find()])

    if (totalPosts == 0):
        # print("\nNo users to show!")
        users = ["No users to show!"]
    else:
        # for i in mycol.find():
        #     print(i)
        users = mycol.find()
    return render_template('/allUsers.html', users = users)

@app.route('/viewPostings')
def view_postings():
    mydb = myclient["foodpool"]
    mycol = mydb["posts"]

    totalPosts = len([i for i in mycol.find()])

    if (totalPosts == 0):
        print("\nNo postings to show!")
    else:
        for i in mycol.find():
            print("\nPosting #: " + str(i['post_id'])
                  + ", Food name: " + i['food_name']
                  + ", Description: " + i['food_descr']
                  + ", Price of food: " + i['food_price']
                  + ", Poster: " + i['user_id'] + "\n")

# HELPER FUNCTIONS
def genID(chars):
    idChars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    id = ''
    while len(id) != chars:
        id = id + random.choice(idChars)
    return id



if __name__ == '__main__':
    app.run()
