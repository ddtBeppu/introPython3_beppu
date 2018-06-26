# 復習課題 8-2
# test.txtファイルを開き、その内容をtest2変数に読み出そう。test1とtest2は同じになっているだろうか。

fout = open('../e08_01/test.txt', 'r')
test2 = fout.readline()
print(test2)

fout.close()

# 実行結果
"""
NaotonoMacBook-puro:e08_02 naotobeppu$ python e08_02.py 
This is a test of the emergency text system
"""