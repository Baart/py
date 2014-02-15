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

mydbfile = "_braincraftsqlite3file.db"
where="D:/Divx"
what = "test"

conn = sqlite3.connect(mydbfile)
c = conn.cursor()

results = dbfolder(where)

c.executemany('INSERT INTO poc1_file VALUES (?,?,?)', results)
conn.commit()
    
c.execute('SELECT * FROM poc1_file')
results = c.fetchall()

print("entries:", len(results))

for entry in results:
    print (entry)

conn.close()






