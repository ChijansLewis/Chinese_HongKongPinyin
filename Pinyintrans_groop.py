import csv
from Pinyintrans_single import trans

file=open("HongKongPinyin.txt","r",encoding='utf-8')

lines=file.readlines()

for line in lines:
    for char in line:
        trans(char)

file.close()