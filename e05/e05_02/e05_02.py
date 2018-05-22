# 復習課題 5-2
# 対話型インタープリタの中でzooモジュールをmenegerieという名前でインポートし、そのhours()関数を呼び出そう。


# 解答
# コメントは、後からエディタにて追加しました。

"""

>>> import zoo as menegerie  ### menegerieという名前でzooモジュールをインポート
>>> menegerie.hours()  ### 関数hours()を呼び出す
Open 9-5 daily

"""


### zoo.pyの中身
###  関数hoursを定義
def hours():
    ### 開園時間の表示
    print('Open 9-5 daily')