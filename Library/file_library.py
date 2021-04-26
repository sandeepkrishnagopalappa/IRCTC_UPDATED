""" importing data from Excel file """
import xlrd

class XlData:
    """ class to read the excel data from excel file with xlrd module """

    def read_locators(self,file_name,sheet_name):
        """ methods where we pass the file_name and the sheet_name to read """

        with xlrd.open_workbook(file_name) as workbook:
            worksheet=workbook.sheet_by_name(sheet_name)
            rows=worksheet.get_rows()
            next(rows)
            read_line={row[0].value:(row[1].value,row[2].value) for row in rows}
            return read_line, read_line.keys()
