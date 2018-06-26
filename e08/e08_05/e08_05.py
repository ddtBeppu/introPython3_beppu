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

books = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],
    ['Perdido Street Station', 'china Mieville', '2000'],
    ['Thud!', 'Terry Pratchett', '2005'],
    ['The Spellman Files', 'Lisa Lutz', '2007'],
    ['Small Gods', 'Terry Pratchett', '1992'],
]

with open('../e08_03/books', 'rwt') as fout:
    cout = csv.DictWriter(fout, books)
