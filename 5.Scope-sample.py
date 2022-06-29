def check_scope():
    def do_local():                 #if we give print to this local method it'll print local-test while calling--Local always take inside the method
        test = "local test"

    def do_non_local():
        nonlocal test               #adding keyword "nonlocal" --it'll take test just above the method
        test = "non-local test"

    def do_global():
        global test                 #adding keyword "global" -- it'll take test outside the function
        test = "global test"

    test = "Default"

    do_local()
    print("test value after do-local: " + test)

    #lets call do-non-local by adding "nonlocal" keyword
    do_non_local()
    print("test value after do-non-local: " + test)

    # lets call do-global by adding "global" keyword
    do_global()
    print("test value after do-global: " + test)

check_scope()
print("test value after main: " + test)
