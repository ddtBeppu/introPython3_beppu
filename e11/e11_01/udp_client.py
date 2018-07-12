# 復習課題 11-1
# プレーンなソケットを使って現在時サービスを実装しよう。
# クライアントがサーバーにtimeという文字列を送ると、ISO文字列で現在の日時を返すものとする。

import socket
from datetime import datetime

# サーバーアドレスを設定
server_address = ('localhost', 9999)
# 文字列の最大長を定義
max_size = 150

# クライアントが立ち上がったことを知らせる
print('Starting the client at', datetime.now())
# ソケットを作る
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# サーバーにtimeという文字列を送信
client.sendto(b'time', server_address)

# サーバーからの応答を待つ
data, server = client.recvfrom(max_size)
# サーバーから受信したデータを表示
print(server, 'said', data)
# 通信を終了
client.close()