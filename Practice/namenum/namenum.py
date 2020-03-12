def getWords(num):
    numtoletter = {
   '2': ['A','B','C'],
   '3': ['D','E','F'],
   '4': ['G','H','I'],
   '5': ['J','K','L'],
   '6': ['M','N','O'],
   '7': ['P','R','S'],
   '8': ['T','U','v'],
   '9': ['W','X','Y'], }

    possibleNames = []

    

in_file = open("namenum.in", "r")
output = open("naumenum.in", "w")


num = in_file.readline().rstrip()


