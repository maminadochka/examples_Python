import openpyxl
import csv


with open("users.csv", "r") as us_file:
     csv_data_list = list(csv.reader(us_file))

# print(csv_data_list)

wb = openpyxl.Workbook()
sheet = wb.active

i = 1
for user_data in csv_data_list:
    if user_data:
        print(user_data)
        for col, cell in enumerate(user_data):
            data_cell = sheet.cell(row=col+1, column=i)
            data_cell.value = cell
        i += 1

sheet.delete_rows(3, 1)
wb.save("users.xlsx")
