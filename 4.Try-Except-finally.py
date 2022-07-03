try:
    f = open("sithara.py")
    try:
        f.write("print('Hello Python')")
    except:
        print("Error occur while writing contents")
    finally:
        f.close()

except:
    print("something wrong while opening text file")
