# 復習課題 4-11
# OopsExceptionという例外を定義しよう。次に、何が起きたかを知らせるためにこの例外を生成するコードと、この例外をキャッチして
# 'Caught an Oops'と表示するコードを書こう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""
###  例外を定義
class OopsException(Exception):
        ### 処理内容は定義しない
...     pass
... 
### 例外を生成することにより例外をキャッチするようにする
>>> try:
        ###  例外を生成
...     raise OopsException('Caught an Oops')
###  例外をキャッチした時、
... except OopsException as exc:
        ###  例外をキャッチしたことを表すテキストを表示する
...     print(exc)
... 
Caught an Oops
>>> 

"""