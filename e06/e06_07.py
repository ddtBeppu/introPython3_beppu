# 復習課題 6-7
# print(hydrogen)を呼び出そう。次に、Elementの定義の中でdumpというメソッド名を__str__に変更し、
# 新しい定義のもとでhydrogenオブジェクトを作って、print(hydrogen)をもう一度呼び出そう。

# クラスElementを作成
class Element():
    #  初期化メソッドを定義
    def __init__(self, name, symbol, number):
        self.name = name # 属性の追加
        self.symbol = symbol # 属性の追加
        self.number = number # 属性の追加

    # 属性の値を表示するメソッド
    def __str__(self):
        # 属性の表示
        print(self.name)
        # 属性の表示
        print(self.symbol)
        # 属性の表示
        print(self.number)

# オブジェクトの作成
hydrogen = Element('Hydrogen', 'H', 1)
#print(hydrogen)
print(hydrogen)

# 実行結果
# print(hydrogen)：１回目
"""

NaotonoMacBook-puro:e06 naotobeppu$ python e06_07.py
<__main__.Element object at 0x10845c160>

"""

# Elementの定義の中でdumpというメソッド名を__str__に変更後に実行した結果
"""

NaotonoMacBook-puro:e06 naotobeppu$ python e06_07.py
Hydrogen
H
1
Traceback (most recent call last):
  File "e06_07.py", line 23, in <module>
    print(hydrogen)
TypeError: __str__ returned non-string (type NoneType)

"""
# → __str__()関数はstr型の返り値を持たねばならないことが分かった。