## What is this

A POC implementation of expanding keys in redis values to the values they reference

## How to execute

#### 1. Install dependencies

`brew install redis python`

#### 2. Install python libraries

`pip install redis`

####  3. Install redis fixtures

`python buildRedis.py`

#### 4. Call Redis with lua script (works with bash)

simple:

`redis-cli eval "$(cat view.lua)" 1 partial:2`

nested:

`redis-cli eval "$(cat view.lua)" 1 page:1`

or use python:

`python queryRedis.py --key='page:1'`

This should be `shaeval` in the final code, with
a preregistered script, see http://www.redisgreen.net/blog/intro-to-lua-for-redis-programmers/
