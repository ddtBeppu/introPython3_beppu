# 復習課題 10-9
# 生まれてから10,000日になるのはいつか（あるいはいつだったか）。

from datetime import date, timedelta

# 誕生日のdateオブジェクトを作成
birthday = date(1993, 2, 14)
print("誕生日: ", birthday)

some_days = timedelta(10000)
after = birthday + some_days

print("10,000日後: ", after)

# 実行結果
"""
NaotonoMacBook-puro:e10 naotobeppu$ python e10_09.py 
誕生日:  1993-02-14
10,000日後:  2020-07-02
"""