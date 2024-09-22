import os, time
title = "My Guest List"

myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  print(f"{title: ^30}")
  print()
  firstName = input("WHat is the first name? ").strip().capitalize()
  lastName = input("What is the last name? ").strip().capitalize()
  fullName = f"{firstName} {lastName}"
  if fullName not in myList:
    myList.append(fullName)
  else:
    print(f"{fullName} already exist")
  print()
  printList()
  time.sleep(3)
  os.system("clear")


