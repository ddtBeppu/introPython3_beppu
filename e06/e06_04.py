# 復習課題 6-4
# name, symbol, numberというインスタンス属性を持つElementというクラスを作り、
# 'Hydrogen', 'H', 1という値を持つこのクラスのオブジェクトを作ろう。

# クラスElementを作成
class Element():
    #  初期化メソッドを定義
    def __init__(self, name, symbol, number):
        self.name = name # 属性の追加
        self.symbol = symbol # 属性の追加
        self.number = number # 属性の追加

# オブジェクトの作成
element = Element('Hydrogen', 'H', 1)