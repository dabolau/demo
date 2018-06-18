import pickle

game_data = {'position': 'N2 E3', 'pocket': ['key', 'knife'], 'money': 160}

# 文件写操作
# 1、开，文件变量=open('文件路径文件名','wb')
# 2、存，pickle.dump(待写入的变量，文件变量)
# 3、关，文件变量.close()
save_file = open('data.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()
