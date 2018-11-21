import pymysql
def inserts(list):
        db=pymysql.connect('localhost','root','root','django')
        cur=db.cursor()
        sql='insert into blog_blogpost(title,content) values '
        for i in range(10):
            obj=list[i]
            ip=obj['ip']
            port=obj['port']
            sql+='("'+ip+'","'+port+'"),'
            print('sql%s'%sql[:(len(sql)-1)])
            cur.execute(sql[:(len(sql)-1)])
            db.Close()
    