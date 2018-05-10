# 復習課題 3-11
# 3つの単語が含まれている辞書e2fを使って、walrusという単語に対応するフランス語の単語を表示しよう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
# 辞書の作成
>>> e2f = {
...     "dog": "chien",  # 英/dog: 仏/chien
...     "cat": "chat",   # 英/cat: 仏/chat
...     "walrus": "morse",   # 英/walrus: 仏/morse
... }
>>> e2f   # 辞書の表示
{'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
>>> e2f["walrus"]    ### "walrus"に対応するフランス語を表示する
'morse'
>>> 

"""