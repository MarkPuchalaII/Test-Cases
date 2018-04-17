i = input().split()
if (i[0] == "what" and i[1] == "is") :
    i[0] = i[0]+i[1]
    i[1] = i[2]
if (len(i) > 1) : eval(i[1]+"."+i[0]+"()")
else : print("That does nothing.")

class hammertron():
    def make():
        print("lol")
    def trade():
        print("typer")

class effort():
    def whatis():
        print("Effort is a unit that divides a goal by the number of actions it requires, measured in ticks.")
#
# i = input().split()
# i[0] = i[0]+i[1]
# i[1] = i[2]
# print(i[0])
# print(i[1])
# print(i[2])
