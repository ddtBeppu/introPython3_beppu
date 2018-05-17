# 復習課題 4-6
# 集合内包表記を使って、range(10)の奇数からoddという集合を作ろう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。


"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

### 集合内包表記を使って、奇数の値の集合を作成
>>> odd = {number for number in range(10) if number % 2 == 1}
###  集合の値を表示
>>> odd
{1, 3, 5, 7, 9}
>>> 


"""