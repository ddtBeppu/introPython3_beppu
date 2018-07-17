# 復習課題 11-4
# テレビ番組「アイ・ラブ・ルーシー」で、ルーシーとエセルがチョコレート工場で働いていたシーンを覚えているだろうか。
# 紙で包むチョコが送られてくるベルトコンベアがスピードアップすると、彼女たちはついていけなくなる。
# Redisリストに様々なタイプのチョコをプッシュすると、ルーシーがこのリストに対してブロックを起こすポップを行うという
# シミュレーションを書いてみよう。彼女がチョコを1個包むのに0.5秒かかる。ルーシーがポップするたびに時刻とチョコのタイプと
# 残っているチョコが何個あるかを表示しよう。

import redis
import time
from datetime import datetime, date

conn = redis.Redis()

while True:
    msg = conn.blpop('chocolate')
    if not msg:
        break

    val = msg[1].decode('utf-8')
    if val == 'quit':
        break

    print("Got ", val)

    # 日時の表示形式を定義
    time_fmt = "%A, %B, %d, %Y, %I:%M:%S%p"
    # 現在時刻を取得
    now_utc = datetime.utcnow()
    # フォーマットにしたがって、日時の値を文字列にする
    now = now_utc.strftime(time_fmt)

    # 文字列をエンコード
    now_time = now.encode('utf-8')
    print("It's ", now_time)