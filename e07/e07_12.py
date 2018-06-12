# 復習課題 7-12
# unhexlifyを使ってこの１６進文字列をgifというbytes変数に変換しよう。

# '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'

import binascii

# 文字列を定義
hex_string = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
# bytes変数に変換
gif = binascii.unhexlify(hex_string)
# 結果表示
print(gif)