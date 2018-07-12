# 復習課題 11-2
# ZeroMQのREQ、REPソケットを使って同じことをしてみよう。

import zmq

# ホストアドレス
host = '127.0.0.1'
# ポート番号
port = 6789

# 状態を管理するオブジェクトの生成
context = zmq.Context()
# 要求するタイプのソケットを作成
client = context.socket(zmq.REQ)

# サーバーに通信
client.connect("tcp://%s:%s" % (host, port))

# 送信する"time"という値を格納
request_str = "time"
# エンコード
request_bytes = request_str.encode('utf-8')
# サーバーに送信
client.send(request_bytes)

# サーバーからの応答の値を格納
reply_bytes = client.recv()

# デコード
reply_str = reply_bytes.decode('utf-8')
# 送受信の結果を表示
print("Sent %s, received %s" % (request_str, reply_str))
