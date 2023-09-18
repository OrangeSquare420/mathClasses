def sjekkPrimtall(x):
    for devisor in range(2,x):
        kvotient = x/devisor
        
        if (kvotient == int(kvotient)):
            print(print(kvotient, '*', devisor, "=", x))
            
        
    print(x, "er et primtall")
    
    
sjekkPrimtall(int(input("Tall: ")))
