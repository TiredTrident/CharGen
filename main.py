from random import randint
#from test2 import *
#^^^ this grabs stuff form a different pythond file, like variables and nubmers
print("Initilizing Character Generator")
#var = input('what will i write back to you:')
#print(var)


#name = input("Name: ")
#gender = input("Gender")
classlevel = input("class level:")
#randints or something


# get_stat that returns one value
#  def thing():
#      thing = randint(low_int, high_int)
#      return thing
def classhealthpoints():
	hitdice = randint(0,7)
	return hitdice
	
hitdie = classhealthpoints()
#classhitdie = hitdie * classlevel

def get_class(hitdie):
    classes = ["Barbarian", "Bard", "Cleric", "Fighter", "Monk", "Ranger", "Sorcerer", "Wizard"]
#   hp = ["12", "6", "8", "10", "8", "10", "6", "6"]
    try:
#       jobbo = randint(0,7)
#		health = hp[jobbo]
#       class = classes[hitdie]
        return classes[hitdie]
		
#		return health
    except:
        return classes[0]
#		return health

def get_health(hitdie):
    hp = [12, 6, 8, 10, 8, 10, 6, 6]
#    try:
    health = hp[hitdie]
    healthcalc = int(health) * int(classlevel)
    return healthcalc
#    except:
#        return hp[0]




def alignment(hitdie):
    align = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
    if(hitdie) = 0
        classalign = randint[3,8]
    if(hitdie) = 1
        classalign = randint[0,8]
    if(hitdie) = 2
        classalign = randint[0,8]
    if(hitdie) = 3
        classalign = randint[0,8]
    if(hitdie) = 4
	classalign = randint[0,8]
    if(hitdie) = 5
        classalign = randint[0,8]
    if(hitdie) = 6
        classalign = randint[0,8]
    if(hitdie) = 7
        classalign = randint[0,8]




def get_age():
    young_l = 14
    young_o = 27
    middle_l = 28
    middle_o = 45
    old_l = 46
    old_o = 85
    age_group = randint(1,10)
    
    #young group
    if age_group < 6:
        return(randint(young_l, young_o))
    #middle age
    elif age_group >= 6 and age_group <= 9:   
        return(randint(middle_l, middle_o))
    #old age    
    else:
        return(randint(old_l, old_o))

def get_stat(num_dice):
    values = []
    for item in range(num_dice):
        values.append(randint(3,18))

    return values


dex = get_stat(6)
job = get_class(hitdie)

text_file = open("Character.txt", "w")
#FIX THIS, YOU CAN LEARN PYTHON, NERD.
text_file.write("HP:" + str(get_health(hitdie)) + "\n")
text_file.write("Class:" + str(get_class(hitdie)) + "\n")
text_file.write("Age:" + str(get_age()) + "\n")
text_file.write("Str:" + str(get_stat(1)) + "\n")
text_file.write("Dex:" + str(get_stat(1)) + "\n")
text_file.write("Con:" + str(get_stat(1)) + "\n")
text_file.write("Int:" + str(get_stat(1)) + "\n")
text_file.write("Wis:" + str(get_stat(1)) + "\n")
text_file.write("Cha:" + str(get_stat(1)) + "\n")
text_file.close()
input()
