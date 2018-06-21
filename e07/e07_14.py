# 復習課題 7-14
# GIFファイルの幅（単位ピクセル）は、バイトオフセット6からの16ビットビッグエンディアンの整数で、高さはオフセット8からの
# 同じサイズの整数になっている。
# gifのこれらの値を抽出して表示しよう。どちらも1になっているか。

import binascii
import struct

# 文字列を定義
hex_string = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
# bytes変数に変換
gif = binascii.unhexlify(hex_string)
# 結果表示
print('gif: ', gif)

#print('width: ', gif[7:9])
#print('height: ', gif[10:12])

# バイトの取り出し
width, height = struct.unpack('>2H', gif[6:10])
print('width: ', width, ', heidht: ', height)

# 実行結果
# エンディアン指定子をビッグエンディアンに指定して表示すると、幅、および高さはいずれも1になっている。
#NaotonoMacBook-puro:e07 naotobeppu$ python e07_14.py 
#gif:  b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
#width:  256 , heidht:  256