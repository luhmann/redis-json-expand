import redis
import json

keys = {
    "partial:1": {
        "id": 1,
        "type": "image",
        "title": "Foo1"
    },
    "partial:2": {
        "id": 2,
        "type": "video",
        "title": "Foo2",
        "image": "partial:1"
    },
    "page:1": {
        "id": "homepage",
        "stage": {
            "reference": "partial:1"
        },
        # non-existing entry
        "sushi1": "partial:3"
    }
}

redisHandle = redis.StrictRedis(host="localhost", port=6379, db=0)
redisHandle.flushall()

for key, value in keys.iteritems():
    redisHandle.set(key, json.dumps(value))
