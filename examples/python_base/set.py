char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
char2_list = ['a', 'e', 'i']
sentence = 'Welcome Back to This Tutorail'

# 用set找出列表中不同的值
print(type(char_list))
print(type(set(char_list)))
print(set(char_list))
print(set(sentence))

unique_char = set(char_list)
# 添加进入set中
unique_char.add('a')
# 清除所有数据
# unique_char.clear()
# 移除一个数据，如果没有会报错
# print(unique_char.remove('a'))
# 移除一个数据，如果没有不会报错
# print(unique_char.discard('y'))
print(unique_char)

# 用unique_char与char2_list对比找出不重合的值
print(unique_char.difference(char2_list))
# 用unique_char与char2_list对比找出重合的值
print(unique_char.intersection(char2_list))
