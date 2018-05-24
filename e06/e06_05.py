# 復習課題 6-5
# 'name': 'Hydrogen', 'symbol': 'H', 'number': 1というキー/値ペアを持つ辞書を作ろう。
# 次に、この辞書を使ってElementクラスのhydrogenオブジェクトを作ろう。

# クラスElementを作成
class Element():
    #  初期化メソッドを定義
    def __init__(self, name, symbol, number):
        self.name = name # 属性の追加
        self.symbol = symbol # 属性の追加
        self.number = number # 属性の追加

# 辞書を作成
dict_elem = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

# 辞書の値をそれぞれクラスの引数として与え、オブジェクトを作成
hydrogen = Element(dict_elem['name'], dict_elem['symbol'], dict_elem['number'])

# 値の確認
print(hydrogen.name)
# 値の確認
print(hydrogen.symbol)
# 値の確認
print(hydrogen.number)