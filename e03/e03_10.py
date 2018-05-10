# 復習課題 3-10
# e2fという英仏辞書を作り、それを表示しよう。この辞書は次のデータが初期状態で入っていることとする。
# dogはchien, catはchat, walrusはmorse。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
### 辞書の作成
>>> e2f = {
...     "dog": "chien",  ### 英/dog: 仏/chien
...     "cat": "chat",   ### 英/cat: 仏/chat
...     "walrus": "morse",   ### 英/walrus: 仏/morse
... }
>>> e2f   ### 辞書の表示
{'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
>>> 

"""