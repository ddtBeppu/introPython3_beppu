# 復習課題 11-5
# ZeroMQを使って7.3節の詩の単語を一度に一つずつパブリッシュしよう。
# また、母音で始まる単語を表示するZeroMQサブスクライバと、５字の単語を表示する別のサブスクライバを書こう。
# 句読点などの記号は無視して良い。

import zmq

# ホストの指定
host = '127.0.0.1'
# ポート番号の指定
port = 6789
# 状態を管理するオブジェクトを作成
context = zmq.Context()
# ソケットのタイプを指定
subscriber = context.socket(zmq.SUB)
# サーバーが特定のIPアドレスとポートをリスンするようにする
subscriber.connect('tcp://%s:%s' % (host, port))

# トピックは以下の二つ
topics = ['vowels', 'fives']

# トピックごとに処理
for topic in topics:
    # ソケットの設定
    subscriber.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))

# 受信されるデータがある間
while True:
    # 受信したデータを格納
    topic_bytes, chara_bytes = subscriber.recv_multipart()
    # デコードする
    topic = topic_bytes.decode('utf-8')
    # デコードする
    chara = chara_bytes.decode('utf-8')
    # トピックと内容を表示
    print('"',topic, '": ', chara)