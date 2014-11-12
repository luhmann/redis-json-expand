import redis
import argparse
import json
import os

parser = argparse.ArgumentParser(description='Gets a key from redis expanding further keys')
parser.add_argument('--key', dest='key', help='The key you want to get')
args = parser.parse_args()

redisHandle = redis.StrictRedis(host="localhost", port=6379, db=0)
base_dir = os.path.dirname(os.path.realpath(__file__))

with open (os.path.join(base_dir, 'view.lua'), "r") as file:
    lua=file.read()

query = redisHandle.register_script(lua)

result = json.loads(query(keys=[args.key]))

print result
