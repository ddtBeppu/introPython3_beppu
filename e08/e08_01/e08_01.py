# 復習課題 8-1
# test1という変数に、'This is a test of the emergency text system'という文字列を代入し、
# test.txtというファイルにtest1の内容を書き込もう。

# 文字列を変数に格納
test1 = 'This is a test of the emergency text system'

# ファイルオープン
fout = open('test.txt', 'wt')
# 文字列をテキストファイルに書き込む
print(test1, file=fout)

# ファイルクローズ
fout.close()