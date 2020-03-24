
import mysql.connector
import random

#connecting to the database

def create_community():
    cursor = cnx.cursor()
    zipcode = input("Enter community zipcode: ")
    community = input("Enter community name: ")
    add_community_name = ("INSERT INTO communities "
                          "(zipcode, comm_name) "
                          "VALUES (%(zipcode)s, %(comm_name)s)")
    community_name = {
        'zipcode' : zipcode,
        'comm_name': community,
    }
    cursor.execute(add_community_name, community_name)
    cnx.commit()
    cursor.close()

def post_food():
    cursor = cnx.cursor()
    # get number of all posts, then add one, make that the post id??
    food_name = input("Enter food name: ")
    food_description = input("Describe your food!: ")
    food_price = input("Enter price of food: ")
    user_id = input("Enter your user id: ")

    query = ("SELECT COUNT(post_id) FROM posts")

    cursor.execute(query)

    post_id = 0
    
    for i in cursor.fetchall():
        post_id = i[0]

    add_post = ("INSERT INTO posts "
                "(post_id, food_name, food_descr, food_price, user_id) "
                "VALUES (%(post_id)s, %(food_name)s,"
                "%(food_descr)s, %(food_price)s, %(user_id)s)")
    post = {
        'post_id' : post_id + 1,
        'food_name' : food_name,
        'food_descr': food_description,
        'food_price' : food_price,
        'user_id' : user_id,
    }
    cursor.execute(add_post, post)
    cnx.commit()
    cursor.close()

def totalPosts():
    cursor = cnx.cursor()

    query = ("SELECT COUNT(post_id) FROM posts")

    cursor.execute(query)

    for i in cursor.fetchall():
        print("\nTotal number of posts: " + str(i[0]))

def allUsers():
    cursor = cnx.cursor()

    query = ("SELECT user_id FROM users")
    queryNumUsers = ("SELECT COUNT(*) FROM users")

    cursor.execute(queryNumUsers)

    totalUsers = 0;

    for i in cursor:
        totalPosts = i[0]

    if (totalPosts == 0):
        print("\nNo users to show!")
    else:
        cursor.execute(query)
        for i in cursor.fetchall():
            print("\nuser_id: " + str(i[0]))

    
def add_user():
    cursor = cnx.cursor()
    user_name = input("Enter Name: ")
    verified = input("Are you verified (y/n) ?: ")
    zipcode = input("What is your zipcode?: ")

    query = ("SELECT COUNT(*) FROM users")

    cursor.execute(query)

    user_id = 0
    
    for i in cursor.fetchall():
        user_id = i[0]
    
    add_user = ("INSERT INTO users "
                          "(user_id, user_name, verified, zipcode) "
                          "VALUES (%(user_id)s, %(user_name)s, %(verified)s, %(zipcode)s)")
    user_record = {
        'user_id' : user_id + 1,
        'user_name' : user_name,
        'verified' : verified,
        'zipcode' : zipcode,
    }
    cursor.execute(add_user, user_record)
    cnx.commit()
    cursor.close()

def view_postings():
  cursor = cnx.cursor()
  query = ("SELECT * FROM posts")
  queryNumPosts = ("SELECT COUNT(*) FROM posts")

  cursor.execute(queryNumPosts)

  totalPosts = 0;

  for i in cursor:
      totalPosts = i[0]

  if (totalPosts == 0):
      print("\nNo postings to show!")
  else:
    cursor.execute(query)
    for (post_id, food_name, food_descr, food_price, user_id) in cursor:
        print("\nPosting #: " + str(post_id)
              + ", Food name: " + str(food_name)
              + ", Description: " + str(food_descr)
              + ", Price of food: " + str(food_price)
              + ", Poster: " + str(user_id) + "\n")
  
  cursor.close()


# Main Function 
if __name__ == '__main__':

  #Connect to the database
  cnx = mysql.connector.connect(user='root', password='rootroot123',
    host='127.0.0.1',
    database='foodpool',
    auth_plugin='mysql_native_password')

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
        
