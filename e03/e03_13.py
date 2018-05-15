# 復習課題 3-13
# f2eを使って、フランス語のchienに対する英語の単語を表示しよう。

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
>>> f2e = {}   ### 空の辞書f2eを作成
#  辞書e2fの内容を順に参照しながら、辞書を更新
#  nameは英語、keyはフランス語
>>> for name, key in e2f.items():
...     f2e.update({key: name})  新しい辞書f2eの内容に、英/仏が逆順の状態で代入
... 
>>> f2e   #   仏英辞書になっていることを確認
{'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
>>> f2e["chien"]   ###  フランス語の'chien'に対応する語を表示
'dog'
>>> 

"""