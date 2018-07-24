# 復習課題 11-5
# ZeroMQを使って7.3節の詩の単語を一度に一つずつパブリッシュしよう。
# また、母音で始まる単語を表示するZeroMQサブスクライバと、５字の単語を表示する別のサブスクライバを書こう。
# 句読点などの記号は無視して良い。

import zmq
host = '127.0.0.1'
port = 6789
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect('tcp://%s:%s' % (host, port))

#targets = ['a', 'i', 'u', 'e', 'o']
while True:
    target = '[aiueo]*\w'
    subscriber.setsockopt(zmq.SUBSCRIBE, target.encode('utf-8'))

    word_bytes = subscriber.recv_multipart()
    word = word_bytes.decode('utf-8')
    print('Subscribe: %s' % word)
