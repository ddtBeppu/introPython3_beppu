# 復習課題 4-2
# 変数guess_meに7、変数startに1を代入し、startとguess_meを比較するwhileループを書こう。
# ループは、startがguess_meよりも小さければ'too low'と表示し、startとguess_meが等しければ'found it!'を表示し、
# startがguess_meよりも大きければ'oops'と表示してループを終了するものとする。
# ループの最後の部分でstartをインクリメントすること。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。


"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> guess_me = 7     ### guess_meの初期値を設定
>>> start = 1    ###  インクリメントを繰り返して、guess_meの値を推定
>>> while True:   ###  break文が実行された時に終了する無限ループ
...     if start < guess_me:   ### startの値がguess_meに満たない
                ###  テキストの表示
...             print('too low')
...     elif start == guess_me:    ###  guess_meの値と等しくなった
                ###  テキストの表示
...             print('found it!')
...     else:    ###  startの値がguess_meを超えてしまった
                ###  テキストの表示
...             print('oops')
                ### ループの終了
...             break
        ### インクリメント
...     start += 1
... 

###  以下、実行結果
too low
too low
too low
too low
too low
too low
found it!
oops
>>> 

"""