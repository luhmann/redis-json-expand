function string.starts(String,Start)
   return string.sub(String,1,string.len(Start))==Start
end

local parse = nil
function parse (tree)
    for k,v in pairs(tree) do
        if type(v) == 'string' and string.starts(v, 'partial') then
            local subtree = redis.call('GET', v)
            if subtree ~= false then
                tree[k] = parse(cjson.decode(subtree))
            else
                ---  key does not exist -> delete
                tree[k] = nil
            end
        end

        if type(v) == 'table' then
            tree[k] = parse(v)
        end
    end
    return tree
end



local base = redis.call('GET', KEYS[1])
return cjson.encode(parse(cjson.decode(base)))
