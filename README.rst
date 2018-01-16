Minimum Working Example: redis_lua returns str(bytes)
*****************************************************

.. code-block:: bash

    git clone https://github.com/benjaminweb/redis_lua_bytes_bug
    cd redis_lua_bytes_bug
    tox


If your redis-server binary is not placed at
/usr/local/bin/redis-server you have to
change the location in pytest.ini.


The relevant code may be here:

https://github.com/ereOn/redis-lua/blob/master/redis_lua/script.py#L333
