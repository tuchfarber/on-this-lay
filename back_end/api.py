from bottle import get
import redis

@get('/api/test')
def index():
  return {'status':'fuck you'}