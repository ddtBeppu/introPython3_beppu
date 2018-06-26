# 復習課題 7-5
# 新しいスタイルの書式指定を使って定型書簡を作りたい。次の文字列をletterという変数に保存しよう(次の問題で使う)。

"Dear {salutation} {name},\
\
Thank you for your letter. We are sorry that our {product} {verbed} in your\
{room}. Please note that it should never be used in a {room}, especially\
near any {animals}.\
\
Send us your receipt and {amount} for shipping and handling. We will send\
you another {product} that, in our tests, is {percent}% less likely to\
have {verved}.\
\
Thank you for your support.\
\
Sincerely,\
{spokesman}\
{job_title}"


# 実行結果
"""
NaotonoMacBook-puro:e07 naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> letter = "Dear {salutation} {name},\
... \
... Thank you for your letter. We are sorry that our {product} {verbed} in your\
... {room}. Please note that it should never be used in a {room}, especially\
... near any {animals}.\
... \
... Send us your receipt and {amount} for shipping and handling. We will send\
... you another {product} that, in our tests, is {percent}% less likely to\
... have {verved}.\
... \
... Thank you for your support.\
... \
... Sincerely,\
... {spokesman}\
... {job_title}"
>>> 
"""