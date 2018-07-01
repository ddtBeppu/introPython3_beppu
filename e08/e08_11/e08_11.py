# 復習課題 8-11
# RedisサーバーというPythonのredisライブラリをインストールしよう（後者はpip install redis）。
# そして、count(1), name('Fester Bestertester')フィールドを持つtestというRedisハッシュを作り、
# testの全てのフィールドを表示しよう。

import redis

# Redisサーバーに接続
conn = redis.Redis()
# ハッシュを作成
conn.hmset('test', {'count': '1', 'name': 'Fester Bestertester'})

# すべてのフィールドのキーと値を取得する。
output = conn.hgetall('test')
# 表示
print(output)

# 実行結果
"""
NaotonoMacBook-puro:e08_11 naotobeppu$ python e08_11.py 
{b'count': b'1', b'name': b'Fester Bestertester'}
"""