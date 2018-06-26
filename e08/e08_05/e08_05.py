# 復習課題 8-5
# 次の行を使ってbooks.csvというCSVファイルを作ろう。
"""
title, author, year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,china Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""

import csv

# 次の行に追加する内容
books = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],
    ['Perdido Street Station', 'china Mieville', '2000'],
    ['Thud!', 'Terry Pratchett', '2005'],
    ['The Spellman Files', 'Lisa Lutz', '2007'],
    ['Small Gods', 'Terry Pratchett', '1992'],
]

with open('books', 'wt') as fout2:
    # 書き込む対象を設定
    csvout = csv.writer(fout2)
    # e08_03で作成した内容の次の行から今回のbooksの内容を表示
    csvout.writerows(books)
