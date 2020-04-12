import os 


# kiem tra xem file co ton tai hay k
if os.path.exists("hjhj.txt"):
    os.remove("hjhj.txt")
else:
    print("My file does not exist")


# delete folder
os.rmdir("Myfolder")
