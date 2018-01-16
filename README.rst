Minimum Working Example: redis_lua returns str(bytes)
*****************************************************

.. code-block:: bash

    git clone https://github.com/benjaminweb/redis_lua_bytes_bug
    cd redis_lua_bytes_bug
    tox

will return:

.. code-block:: python

        def test_set_get(redisdb):
            set_get = redis_lua.load_script('set_get', 'lua').get_runner(redisdb)
            data = dict(value='foo bar')
            result = set_get(**data)
            pyredis = redisdb.get('fancykey')
            expected = data['value'].encode('utf-8')
            assert pyredis == expected
            print(pyredis)
    >       assert result == expected
    E       assert "b'foo bar'" == b'foo bar'



If your redis-server binary is not placed at
`/usr/local/bin/redis-server` you have to
change the location in pytest.ini.


The relevant code may be here:

https://github.com/ereOn/redis-lua/blob/master/redis_lua/script.py#L333


Feel free to get in touch for questions or general discussion.
