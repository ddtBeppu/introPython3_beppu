# 復習課題 4-1
# 変数guess_meに7を代入しよう。次に、guess_meが7よりも小さければ、'too low', 7よりも大きければ'too high'を表示し、
# 7に等しければ'just right'と表示する条件テスト(if, else, elif)を書こう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。


"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> guess_me = 7   ###  変数guess_meに7を代入
>>> if guess_me < 7:   ###  guess_meが7よりも小さい場合
...     print('too low')
... elif guess_me > 7:  ###  guess_meが7よりも大きい場合
        ### 以下を表示
...     print('too high')
... else:               ###  guess_meが7と等しい場合
        ### 以下を表示
...     print('just right')
... 
just right   ###  guess_me == 7のため
>>> 


"""