# 復習課題 11-3
# XMLRPCで同じことをしてみよう。

from xmlrpc.server import SimpleXMLRPCServer
import time
from datetime import datetime, date

# 日時を返す関数
def reply_time(num):
    # 日時の表示形式を定義
    fmt = "%A, %B, %d, %Y, %I:%M:%S%p"
    # 現在時刻を取得
    now_utc = datetime.utcnow()

    # フォーマットにしたがって、日時の値を文字列にする
    now = now_utc.strftime(fmt)
    # 文字列をエンコード
    reply_str = now.encode('utf-8')

    return reply_str

# サーバーを起動
server = SimpleXMLRPCServer(("localhost", 6789))

# クライアントからのメッセージを受信して、日時を返す
server.register_function(reply_time, "double")
# サービスの提供を開始
server.serve_forever()