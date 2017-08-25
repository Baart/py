#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

Allow to write a file slowly to fake a growing file

'''
from __future__ import print_function
from time import sleep
import os




source = '\\\\frtosyno01\\if\\dev-storage\\_bam_composite\\EVS-beautiful_Cameroon-111A.mxf'
output = '\\\\frtosyno01\\if\\dev-storage\\_bam_composite\\growing-file.mxf'


def main():
    while 1:
        slow_copy_file(source, output);
        decorated_wait(10)


def get_progress_bar(percentage, length):
    progress = percentage / 100. * float(length)
    chain = '['
    for x in xrange(1, length):
        if(progress < x):
            chain = chain + '-'
        else:
            chain = chain + 'X'
    chain = chain + ']'
    return chain

def slow_copy_file (filepathIn, filepathOut):

    input_size = os.path.getsize(filepathIn)


    chars = ['/', '|', '-', '\\', '-']
    charPos = 0
    print ("\n\n\n\n\n\n*** Start a new write ***")
    print (" from :" + filepathIn )
    print (" to   :" + filepathOut )
    chunk_size = 1
    output_size = 0
    with open(filepathIn, 'rb') as src:
        with open(filepathOut, 'wb') as dst:
            while 1:
                buf = src.read(chunk_size)
                output_size = output_size + chunk_size
                if not buf:
                    break;

                charPos = (charPos+1)%len(chars)
                percentage = int(float(output_size) / input_size * 100.)
                percentage_str = str(percentage).rjust(3, ' ') + '%'
                progress_bar = get_progress_bar(percentage, 100)
                print ("\r", chars[charPos], percentage_str , progress_bar, str(output_size/(1024*1024)) + 'MB / ' + str(input_size/(1024*1024)) + 'MB', end="")
                dst.write(buf)

    print ("\n*** File written *** ")


def decorated_wait (seconds):
    print ("\n*** Waiting " + str(seconds) + " seconds *** ")
    for x in xrange(seconds * 10,-1,-1):
        if (x%10 == 0):
            print (x/10, end="")
        else:
            print ('.', end="")
        sleep(0.1)
        pass


if __name__ == '__main__':
    main()