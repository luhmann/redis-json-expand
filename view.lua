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

        if (type(v) == 'table') then
            tree[k] = parse(v)
        end
    end
    return tree
end



local base = redis.call('GET', KEYS[1])

return cjson.encode(parse(cjson.decode(base)))
