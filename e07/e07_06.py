# 復習課題 7-6
# 'salutation', 'name', 'product', 'verbed'(過去形の動詞)、
# 'room', 'animals', 'amount', 'percent', 'spokesman', 'job_title'という文字列キーに値を追加して、
# responseという辞書を作ろう。そして、responseの値を使ってletterを表示しよう。

import re

letter = "Dear {salutation} {name},\
\n\
\nThank you for your letter. We are sorry that our {product} {verbed} in your\
\n{room}. Please note that it should never be used in a {room}, especially\
\nnear any {animals}.\
\n\
\nSend us your receipt and {amount} for shipping and handling. We will send\
\nyou another {product} that, in our tests, is {percent}% less likely to\
\nhave {verbed}.\
\n\
\nThank you for your support.\
\n\
\nSincerely,\
\n{spokesman}\
\n{job_title}"

response = {'salutation': 'Mr.', \
            'name': 'Simon', \
            'product': 'cleaner', \
            'verbed': 'stopped', \
            'room': 'kitchen', \
            'animals': 'cats', \
            'amount': '$200', \
            'percent': '5', \
            'spokesman': 'Micheal', \
            'job_title': 'Chief Technician'}

letter2 = re.sub('{', '{0[', letter)
letter2 = re.sub('}', ']}', letter2)

print("\n", letter2.format(response))


# 実行結果
"""
NaotonoMacBook-puro:e07 naotobeppu$ python e07_06.py 

 Dear Mr. Simon,

Thank you for your letter. We are sorry that our cleaner stopped in your
kitchen. Please note that it should never be used in a kitchen, especially
near any cats.

Send us your receipt and $200 for shipping and handling. We will send
you another cleaner that, in our tests, is 5% less likely to
have stopped.

Thank you for your support.

Sincerely,
Micheal
Chief Technician
"""