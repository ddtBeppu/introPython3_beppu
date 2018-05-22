# 復習課題 5-4
# hours関数をinfoという名前でインポートし、呼び出そう。

# 解答
# コメントは、後からエディタにて追加しました。

"""

>>> from zoo import hours as info  ###  hours関数をinfoという名前でインポート
>>> info()  ### 関数の呼び出し
Open 9-5 daily
>>> 


"""

### zoo.pyの中身
###  関数hoursを定義
def hours():
    ### 開園時間の表示
    print('Open 9-5 daily')