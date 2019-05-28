import os
import re
import json

# 取指定文件
for parent, dirnames, filenames in os.walk('./'):
    # for dirname in dirnames:
    #     print('@' * 50)
    #     print('[DIR]', dirname)
    #     print('@' * 50)

    filesList = []
    for filename in filenames:
        # print('-' * 50)
        # print('[FILE]', filename)
        # print('-' * 50)
        # break
        if re.match('.*\.java\.json', filename):
            filesList.append(filename)
        # print('^^' * 50)
        # print([i for i in filesList])
        # print('^^' * 50)
        for file_name in filesList:
            file_path = os.path.join(parent,filename)

            # srcPath = filename
            # file_path = os.path.abspath(srcPath)
            # print(file_path)
            with open(file_path, 'r') as load_f:
                load_json = json.load(load_f)
                a = len(load_json)
                # print('db '*30)
                for i in range(a):
                    print("range:", load_json[i]["range"])
                    print("Description:", load_json[i]["description"])
                    print(">")

                print('- '*30)

# 	filesList=[]
# 	for i in filenames:
# 	    if (re.match('.*.java.json', i)):  # 这里是获取.java.json文件
# 	        filesList.append(i)
# 	print(filesList)
# 	print('-'*50)

# # print(filesList)
# 	for file_path in filesList:
# 		# file_path = "./DiffExecutorConfigurationSupport.java.json"
# 		print(">>>>"*10+file_path+"<<<<"*10)
# 		with open(file_path,'r') as load_f:
# 		    load_json = json.load(load_f)
# 		    # print(load_json)

# 		print('-'*50)
# 		# print(load_json)
# 		# print(len(load_json))
# 		for i in range(5):
# 			# print(i)
# 			print(load_json[i]["description"])
# 			# print(type(load_json[i]))
# 			print('-'*50)


# # 第一种方法获取指定文件
# for parent, dirnames, filenames in os.walk('./'):
#     for dirname in dirnames:
#         print('[DIR]', dirname)
#     for filename in filenames:
#         print('[FILE]', filename)
#     break

# filesList = []
# for i in filenames:
#     if (re.match('.*.java.json', i)):  # 这里是获取.log文件
#         filesList.append(i)
# print(filesList)
# print('-'*50)

# # 第二种方法获取指定文件
# files = os.listdir(os.getcwd())  # os.getcwd() 获取当前文件的路径 
# print(files)
# print('-'*50)

# filesList = []
# for i in files:
#     if (re.match('.*.java.json', i)):  # 这里是获取.java.json文件
#         filesList.append(i)
# print(filesList)
