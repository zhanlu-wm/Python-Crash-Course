"""逐行读取文件内容"""

filename = 'pi_digits.txt'


with open(filename) as file_object:
    for line in file_object:
        # print(line)
        print(line.rstrip())