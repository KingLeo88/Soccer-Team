count = 1
dictKey = {}
dictNew = {}

while count <= 4:
    numJer = int(input("Enter player %d's jersey number:\n" % count))
    numRate = int(input("Enter player %d's rating:\n" % count))
    dictKey[numJer] = numRate
    jerList = list(dictKey.keys())
    jerList = sorted(jerList)
    count += 1
    print()

print("ROSTER")
for i in jerList:
  print("Jersey number: %d, Rating: %d" % (i, dictKey[i]))

while True:
 jerList = list(dictKey.keys())
 jerList = sorted(jerList)
 print()
 print("MENU")
 print("a - Add player")
 print("d - Remove player")
 print("u - Update player rating")
 print("r - Output players above a rating")
 print("o - Output roster")
 print("q - Quit")
 option = input("\nChoose an option:\n")
 if option == "q":
   exit()
 elif option == "o":
  print()
  print("Roster")
  for i in jerList:
    print("Jersey number: %d, Rating: %d" % (i, dictNew[i]))
 elif option == "a":
   numJer2 = int(input("Enter new player's jersey number:\n"))
   numRate2 = int(input("Enter the player's rating:"))
   dictNew[numJer2] = numRate2
   dictKey.update(dictNew)
 elif option == "d":
   remJer = int(input("Enter a jersey number:\n"))
   dictKey.pop(remJer)
 elif option == "u":
   updJEr = int(input("Enter a jersey number:\n"))
   rateUpd = int(input("Enter a new rating for player:\n"))
   dictKey[updJEr] = rateUpd
 elif option == "r":
   rateAbv = int(input("Enter a rating:\n"))
   print()
   print("ABOVE %d" % rateAbv)
   for jersey, rate in dictKey.items():
     if rate > rateAbv:
       print("Jersey number: %d, Rating: %d" %(jersey, rate))
     if rate <= rateAbv:
       continue
