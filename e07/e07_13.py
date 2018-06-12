# 復習課題 7-13
# gifのバイトは、１ピクセルの透明なGIFファイルを定義する。GIFは、広く使われているグラフィックファイル形式のひとつだ。
# 有効なGIFファイルの先頭は、'GIF89a'という文字列になっている。gifはこのパターンにマッチするか。

# '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'

import binascii

# 文字列を定義
hex_string = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
# bytes変数に変換
gif = binascii.unhexlify(hex_string)
# 結果表示
print(gif)

# 実行結果
# 先頭が'GIF89a'であり、マッチしていることが確認できる。
"""
NaotonoMacBook-puro:e07 naotobeppu$ python e07_12.py 
b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,
\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
"""