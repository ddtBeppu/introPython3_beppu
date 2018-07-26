# 復習課題 11-1
# プレーンなソケットを使って現在時サービスを実装しよう。
# クライアントがサーバーにtimeという文字列を送ると、ISO文字列で現在の日時を返すものとする。

import time
from datetime import datetime, date
import socket

# サーバーアドレスを設定
server_address = ('localhost', 9999)
# 文字列の上限の長さを定義
max_size = 150

# サーバーの処理開始を知らせる
print('Starting the server at', datetime.now())

# ソケットを作る
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ソケットにバインド
server.bind(server_address)

# クライアントからのデータを待つ
print('Waiting for a client to call.')
data, client = server.recvfrom(max_size)

# 日時の表示形式を定義
fmt = "%A, %B, %d, %Y, %I:%M:%S%p"
# 現在時刻を取得
now_utc = datetime.utcnow()

# フォーマットにしたがって、日時の値を文字列にする
now = now_utc.strftime(fmt)
# 文字列をエンコード
now = now.encode('utf-8')

# クライアントに送信
server.sendto(now, client)
# 通信を終了
server.close()