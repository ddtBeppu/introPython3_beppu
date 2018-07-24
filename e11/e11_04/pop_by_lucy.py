# 復習課題 11-4
# テレビ番組「アイ・ラブ・ルーシー」で、ルーシーとエセルがチョコレート工場で働いていたシーンを覚えているだろうか。
# 紙で包むチョコが送られてくるベルトコンベアがスピードアップすると、彼女たちはついていけなくなる。
# Redisリストに様々なタイプのチョコをプッシュすると、ルーシーがこのリストに対してブロックを起こすポップを行うという
# シミュレーションを書いてみよう。彼女がチョコを1個包むのに0.5秒かかる。ルーシーがポップするたびに時刻とチョコのタイプと
# 残っているチョコが何個あるかを表示しよう。

import redis
import time
from datetime import datetime
from time import sleep

# redisサーバーに接続
conn = redis.Redis()
# タイムアウトの時間(秒)
timeout = 10
waiting_time = 0.5

print("start!")
while True:
    # ルーシーがチョコレートを包むのにかかる時間だけ待つ
    sleep(waiting_time)
    # チョコレートのリストからポップする
    msg = conn.blpop("chocos", timeout)
    # 残りの個数を求める
    stock = conn.llen("chocos")

    # メッセージを受信したら
    if msg:
        # メッセージの2番目の要素(ポップしたチョコレート)
        out = msg[1]
        # 包んだチョコレートを表示
        print("Got ", out, "chocolate")
        # 残り個数を表示
        print(stock, "remains.")

        # 現在時刻を取得
        now_utc = datetime.utcnow()
        # 現在時刻を表示
        print("It's ", now_utc)