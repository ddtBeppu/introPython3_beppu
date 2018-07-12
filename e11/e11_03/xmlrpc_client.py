# 復習課題 11-3
# XMLRPCで同じことをしてみよう。

import xmlrpc.client

# サーバーに接続
proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
# 送信するメッセージを定義
message = "time"
# サーバーからの応答を格納
result = proxy.double(message)

# 送受信の結果を表示
print("Sent: ", message, ", Receive: ", result)