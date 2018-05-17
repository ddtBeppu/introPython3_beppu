# 復習課題 4-7
# ジェネレータ内包表記を使って、range(10)の数値に対しては、'Got'と数値を返そう。forループを使って反復処理すること。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
### ジェネレータ内包表記を使って、タプルを作成
>>> num_thing = (num for num in range(10))
###  タプルnum_thingの値の数だけ、ループ
>>> for number in num_thing:
        #### 文字列と数値を連結して表示
...     print('Got', number)
... 


### 実行結果
Got 0
Got 1
Got 2
Got 3
Got 4
Got 5
Got 6
Got 7
Got 8
Got 9
>>> 


"""