# 復習課題 2-3
# 1日は何秒か。seconds_per_hour変数を使って計算しよう。


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
>>> seconds_per_hour = hour   # 計算結果を変数seconds_per_hourに代入
>>> seconds_per_hour * 24   ### 1日の秒数 = 1時間の秒数　× 24時間
86400
>>> 

"""