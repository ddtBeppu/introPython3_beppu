# 復習課題 4-4
# リスト内包表記を使って、range(10)の偶数リストを作ろう。 

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。


"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> list = []   ###  空のリストを作成。値を追加していく。
###  0から9までの値で、偶数のみを参照しながらループ
>>> for i in range(0, 10, 2):
        iの値を追加
...     list.append(i)
... 
>>> list   ###  listの値を表示
[0, 2, 4, 6, 8]
>>> 

"""