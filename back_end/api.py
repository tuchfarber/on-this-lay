from bottle import get, route
import redis
import json
import sys
import random
from datetime import date, timedelta

#RED = redis.ConnectionPool(host='redis_01',port=6379,db=0)
RED = redis.ConnectionPool(host='tuchfarber.com',port=6379,db=0)
LENGTH_OF_PREG = 280
WEEK = 7

@get('/api/test')
def index():
  return {'status':'fuck you'}

@get('/api/onthislay/<date>')
def return_date(sent_date):
    #Create the redis connection
    redis_server = redis.Redis(connection_pool=RED)

    # Init dictionary
    data = {}
    data['data'] = {}


    birthday = get_date(sent_date)
    conception = birthday - timedelta(LENGTH_OF_PREG + WEEK)

    all_events = {}
  
    for i in range(1, 14):
        possible_conception_date = conception + timedelta(i)
        sys.stdout.write(possible_conception_date.isoformat() + "\n")
        sys.stdout.flush()
        response = redis_server.lrange('dates:' + 
                                       possible_conception_date.isoformat(),
                                       0, -1)
        if len(response) > 0:
            data['data']['detail'] = response[0].decode("utf-8")
            data['data']['day'] = sent_date
            all_events[possible_conception_date] = json.dumps(data)
    
    # key_to_use = random.choice(all_events.keys())
    for key, value in all_events.items():
         return all_events[key]
    #    sys.stdout.write('Date: ' + key.isoformat() + "\n")
    #    sys.stdout.write('Value: ' + value + "\n")
    #    sys.stdout.flush()
 
def get_date(sent_date):
    splitd = sent_date.split('-')
    return date(int(splitd[0]), int(splitd[1]), int(splitd[2]))
    
