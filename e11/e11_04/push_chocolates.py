# 復習課題 11-4
# テレビ番組「アイ・ラブ・ルーシー」で、ルーシーとエセルがチョコレート工場で働いていたシーンを覚えているだろうか。
# 紙で包むチョコが送られてくるベルトコンベアがスピードアップすると、彼女たちはついていけなくなる。
# Redisリストに様々なタイプのチョコをプッシュすると、ルーシーがこのリストに対してブロックを起こすポップを行うという
# シミュレーションを書いてみよう。彼女がチョコを1個包むのに0.5秒かかる。ルーシーがポップするたびに時刻とチョコのタイプと
# 残っているチョコが何個あるかを表示しよう。

import redis
import random
from time import sleep

# Redisサーバーに接続
conn = redis.Redis()

# プッシュ開始
print("start pushing chocolates!!")
# 以下のチョコレートを順にプッシュ
chocolates = ["dark", 
                "milk", 
                "white", 
                "regular", 
                "couverture", 
                "ultra couverture", 
                "quality handcrafted gourmet",
                ]

# 
while True:
    # 待ち時間を設けてプッシュする個数の調整
    sleep(random.random())
    # chocolatesリストからチョコレートを抜き出す
    choco = random.choice(chocolates)
    # プッシュする
    conn.rpush("chocos", choco)