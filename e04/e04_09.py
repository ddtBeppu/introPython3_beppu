# 復習課題 4-9
# range(10)から奇数を返すget_odd()というジェネレータ関数を定義しよう。
# また、forループを使って、返された3番目の値を見つけて表示しよう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。


"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

###  ジェネレータ関数get_oddを作成
>>> def get_odd(first=0, last=10, step=1):
        ### 開始値をコピーし、インクリメント
...     num = first
        ### 第2引数の値を終了値としてループ
...     while num in range(last):   
                ### 奇数の場合
...             if num % 2 == 1:
                        ###  値を返却
...                     yield num
                ### ステップを進める
...             num += step
... 

###  ループを回す初期値を設定
>>> i = 0
### ジェネレータ関数で生成される奇数の数だけループ
>>> for x in get_odd():
        ### 3番目の値である時
...     if i == 2:
                ### 値を表示
...             print(x)
        ### 値を加算して処理を進める
...     i += 1
... 
### 実行結果
5   ### 生成された値は 1, 3, 5, 7, 9であり、3番目の値が表示されたことを確認
>>> 

"""