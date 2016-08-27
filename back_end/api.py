from bottle import get, route
import redis
import json
from datetime import datetime

RED = redis.ConnectionPool(host='redis_01',port=6379,db=0)
LENGTH_OF_PREG = 280

@get('/api/test')
def index():
  return {'status':'fuck you'}

@get('/api/onthislay/<date>')
def return_date(date):
    redis_server = redis.Redis(connection_pool=RED)
    data = {}
    response = redis_server.lrange('dates:' + date, 0, -1)
    data['2000-05-05'] = response[0].decode("utf-8")
    return json.dumps(data)
 
