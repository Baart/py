import os
import sqlite3

import datetime


def dbfolder(where):
    #print("findfile on", where)
    results = []
    if(not os.path.isdir(where)):
        raise Exception("dbfolder work only with folder.")
    content = []
    try:
        content = os.listdir(where)
    except:
        return content
    for elem in content:
        elempath = where+"/"+elem
        if(os.path.isfile(elempath)): # file
            results.append((os.path.basename(elempath),
                            os.path.getsize(elempath),
                            os.path.dirname(elempath),
                            ))
            
        elif(os.path.isdir(elempath)): # folder
            results.extend(dbfolder(elempath))
        else:
            print("not a file nor a folder : ", elempath)
    return results

withPurge = False
mydbfile = "testfile.db"
where="J:/bam/py"
what = "test"


if(withPurge):
    beforePurge = datetime.datetime.now()
    try:
        os.remove(mydbfile)
    except:
        pass
    print("indexing", where)
    conn = sqlite3.connect(mydbfile)
    c = conn.cursor()
    c.execute('''CREATE TABLE files(basename text, size real, dirname text)''')
    c.executemany('INSERT INTO files VALUES (?,?,?)', dbfolder(where))
    conn.commit()
    conn.close()
    print("indexing took:",(datetime.datetime.now() - beforePurge))
    



conn = sqlite3.connect(mydbfile)
c = conn.cursor()

print("search", what, "in", where)
    
beforeSearch = datetime.datetime.now()
t = ("%"+what+"%",) # % is a joker
c.execute('SELECT * FROM files WHERE basename like ?', t)
results = c.fetchall()

print("search took:",(datetime.datetime.now() - beforeSearch))


print("entries:", len(results))

#for entry in results:
#    print (entry)




conn.close()



