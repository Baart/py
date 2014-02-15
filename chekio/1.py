def checkio(data):
    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data

    while(1):    
        print(initial_sofi, raise_sofi, initial_oldman, reduction_oldman)
        
        if(initial_sofi + raise_sofi <= initial_oldman):
            initial_sofi += raise_sofi

        if(initial_sofi >= initial_oldman):
            print("she propose", initial_sofi, "against", initial_oldman)
            print("he accept")
            return initial_sofi
        
        if(initial_oldman - reduction_oldman >= initial_sofi):
            initial_oldman -= reduction_oldman

        if(initial_sofi >= initial_oldman):
            print("he propose", initial_oldman, "against", initial_sofi)
            print("she accept")
            return initial_oldman

print (checkio([150, 50, 1000, 100]))
print (checkio([150, 50, 900, 100]))
