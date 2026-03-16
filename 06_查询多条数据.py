import pymysql

# 获取数据,默认是返回一条数据。如果传递了数字就是指定的条数。

def query_maby():
    # 链接数据库
    con = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',db='sxt')
    # 获取一个和数据库交互的工具cursor
    coursor = con.cursor()

    # 查询数据SQL
    sql ="SELECT id,uname,age,sex FROM t_user;"
        
    # 执行SQL
    coursor.execute(sql)

    # 获取数据,默认是返回一条数据。如果传递了数字就是指定的条数。
    rs = coursor.fetchmany(4)
    print(rs)

    # 关闭cursor
    coursor.close()

    # 关闭链接
    con.close()

if __name__ == "__main__":
    query_maby()