import os

version = '6.4.1.8'
extension_from = 'doc'
extension_to = 'docx'

wait_for_open = 5  # время ожидания открытия
wait_for_press = 0.5  # время ожидания открытия

list_file_names_doc_from_compare = [
    '_4__.docx'
]



custom_path_to_document_to = f'd:/ProjectsAndVM/data_db/results/{version}_xmllint_{extension_to}_{extension_from}/'
# custom_path_to_document_to = f'D:/documents/results/{version}_xmllint_{extension_to}_{extension_from}/'
# custom_path_to_document_to = f'd:/ProjectsAndVM/data_db/results/{version}_xmllint_{extension_from}_{extension_to}/'
custom_path_to_document_from = f'd:/ProjectsAndVM/data_db/files/{extension_from}/'
# custom_path_to_document_from = f'D:/documents/files/{extension_from}/'

ms_office = 'C:/Program Files (x86)/Microsoft Office/root/Office16/'
word = 'WINWORD.EXE'
power_point = 'POWERPNT.EXE'


path_to_project = os.getcwd()
path_to_data = path_to_project + '/data/'
path_to_compare_files = path_to_project + '/data/files/'
path_to_result = path_to_project + '/data/result/'
path_to_tmp = path_to_project + '/data/tmp/'
path_to_tmpimg_after_conversion = path_to_project + '/data/tmp/after/'
path_to_tmpimg_befor_conversion = path_to_project + '/data/tmp/before/'
path_to_errors_file = path_to_project + '/data/errors/'
path_to_not_tested_file = path_to_project + '/data/not_tested/'
path_to_temp_in_test = path_to_project + '/data/tmp/in_test/'
path_to_folder_for_test = path_to_project + f'/data/{version}_{extension_from}_{extension_to}/'

# папки исходных30 файлов должны называться как расширения,
# например если расширение из котрого мы конвертируем doc,
# то и папка где лежат эти файлы должна называться doc
