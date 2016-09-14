import os
import json
import MySQLdb
path='data.txt'

def db_check():
    
    db = MySQLdb.connect(host='localhost', db='sandbox_signatures', user='root', passwd='polydata', port=3306,
                         charset='utf8')
    cursor = db.cursor()
    select_sql='select name from signatures'
    cursor.execute(select_sql)  
    results=cursor.fetchall()
    for result in results:
        select_sql='select file from signatures where name="%s"'%result
        cursor.execute(select_sql)
        result1=cursor.fetchall()
        if not result1[0][0]:
            a=open(path).readlines()
            for line in a:
                
                m=line.split('    ')
                print result,m[1]
                if result[0] in m[1]:
                    print result[0],m[0]
                    update_sql='update signatures set file="%s" where name="%s"'% (m[0],result[0])
                    cursor.execute(update_sql)  
                    break
                        
                
    db.commit()    
    cursor.close()
    db.close()
   
if __name__=="__main__":
    db_check()
