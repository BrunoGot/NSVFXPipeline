import os
import sys
import shutil

from PySide2.QtWidgets import QMainWindow, QWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, \
    QPushButton


class FileSorterUI(QMainWindow):
    def __init__(self):
        super(FileSorterUI, self).__init__()
        self.confirmation_window = QWidget()

        vertical_main_layout = QVBoxLayout()
        # browser layout
        browser_line_layout = QHBoxLayout()
        browser_line_layout.addWidget(QLabel("folder to sort : "))
        self.path_browser = QLineEdit()
        browser_line_layout.addWidget(self.path_browser)
        vertical_main_layout.addLayout(browser_line_layout)
        # folder name layout
        # folder_line_layout = QHBoxLayout()
        # folder_line_layout.addWidget(QLabel("folder name : "))
        # self.folder_name = QLineEdit()
        # folder_line_layout.addWidget(self.folder_name)
        # vertical_main_layout.addLayout(folder_line_layout)

        execute_btn = QPushButton("Sort")
        execute_btn.clicked.connect(self.execute_btn)
        vertical_main_layout.addWidget(execute_btn)
        main_widget = QWidget()
        main_widget.setLayout(vertical_main_layout)
        self.setCentralWidget(main_widget)
        self.show()

    def execute_btn(self):
        self.src_folder_path = self.path_browser.text()
        self.sort_file_at_path(self.src_folder_path)

    def sort_file_at_path(self, path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        self.sorted_list = sort_files(files)
        dic_view = display_dic(self.sorted_list)
        self.display_confirmation(dic_view)

    def display_confirmation(self, result_message):
        layout = QVBoxLayout()
        message = QLabel("list of folders that gonna be created with their files : \n" \
                        "\n 'folder  =>  files,...'\n\n "
                        +result_message
                         +"\nDo you want to continue ?")

        layout_butons = QHBoxLayout()
        confirm_btn = QPushButton("Create Folders")
        confirm_btn.clicked.connect(self.execute_process)
        cancel_btn = QPushButton("Cancel Operation")
        cancel_btn.clicked.connect(self.close_confirmation)
        layout_butons.addWidget(confirm_btn)
        layout_butons.addWidget(cancel_btn)

        layout.addWidget(message)
        layout.addLayout(layout_butons)


        self.confirmation_window.setLayout(layout)
        self.confirmation_window.show()

    def close_confirmation(self):
        self.confirmation_window.hide()

    def execute_process(self):
        sort_file_system(self.src_folder_path, self.sorted_list)


def sort_file_system(folder_path, files_group):
    """create a folder, move the files by group into a new folder by group """
    for k,v in files_group.items():
        dst_folder = os.path.join(folder_path, k)
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        for f in v:
            base_file_path = os.path.join(folder_path, f)
            destination_file_path = os.path.join(dst_folder,f)
            shutil.move(base_file_path, destination_file_path)


def filter_folder_separator(list_name, separator):
    """
    return the list of name with the first element of the separtion extracted
    ex : list_name = ['ABC_01', 'ABC_02', 'ABB_03'] separator = '_', result  = [ABC,ABB]
    :param separator:
    :return: list of names with the first part of the separation
    """

    new_list = []
    for n in list_name:
        filtered_name = n.split(separator)[0]
        if filtered_name not in new_list:
            new_list.append(filtered_name)
    return new_list


def sort_files(files):
    """

    :param files: list of folder names
    :return:
    """
    filtered_list = filter_folder_separator(files, "_")
    filtered_list = filter_folder_separator(filtered_list, "-")
    sorted_folder = {}  # {folder_name,[files]}
    singles_files = [] #array that gonna get all the isolated files (files with no common prefix)
    # first pass order dictionary by group on common names
    #for each files in the folder
    for cur_f in filtered_list:
        prefix_found = False
        #compare each files with cur_f
        for f in files:
            if cur_f is not f:
                common_pref = os.path.commonprefix([cur_f, f])
                if common_pref:
                    prefix_found = True
                    if not sorted_folder.get(common_pref):
                        sorted_folder[common_pref] = [f]
                    elif f not in sorted_folder[common_pref]:
                        sorted_folder[common_pref].append(f)
        if not prefix_found:
            singles_files.append(cur_f)

    # second pass : remove duplication by subtracting the biggest group name from all the other groups
    # 1 sort the keys by length
    # 2 for each group remove the duplication values
    sorted_keys = sorted(sorted_folder.keys(), key=len, reverse=True)
    for k in sorted_keys:
        for v in sorted_folder[k]:
            for folder in sorted_folder.keys():
                if folder is not k and v in sorted_folder[folder]:
                    sorted_folder[folder].remove(v)

    # 3rd pass : put all the single file in a "other" folder
    for k,v in sorted_folder.items():
        if len(v) == 1:
            singles_files.append(v[0])

    # 4rd pass : remove empty dic
    filtered_sorted_folder = {k:v for k,v in sorted_folder.items() if len(v)>1}
    filtered_sorted_folder["Other"] = singles_files

    return filtered_sorted_folder


def display_dic(dic):
    """
    display dictionary values
    :param dic: dic {key, val} to display
    """
    message = ""
    for i, j in dic.items():
        message += f"{i}  ===>  {', '.join(j)}\n"
    return message

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FileSorterUI()
    sys.exit(app.exec_())

    ###tests###
    # list = ["ab_02", "ab01", "ab_01", "ec_02", "ecr01", "abc_01", "abc_02", "ac_04", "ac_01", "ac_03","yh-05","yhf-07"]
    # list = os.listdir(r"C:\Users\Natspir\Downloads\swisstransfer_f5cb5536-95e0-461b-be0b-e95cdc3f0f4b")
    # sorted_list = sort_files(list)
    # display_dic(sorted_list)

