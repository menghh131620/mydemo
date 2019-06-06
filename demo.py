import xlwt
new_workbook=xlwt.workbook()
worksheet=new_workbook.add_sheet('new_test')
worksheet.write(0,0,'test')
new_workbook('d:test.xls')
print('****8*****')
