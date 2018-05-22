# 復習課題 5-3
# 対話型インタープリタにそのまま残り、zooのhours()関数を直接インポートして呼び出そう。

# 解答
# コメントは、後からエディタにて追加しました。

"""

>>> from zoo import hours  ### hours()関数を直接インポート
>>> hours()  ### 関数の呼び出し
Open 9-5 daily
>>> 

"""


### zoo.pyの中身
###  関数hoursを定義
def hours():
    ### 開園時間の表示
    print('Open 9-5 daily')