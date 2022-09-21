from 单词复习随机版 import randomly_review as r
import xlrd
#将excel文件变成py中的文件
xlsx = xlrd.open_workbook('dictionary.xls')
english,chinese=[],[]
#通过索引将sheet提出
sheet = xlsx.sheet_by_index(0)
nrows = sheet.nrows#获取行数
for i in range(0,nrows-1):
    english.append(sheet.cell_value(i+1, 1))
    chinese.append(sheet.cell_value(i+1, 3))
dictionary = dict(zip(english,chinese))
r(dictionary)