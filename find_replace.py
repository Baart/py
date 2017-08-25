import os



def find_replace(filepath, find_what, replace_with):
    spare = filepath + '2'
    f1 = open(filepath, 'r')
    f2 = open(spare, 'w')
    for line in f1:
        f2.write(line.replace(find_what, replace_with))
    f1.close()
    f2.close()
    os.remove(filepath)
    os.rename(spare, filepath)




find_what = '"enabled": false'
replace_with = '"enabled": true'

find_replace('J:/git/ifj/runtime-resources/target/classes/elements.json', find_what, replace_with)
find_replace('J:/git/ifj/runtime-resources/src/main/resources/elements.json', find_what, replace_with)