from bottle import get, route
import redis
import json
from datetime import datetime

RED = redis.ConnectionPool(host='redis_01',port=6379,db=0)
#RED = redis.ConnectionPool(host='tuchfarber.com',port=6379,db=0)
LENGTH_OF_PREG = 280

@get('/api/test')
def index():
  return {'status':'fuck you'}

@get('/api/onthislay/<date>')
def return_date(date):
    redis_server = redis.Redis(connection_pool=RED)
    data = {}
    data['data'] = {}
    response = redis_server.lrange('dates:' + date, 0, -1)
    data['data']['detail'] = response[0].decode("utf-8")
    data['data']['day'] = date
    return json.dumps(data)
 
