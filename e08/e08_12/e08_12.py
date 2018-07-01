# 復習課題 8-12
# testのcountフィールドをインクリメントして、結果を表示しよう。

import redis

# Redisサーバーに接続
conn = redis.Redis()
# ハッシュを作成
# countフィールドをインクリメント
conn.hmset('test', {'count': [count for count in range(1,5)], 'name': 'Fester Bestertester'})

# すべてのフィールドのキーと値を取得する。
output = conn.hgetall('test')
# 表示
print(output)

# 実行結果
"""
NaotonoMacBook-puro:e08_12 naotobeppu$ python e08_12.py 
{b'count': b'[1, 2, 3, 4]', b'name': b'Fester Bestertester'}
"""