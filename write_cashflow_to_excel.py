
"""
For writing swap cashflows to excel for investigation purposes

@author: ShasaFoster
"""


import xlsxwriter

def write_trade(path,cashflow_schedules,DV01):

    def write_leg(df, sheet_row):
        df = df.dropna()
        
        # Write the header of the cashflow dataframe
        col_names = df.columns.values
        for c,v in enumerate(col_names):
            worksheet.write(sheet_row,c,v,header_format)
        
        # Write the cashflow dataframe values
        arr = df.values
        
        nb_rows = len(arr)
        nb_cols = len(arr[0])
        map_colnb_to_colname = {i : col_name for i,col_name in enumerate(col_names)}
        for r in range(nb_rows):
            sheet_row +=  1
            for c in range(nb_cols):
                worksheet.write(sheet_row,c,arr[r,c],format_dict[map_colnb_to_colname[c]])
                
        # Write formula to sum the discounted cashflows
        sheet_row += 1
        col_letter = str(xlsxwriter.utility.xl_col_to_name(nb_cols-1))
        worksheet.write(sheet_row,nb_cols-1,'=SUM(' + col_letter + str(sheet_row-nb_rows+1) + ':' + col_letter + str(sheet_row) + ')',sum_format)
        cell = str(xlsxwriter.utility.xl_col_to_name(nb_cols-1)) + str(sheet_row+1)
        sheet_row += 2
        
        return sheet_row, cell
    
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    
    date_format = workbook.add_format({'num_format': 'd-mmm-yyyy;;'})
    number_format = workbook.add_format({'num_format': '#,##0;(#,##0)'})
    fraction_format = workbook.add_format({'num_format': '0.0000_-'})
    percentage_format = workbook.add_format({'num_format': '0.0000%'})
    general_format = workbook.add_format({'num_format': 'General'})
    header_format = workbook.add_format()
    header_format.set_bottom()
    sum_format = workbook.add_format({'num_format': '#,##0;(#,##0)'})
    sum_format.set_top()
    sum_format.set_bottom()
    
    format_dict = {'Fixing Date' : date_format,
                   'Start Date' : date_format,
                   'End Date' : date_format,
                   'Payment Date' : date_format,
                   'Days' : general_format,
                   'Year Fraction' : fraction_format,
                   'Notional' : number_format,
                   'Fixed Rate' : percentage_format,
                   'Index Rate' : percentage_format,
                   'Spread' : percentage_format,
                   'Floating Rate' : percentage_format,
                   'Cash Flow' : number_format,
                   'Discount Factor' : fraction_format,
                   'Cash Flow PV' : number_format}
        
    sheet_row = 0
    cells = []
    for i,leg in enumerate(cashflow_schedules):
        print(i)
        sheet_row,cell = write_leg(cashflow_schedules[i], sheet_row)
        cells.append(cell)
        
    worksheet.write(sheet_row,1,"MV",header_format)
    worksheet.write(sheet_row,2,"DV01",header_format)
    sheet_row += 1
    for i,cell in enumerate(cells):
        worksheet.write(sheet_row,0,"LEG"+str(i+1),number_format)
        worksheet.write(sheet_row,1,"="+cell,number_format)
        worksheet.write(sheet_row,2,DV01[i],number_format)
        sheet_row += 1
        
    worksheet.write(sheet_row,0,"Net")
    worksheet.write(sheet_row,1,"=SUM(" + "B" + str(sheet_row - len(cells) + 1) + ":B" + str(sheet_row) + ')',sum_format)
    worksheet.write(sheet_row,2,"=SUM(" + "C" + str(sheet_row - len(cells) + 1) + ":C" + str(sheet_row) + ')',sum_format)
    
    workbook.close()
    
    
#%%
