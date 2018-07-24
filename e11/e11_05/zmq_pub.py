# 復習課題 11-5
# ZeroMQを使って7.3節の詩の単語を一度に一つずつパブリッシュしよう。
# また、母音で始まる単語を表示するZeroMQサブスクライバと、５字の単語を表示する別のサブスクライバを書こう。
# 句読点などの記号は無視して良い。

import re
import zmq

host = '*'
port = 6789
context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind('tcp://%s:%s' % (host, port))

mammoth = '''We have seen the Queen of cheese,
            Laying quietly at your ease,
            Gently fanned by evening breeze –
            Thy fair form no flies dare seize.
            All gaily dressed soon you'll go
            To the great Provincial Show,
            To be admired by many a beau
            In the city of Toronto.
            Cows numerous as a swarm of bees –
            Or as the leaves upon the trees –
            It did require to make thee please,
            And stand unrivalled Queen of Cheese.
            May you not receive a scar as
            We have heard that Mr. Harris
            Intends to send you off as far as
            The great World's show at Paris.
            Of the youth – beware of these -
            For some of them might rudely squeeze
            And bite your cheek; then songs or glees
            We could not sing o' Queen of Cheese.
            We'rt thou suspended from baloon,
            You'd caste a shade, even at noon;
            Folks would think it was the moon
            About to fall and crush them soon.'''

while True:
    word = re.findall(r'\W\w*', mammoth)
    word.bytes = word.encode('utf-8')
    publisher.send_multipart([])
