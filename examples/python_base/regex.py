import re

# 简单的python匹配
print('##############################')
pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'
print(pattern1 in string)
print(pattern2 in string)

# 正则表达式匹配
print('##############################')
print(re.search(pattern1, string))
print(re.search(pattern2, string))

# 匹配多种可能，使用[]
print('##############################')
ptn = 'r[au]n'  # 括号中的au代表可以匹配到ran或者匹配到run
print(re.search(ptn, 'dog runs to cat'))

# 匹配多种可能，使用[]，简单写法。
print('##############################')
print(re.search('r[A-Z]n', 'dog runs to cat'))
print(re.search('r[a-z]n', 'dog runs to cat'))
print(re.search('r[0-9]n', 'dog r2ns to cat'))
print(re.search('r[0-9a-z]n', 'dog runs to cat'))

# 特殊种类匹配，数字，\d表示数字，\D表示非数字。
print('##############################')
print(re.search('r\dn', 'run r4n'))
print(re.search('r\Dn', 'run r4n'))

# 特殊种类匹配，空白，\s表示空白，\D表示非空白，[\t\n\r\f\v]表示特殊的空白符号。
print('##############################')
print(re.search('r\sn', 'r\tn r4n'))
print(re.search('r\Sn', 'r\nn r4n'))

# 特殊种类匹配，所有字母数字和“_”，\w表示匹配[a-zA-Z0-9_]，\W表示匹配非[a-zA-Z0-9_]。
print('##############################')
print(re.search('r\wn', 'r\tn r4n'))
print(re.search('r\Wn', 'r\nn r4n'))

# 特殊种类匹配，空白字符，\b表示单词边界，\B表示非单词边界。
print('##############################')
print(re.search('\bruns\b', 'dog runs to cat'))
print(re.search('\B runs \B', 'dog   runs  to cat'))

# \表示特殊字符，.表示任意字符（除\n以外）。
print('##############################')
print(re.search('runs\\\\', 'runs\ to me'))
print(re.search('r.n', 'r[ns to me'))

# 匹配首尾，^表示首，$表示尾。
print('##############################')
print(re.search('^dog', 'dog runs to cat'))
print(re.search('cat$', 'dog runs to cat'))

# 是否，?表示是或否()?括号中的东西不管有没有都能匹配。
print('##############################')
print(re.search('Mon(day)?', 'Monday'))
print(re.search('Mon(day)?', 'Mon'))

# 多行匹配
print('##############################')
string = '''
dog runs to cat.
I run to dog.
'''
print(re.search('^I', string))
print(re.search('^I', string, flags=re.M))  # re.M表示多行匹配

# *表示匹配零或多次
print('##############################')
print(re.search('ab*', 'a'))
print(re.search('ab*', 'abbbbbb'))

# +表示匹配一或多次
print('##############################')
print(re.search('ab+', 'a'))
print(re.search('ab+', 'abbbbbb'))

# {n,m}表示匹配可选次数
print('##############################')
print(re.search('ab{2,10}', 'a'))
print(re.search('ab{2,10}', 'abbbbbb'))

# group表示分组，用数字寻找，每一个括号表示一个组
print('##############################')
match = re.search('(\d+),date:(.+)', 'id:021523,date:feb/12/2017')
print(match.group())
print(match.group(1))
print(match.group(2))

# group表示分组，用名字寻找,?P<id>其中id为自己定义的名字
print('##############################')
match = re.search('(?P<id>\d+),date:(?P<date>.+)',
                  'id:021523,date:feb/12/2017')
print(match.group())
print(match.group('id'))
print(match.group('date'))

# re.findall表示一次性找出所有的匹配
print('##############################')
print(re.findall('r[ua]n', 'run ran ren'))
print(re.findall('run|ran', 'run ran ren'))  # |表示或

# re.sub表示替换
print('##############################')
print(re.sub('r[au]n', 'catches', 'dog runs to cat'))

# re.split表示分割
print('##############################')
print(re.split('[,;\.]', 'dog.runs,to;cat'))

# complie表示编译
print('##############################')
rc = re.compile('r[ua]n')
print(rc.search('dog ran to cat'))
