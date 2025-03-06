# Exercise to open edit and save a text file

import os.path 

parent_dir = 'D:\\Claudio\Documents\\Programming\\test_files\\'
file_toRead = 'text_file.txt'
file_toWrite = 'text_file_clened.txt'
path_toRead = os.path.join(parent_dir,file_toRead)
path_toWrite = os.path.join(parent_dir,file_toWrite)

if os.path.exists(path_toRead):
    with open(path_toRead, newline='') as tmp_file_toRead:
        file_content = tmp_file_toRead.readlines()
        clean_text = [line for line in file_content if line.strip()]
        for each in clean_text:
            if len(each) > 20:
                split_line = each.split('.')
                clean_text.extend(split_line)
else:
    print(f"Error: File '{path_toRead}' does not exist.")

new_string = ''
print(clean_text)

'''
with open(path_toWrite, 'w', newline='') as tmp_file_toWrite:
    tmp_file_toWrite.write(new_string.join(clean_text))
    print(f'The file has been written in: {path_toWrite}')


line_counter = 0
for each in file_content:
    line_counter += 1
print(line_counter)'''

