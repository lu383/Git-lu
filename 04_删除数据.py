import pymysql

def update_data(args):
    # 链接数据库
    con = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',db='sxt')
    # 获取一个和数据库交互的工具cursor
    coursor = con.cursor()

    # 删除SQL
    sql ="DELETE FROM t_user where id = %s;"
        
    # 执行SQL
    coursor.execute(sql,args)
    # 提交事务
    con.commit()

    # 关闭cursor
    coursor.close()

    # 关闭链接
    con.close()

if __name__ == "__main__":
    args = (4)
    update_data(args)