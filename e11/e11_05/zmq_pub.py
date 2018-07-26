# 復習課題 11-5
# ZeroMQを使って7.3節の詩の単語を一度に一つずつパブリッシュしよう。
# また、母音で始まる単語を表示するZeroMQサブスクライバと、５字の単語を表示する別のサブスクライバを書こう。
# 句読点などの記号は無視して良い。

import re
import zmq
import time

# ブロードキャストのため、ホストを限定しない
host = '*'
# ポート番号を指定
port = 6789

# 状態を管理するオブジェクトを作成
context = zmq.Context()
# ソケットのタイプを指定
publisher = context.socket(zmq.PUB)
# サーバーが特定のIPアドレスとポートをリスンするようにする
publisher.bind('tcp://%s:%s' % (host, port))

# 読み込む詩の内容
mammoth = '''We have seen the Queen of cheese,\
            Laying quietly at your ease,\
            Gently fanned by evening breeze –\
            Thy fair form no flies dare seize.\
            All gaily dressed soon you'll go\
            To the great Provincial Show,\
            To be admired by many a beau\
            In the city of Toronto.\
            Cows numerous as a swarm of bees –\
            Or as the leaves upon the trees –\
            It did require to make thee please,\
            And stand unrivalled Queen of Cheese.\
            May you not receive a scar as\
            We have heard that Mr. Harris\
            Intends to send you off as far as\
            The great World's show at Paris.\
            Of the youth – beware of these -\
            For some of them might rudely squeeze\
            And bite your cheek; then songs or glees\
            We could not sing o' Queen of Cheese.\
            We'rt thou suspended from baloon,\
            You'd caste a shade, even at noon;\
            Folks would think it was the moon\
            About to fall and crush them soon.'''

# スペースで単語を区切る
words = mammoth.split(' ')

# 1秒待つ
time.sleep(1)
# 単語ごとに
for word in words:
    # 単語をエンコード
    word_bytes = word.encode('utf-8')

    # 母音で始まる単語
    if word.startswith(('a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O')):
        # トピックと単語を送信
        publisher.send_multipart([b'vowels', word_bytes])

    # 5文字の場合
    if len(word) == 5:
        # トピックと単語を送信
        publisher.send_multipart([b'fives', word_bytes])
