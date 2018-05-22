# 復習課題 4-10
# 関数が呼び出された時に'start'、終了した時に'end'と表示するtestというデコレータを定義しよう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
### デコレータtestを定義
>>> def test(func):
        ### 関数new_funcを定義
...     def new_func(*args, **kwargs):
                ### 関数が呼ばれた時、以下を表示
...             print('start')
                ### 関数の実行結果を取得
...             result = func(*args, **kwargs)
                ### 実行結果の値を表示
...             print(result)
                ### 関数が終了したので、以下を表示
...             print('end')
                ### 値を返して終了
...             return result
...     return new_func
... 
###  デコレータを使用する
>>> @test
### 足し算を行う関数を定義
... def add_ints(a,b):
        ### 加算結果を返す
...     return a+b
... 
### デコレートした関数を実行
>>> add_ints(3,5)
start   # 関数が呼ばれた
8       # 関数が実行された
end     # 関数が終了
8       # 関数が値を返却
>>> 


"""