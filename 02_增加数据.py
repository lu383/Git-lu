import pymysql

# 链接数据库
con = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',db='sxt')
# 获取一个和数据库交互的工具cursor
coursor = con.cursor()
# 编写SQL
sql ="INSERT INTO t_user VALUES (0,'貂蝉',20,'女');"
# 执行SQL
coursor.execute(sql)
# 关闭cursor
coursor.close()
# 关闭链接
con.close()