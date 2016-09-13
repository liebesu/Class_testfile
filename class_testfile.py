import os
import MySQLdb
file_path=''
def get_path():
    for file in os.listdir(file_path):
        whole_path=os.path.normcase(os.path.join(file_path,file))
        
def clamscan(file):
    fr=os.popen('clamscan '+file)
    clr=fr.read()
    
def jsscan(file):
    pass
def md5scan(file):
    pass
def yarascan():
    pass
def shellscan():
    pass
def sandboxscan():
    pass
def db_insert():
    pass
if __name__=="__main__":
    clamscan