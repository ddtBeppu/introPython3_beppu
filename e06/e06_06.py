# 復習課題 6-6
# Elementクラスのために、オブジェクトの属性（name, symbol, number）の値を表示するdump()というメソッドを定義しよう。
# この新しい定義からhydrogenオブジェクトを作り、dump()を使って属性を表示しよう。

# クラスElementを作成
class Element():
    #  初期化メソッドを定義
    def __init__(self, name, symbol, number):
        self.name = name # 属性の追加
        self.symbol = symbol # 属性の追加
        self.number = number # 属性の追加
    
    # 属性の値を表示するメソッド
    def dump(self):
        # 属性の表示
        print(self.name)
        # 属性の表示
        print(self.symbol)
        # 属性の表示
        print(self.number)


# オブジェクトの作成
hydrogen = Element('Hydrogen', 'H', 1)

# 属性を表示するメソッドの実行
hydrogen.dump()