import string

a=""


phrase="lmu ynnjw ml rfc spj"
#"aaabbb".translate(str.maketrans("a", "e"))
#phrase = "map.html"
#phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for letter in zip(phrase):
    inc = chr(ord(letter[0]) + 2)
    #print (inc)
    if(inc == "{"):
        inc = "a"
    if(inc == "\""):
        inc = " "
    if(inc == "|"):
        inc = "b"
    if(inc == ")"):
        inc = "'"
    if(inc == "0"):
        inc = "."
    a+=inc
print(a)
    
