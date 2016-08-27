from bottle import get, route
import redis
import json
import sys
import random
from datetime import date, timedelta

RED = redis.ConnectionPool(host='redis_01',port=6379,db=0)
#RED = redis.ConnectionPool(host='tuchfarber.com',port=6379,db=0)
LENGTH_OF_PREG = 280
WEEK = 7

@get('/api/test')
def index():
  return {'status':'fuck you'}

@get('/api/onthislay/<sent_date>')
def return_date(sent_date):
    #Create the redis connection
    redis_server = redis.Redis(connection_pool=RED)

    # Init dictionary
    data = {}
    data['data'] = {}

    birthday = get_date(sent_date)
    conception = birthday - timedelta(days=(LENGTH_OF_PREG + WEEK))

    all_events = []
  
    for i in range(1, 14):
        possible_conception_date = conception + timedelta(days=i)
        response = redis_server.lrange('dates:' + 
                                       possible_conception_date.isoformat(),
                                       0, -1)
        if len(response) > 0:
            data['data']['detail'] = response[0].decode("utf-8")
            data['data']['day'] = possible_conception_date.isoformat()
            all_events.append(json.dumps(data))
    
    return random.choice(all_events)
 
def get_date(sent_date):
    splitd = sent_date.split('-')
    return date(int(splitd[0]), int(splitd[1]), int(splitd[2]))
    
