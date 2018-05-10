# 復習課題 3-5
# thingsの要素で人間を参照している文字列の先頭文字を大文字にして、リストを表示しよう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> things = ["mozzarella", "cinderella", "salmonella"]  # リストthingsを作成
>>> things[1] = things[1].capitalize()   ###  人間を表す"conderella"の先頭文字を大文字にして、リストを更新
>>> things   ###  リストを表示
['mozzarella', 'Cinderella', 'salmonella']
>>> 

"""