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
### リスト内包表記により、偶数リストを作成
>>> list = [number for number in range(10) if number%2 == 0]
###  リストの値を表示
>>> list
[0, 2, 4, 6, 8]
>>> 

"""