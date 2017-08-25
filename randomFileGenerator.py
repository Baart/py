




#for x in range(256):
#    with open('folder/' + str(x) + '.txt', 'w') as file:
#        file.write('x'*x);

for x in range(256):
    with open('\\\\frtosyno01\\if\\dev-storage\\test_'+ str(x) + '.txt', 'w') as file:
        file.write('test content'*x)