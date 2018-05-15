# 復習課題 3-14
# e2fのキーから英単語の集合を作って表示しよう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> e2f = {
...     "dog": "chien",  # 英/dog: 仏/chien
...     "cat": "chat",   # 英/cat: 仏/chat
...     "walrus": "morse",   # 英/walrus: 仏/morse
... }
>>> e2f   # 辞書の表示
{'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
>>> key_set = set()   ###  空集合を作成
>>> key_set = key_set.union(e2f.keys())   ###  英仏辞書の全てのキーの値（英語）と、key_setとの和集合を求める
>>> key_set   ###  英単語の集合を表示
{'cat', 'dog', 'walrus'}

"""