from datetime import datetime

import pytest
from openpyxl import load_workbook

from pages.login_page import LoginPage

# excel file location
EXCEL_FILE =  "test_data/login_test_data.xlsx"
# name of the tester
TESTER_NAME = "Dharshini"
# Read login data from excel
workbook = load_workbook(EXCEL_FILE)
sheet = workbook.active
# store the login data from excel

test_data = []
for row in sheet.iter_rows(min_row=2,values_only=True):
    test_id, username, password, date, test_time, tester, result =  row
    test_data.append((test_id, username, password))

@pytest.mark.parametrize("test_id, username, password", test_data)
def test_login(driver, test_id, username, password):
    # create login object using browser driver
    login_page = LoginPage(driver)
# open orangehrm login page
    driver.get(login_page.URL)
    # perform login using username and password from excel
    login_page.login(username, password)
    # check whether login was successful
    login_successful = login_page.is_login_successful()
    # get current date and time
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    if login_successful:
        test_result = "Pass"
    else:
        test_result = "Fail"
    # remember the row
    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row, 1).value == test_id:
            excel_row = row
            break
    # write the date inside the coloumn D in row 1
    sheet.cell(excel_row, 4).value = current_date

    # This writes the Time of Test into colum E.
    sheet.cell(excel_row, 5).value = current_time

    # write name in column F
    sheet.cell(excel_row, 6).value = TESTER_NAME

    # write result into column G
    sheet.cell(excel_row, 7).value = test_result
    # to save the excel file
    workbook.save(EXCEL_FILE)
    print("Test ID:", test_id)

    print("Login successful:", login_successful)