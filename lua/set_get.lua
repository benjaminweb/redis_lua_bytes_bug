%arg value string
%return string

redis.call('SET', 'fancykey', value)
return redis.call('GET', 'fancykey')
