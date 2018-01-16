import redis_lua

# requires pytest-redisdb
def test_set_get(redisdb):
    set_get = redis_lua.load_script('set_get', 'lua').get_runner(redisdb)
    data = dict(value='foo bar')
    result = set_get(**data)
    pyredis = redisdb.get('fancykey')
    expected = data['value'].encode('utf-8')
    assert pyredis == expected
    print(pyredis)
    assert result == expected
