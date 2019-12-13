import xlrd

def excel_read(doc_name):

    book = xlrd.open_workbook(doc_name)
    sheet1 = book.sheets()[0]
    '''
    nrows = sheet1.nrows
    print('表格总行数',nrows)
    ncols = sheet1.ncols
    print('表格总列数',ncols)
    '''
    row3_values = sheet1.row_values(2)
    print('第3行值',row3_values)
    col3_values = sheet1.col_values(2)
    print('第3列值',col3_values)
    cell_3_3 = sheet1.cell(2,2).value
    print('第3行第3列的单元格的值：',cell_3_3)

