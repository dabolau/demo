import pickle

# 文件读操作
# 1、开，文件变量=open('文件路径文件名','wb')
# 2、取，pickle.dump(待写入的变量，文件变量)
# 3、关，文件变量.close()
load_file = open('data.dat', 'rb')
load_game_data = pickle.load(load_file)
load_file.close()

# 读取检查
print(load_game_data)
