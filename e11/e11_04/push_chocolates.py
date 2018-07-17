# 復習課題 11-4
# テレビ番組「アイ・ラブ・ルーシー」で、ルーシーとエセルがチョコレート工場で働いていたシーンを覚えているだろうか。
# 紙で包むチョコが送られてくるベルトコンベアがスピードアップすると、彼女たちはついていけなくなる。
# Redisリストに様々なタイプのチョコをプッシュすると、ルーシーがこのリストに対してブロックを起こすポップを行うという
# シミュレーションを書いてみよう。彼女がチョコを1個包むのに0.5秒かかる。ルーシーがポップするたびに時刻とチョコのタイプと
# 残っているチョコが何個あるかを表示しよう。

import redis

conn = redis.Redis()

chocolates = ["dark", 
                "milk", 
                "white", 
                "regular", 
                "couverture", 
                "ultra couverture", 
                "quality handcrafted gourmet",
                ]

for chocolate in chocolates:
    msg = chocolate.encode('utf-8')
    conn.rpush('chocolate', msg)

conn.rpush('chocolate', 'quit')

print('Out of demand!')