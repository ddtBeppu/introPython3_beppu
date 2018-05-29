# 復習課題 6-8
# Elementを書き換え、name, symbol, number属性を非公開にしよう。そして、それぞれについて値を返すゲッターを定義しよう。

# クラスElementを作成
class Element():
    #  初期化メソッドを定義
    def __init__(self):
        self.__name = "Hydrogen" # 属性の追加
        self.__symbol = "H" # 属性の追加
        self.__number = 1 # 属性の追加

    # ゲッター
    @property
    # 非公開のname属性を返す
    def name(self):
        # __name属性を返す
        return self.__name

    # ゲッター
    @property
    # 非公開のsymbol属性を返す
    def symbol(self):
        # __symbol属性を返す
        return self.__symbol

    # ゲッター
    @property
    # 非公開のnumber属性を返す
    def number(self):
        # __number属性を返す
        return self.__number

# オブジェクトの作成
hydrogen =  Element()

# それぞれの属性値を表示
# name
print(hydrogen.name)
# symbol
print(hydrogen.symbol)
# number
print(hydrogen.number)