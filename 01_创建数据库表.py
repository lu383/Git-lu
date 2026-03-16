# pip install pymysql
# pip install mysql-connector-python -i https://mirrors.aliyun.com/pypi/simple/

import pymysql

# 链接数据库
con = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',db='sxt')
# 获取一个和数据库交互的工具cursor
coursor = con.cursor()
# 编写SQL
sql = '''
CREATE TABLE t_user(  
    id int PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    uname VARCHAR(32) not null,
    age int(11) not null,
    sex VARCHAR(5)
);
'''
# 执行SQL
coursor.execute(sql)
# 关闭cursor
coursor.close()
# 关闭链接
con.close()
