import redis
import argparse
import json

parser = argparse.ArgumentParser(description='Gets a key from redis expanding further keys')
parser.add_argument('--key', dest='key', help='The key you want to get')
args = parser.parse_args()

redisHandle = redis.StrictRedis(host="localhost", port=6379, db=0)

lua = """
function string.starts(String,Start)
   return string.sub(String,1,string.len(Start))==Start
end

local parse = nil
function parse (tree)
    for k,v in pairs(tree) do
        if type(v) == 'string' and string.starts(v, 'partial') then
            local subtree = cjson.decode(redis.call('GET', v))
            tree[k] = parse(subtree)
        end

        if type(v) == 'table' then
            tree[k] = parse(v)
        end
    end
    return tree
end



local base = redis.call('GET', KEYS[1])

return cjson.encode(parse(cjson.decode(base)))
"""

query = redisHandle.register_script(lua)

result = json.loads(query(keys=[args.key]))

print result
