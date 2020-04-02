import pymongo
import random

#connecting to the database

def create_community():
    zipcode = input("Enter community zipcode: ")
    community = input("Enter community name: ")
    
    community_name = {
        'zipcode' : zipcode,
        'comm_name': community,
    }
    mydb = myclient["foodpool"]
    mycol = mydb["communities"]
    mycol.insert_one(community_name)

def post_food():
    mydb = myclient["foodpool"]
    mycol = mydb["posts"]
    
    # get number of all posts, then add one, make that the post id??
    food_name = input("Enter food name: ")
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

def totalPosts():
    mydb = myclient["foodpool"]
    mycol = mydb["posts"]

    print("\nTotal number of posts: " + len([i for i in mycol.find()]))

def allUsers():
    mydb = myclient["foodpool"]
    mycol = mydb["users"]
    totalPosts = len([i for i in mycol.find()])

    if (totalPosts == 0):
        print("\nNo users to show!")
    else:
        for i in mycol.find():
            print(i)
    
def add_user():
    mydb = myclient["foodpool"]
    mycol = mydb["users"]
    
    cursor = cnx.cursor()
    user_name = input("Enter Name: ")
    verified = input("Are you verified (y/n) ?: ")
    zipcode = input("What is your zipcode?: ")
    
    user_id = len([i for i in mycol.find()])

    user_record = {
        'user_id' : user_id + 1,
        'user_name' : user_name,
        'verified' : verified,
        'zipcode' : zipcode,
    }
    
    mycol = mydb["users"]
    mycol.insert_one(user_record)

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


# Main Function 
if __name__ == '__main__':

  #Connect to the database
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    

  print("==============================================================")
  print("Welcome to FOOCYCLE - Food sustainability made simple and easy")
  print("==============================================================")

  i = 0 

  while 1:
    
    program_options = ['Create a new community', 'Add user',
                       'All users', 'Post new food item', 'View postings',
                       'Total number of postings', 'exit']

    if (i == 0):
        print("\n" + str(program_options) + "\nWhat would you like to do? Type first word of option:\n")
        user_input = input('Enter option: ')
        i = i + 1

    elif (i != 0):
        print("\n" + str(program_options) + "\nWhat else would you like to do? Type first word of option:\n")
        user_input = input('Enter option: ')
        i = i + 1

    if (user_input == "create"):
        create_community()

    elif (user_input == "view"):
        view_postings()

    elif (user_input == "post"):
        post_food()
        
    elif (user_input == "add"):
        add_user()

    elif (user_input == "total"):
        totalPosts()

    elif (user_input == "all"):
        allUsers()


    elif (user_input == "exit"):
      #Disconnect from the database
      print("Disconnected")
      cnx.close
      break
    
    else:
      print("\nOh no! Invalid command. Try typing one of the following: ",
            "create, add, post, view, total, exit")
      continue