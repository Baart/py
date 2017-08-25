import os





def get_size(path):
    total_size=0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)

    total_size = total_size / 1024 / 1024
    print total_size, 'MB'
    return total_size





def get_filelist(path):
    for n in os.listdir(path):
        print "'" + n + "',"


path = '\\\\frtosyno01\\if\\dev-storage\\WF\\test-xsquare'
#get_size(path)

path = '\\\\frtosyno01\\if\\dev-storage\\integration-tests\\NAB_2015_checklegalizeAS10'
get_filelist(path)

