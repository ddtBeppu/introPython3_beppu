# 復習課題 2-1
# 1時間は何秒か。対話型インタープリタを電卓として使い、１分の秒数（60）に1時間の分数（同じく60）を掛けて計算してみよう。


# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:introPython3 naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> second = 60  # 秒数を定義。１分=60秒
>>> minute = 60  # 分数を定義。1時間=60分
>>> hour = second * minute  # 計算により、1時間の秒数を求める。
>>> print(hour)  # 計算結果を表示
3600
>>> 

"""