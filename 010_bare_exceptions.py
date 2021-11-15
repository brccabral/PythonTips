try:
    s = input("Input a number")
    x = int(s)
except: # if there is no exception class, it will catch CTRL+C
    print("Not a number")


try:
    s = input("Input a number")
    x = int(s)
except Exception: # good way: catch some exception
    print("Not a number")


try:
    s = input("Input a number")
    x = int(s)
except ValueError: # better way: catch the correct exception
    print("Not a number")