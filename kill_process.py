import sys, os

def pkill(process_name):
    try:
        kill = os.system('tskill ' + process_name)
        print "killed"
    except Exception, e:
        print "not killed", e

#for x in range(10):
#    pkill('C:\\Python27\\python.exe')


def pkillall(process_name):
    try:
        kill = os.system('taskkill /im ' + process_name + ' /F')
        print "killed", kill
    except Exception, e:
        print "not killed", e


pkillall('python.exe')