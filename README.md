# DS4300_Assignment2

Members: Ryan Liang, Vivian Chen, Hiren Patel

We used code from the first HW that would create two .csv files, one that has all of the generated followers (generatedFollowers.csv) and all of the tweets that all of the users have generated (generatedTweets.csv), which ended up totaling to 1,000,000. 

For Strategy 1, we interpreted it as the following:

When a user posts a tweet, we would simply add that tweet to Redis as a key and value store. This is what was stated in the assignment but is an important clarification when it comes to distinguishing the different strategies. This would mean that fetching the timelines for the users would involve receiving all the tweets from the people that the current user follows. The way we structured our data was that we made each user's tweets its own key, and the values that each key would store the text of the tweets and timestamp of that tweet.

We implemented postTweet() Strategy 1 by iterating through every tweet in the generatedTweets.csv file, and we would add it to Redis using the command "zadd". "zadd" would take in a key, which would be the tweets, followed by the user_id of the user posting. This would clarify which user_id posted the tweets that are found within the key. Then, they key would store all of the tweets that the user posted (the text and the timestamp).

We implemented getTimeline() Strategy 1 by iterating through every user and retrieving the list of users that each person follows using the Redis command "smembers". After we generated this list, we would get all of that user's tweets by using the Redis command "zrange", which took in a key (this user's tweets:id), and the range, which we made 0 and -1, to retrieve all of the tweets. 


For Strategy 2, we interpreted it as the following:

When a user posts a tweet, we would go through each person that  then this tweet is posted to we decided to go with a different implementation by using a Hash in Redis. We interpreted the strategy as inserting the tweet information into each follower's timeline when a user posts a tweet. Therefore, the followers only having to retrieve their timelines in order to see the newest tweets.

We implemented postTweet() in Strategy 2 by using similar code from Strategy 1, where we would iterate through each tweet and add it to Redis using the command "zadd". "zadd" would also take in the user_id, text, and timestamp. What differs between the strategies is that we also added the tweet information to each of the user's followers. We used "hset" to add it to the respective "timeline:userID" sets.

We implemented getTimeline() Strategy 2 by iterating through every user and filtering for the set "timeline:<userID>", and using "hgetall" to retrieve all the tweets in that user's timeline.