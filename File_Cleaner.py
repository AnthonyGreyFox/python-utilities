import openpyxl
import easygui
import glob


def nav():
    path = easygui.diropenbox()
    return path


def file_cleaner():
    filenames = glob.glob(nav() + "\*.xlsx")
    for file in filenames:
        check_cell = openpyxl.load_workbook(file)["Data"]["H2"]
        if check_cell.value != 'Doc Type':
            print(f"{file}")


if __name__ == '__main__':
    file_cleaner()
