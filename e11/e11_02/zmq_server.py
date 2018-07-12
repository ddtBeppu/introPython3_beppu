# 復習課題 11-2
# ZeroMQのREQ、REPソケットを使って同じことをしてみよう。

import zmq
import time
from datetime import datetime, date

# ホストアドレス
host = '127.0.0.1'
# ポート番号
port = 6789

# 状態を管理するオブジェクトの生成
context = zmq.Context()
# 応答するタイプのソケットを作成
server = context.socket(zmq.REP)

# IPアドレスとポートをリスンする
server.bind("tcp://%s:%s" % (host, port))

# 通信が正常に行われている場合
while True:
    # クライアントからのデータを受け取り格納
    request_bytes = server.recv()
    # デコード
    request_str = request_bytes.decode('utf-8')

    # クライアントから送られた値を表示
    print("That voice in my head says: %s" % request_str)

    # 日時の表示形式を定義
    fmt = "%A, %B, %d, %Y, %I:%M:%S%p"
    # 現在時刻を取得
    now_utc = datetime.utcnow()

    # フォーマットにしたがって、日時の値を文字列にする
    now = now_utc.strftime(fmt)
    # 文字列をエンコード
    reply_str = now.encode('utf-8')

    # クライアントに日時の値を返す
    server.send(reply_str)