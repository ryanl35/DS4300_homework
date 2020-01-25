import redis



def connect():
    connection = redis.Redis(host=' ',
                                 user=' ',
                                 password='')
    return connection

    
