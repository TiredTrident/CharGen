from random import randint

#declare our fields here so they can be accesed later
l_names = []
f_names = []

#read in file
def get_names(filename): #in: filename, return list
    #read in a file
    lines = open(filename).read().splitlines()

    
    #chop of the list of names

    catagory = None
    for item in lines:
        print(item)
        if item == "":
            continue
        elif item.startswith("["):
            print("setting catagory")
            if item == "[first]":
                catagory = "first"
            elif item == "[last]":
                catagory = "last"
        else:
            if catagory == "last":
                l_names.append(item)
            if catagory == "first":
                f_names.append(item)
    print(f_names)
    print(l_names)

#owe kyle a beer

def get_1_name():
    print(len(f_names))
    f = randint(0, len(f_names) -1)
    l = randint(0, len(l_names) -1)
    print(str(f_names[f]) + " " + str(l_names[l]))

#names = input( "what file has your names in it")
names = "names.txt"
get_names(names)
get_1_name()
