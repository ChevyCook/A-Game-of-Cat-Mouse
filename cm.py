from dataclasses import dataclass
import random
import time, os, sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("clear")


@dataclass
class player:
    heartbeat: int
    stamina: int
    inventory_full: bool
    distance: int
    Game_over: bool
    Movement: int


P1 = player(1, 20, False, 30, False, 0)


@dataclass
class invent:
    Letter1: bool
    Keycard: bool
    Lighter: bool


inventory = invent(False, False, False)


def entity_moves_closer(P1: player) -> None:
    P1.distance -= random.randint(1, 3)
    if P1.distance <= 0:
        P1.Game_over = True
        P1.distance = 0


def stamina_depleation(P1: player) -> None:
        if (P1.stamina - 5) > 0:
            if P1.heartbeat >= 1 and P1.heartbeat <= 5 :
                P1.stamina -= 3
            elif P1.heartbeat >= 5 and P1.heartbeat <= 7:
                P1.stamina -= 6
            elif P1.heartbeat >= 7:
                P1.stamina -= 10
        else:
          P1.stamina = 0
        


def Room_options(Rooms):
    if Rooms == "Lobby":
        print("A[Sectetary Desk] B[Hide] C[Return]")
    if Rooms == "Office":
        print("A[Drawer] B[Locker] C[Return]")
    if Rooms == "Supply Room":
        print("A[Shelf] B[Cupboard] C[Hide] D[Return]")
    if Rooms == "Break Room":
        print("A[Cabinets] B[Fridge] C[Return]")
    if Rooms == "Board Room":
        print("A[Table] B[Hide] C[Return]")
    if Rooms == "Aurmoured Door":
        print("A[Open] B[Return] ")


def options(level):
    if level == "First Floor":
        print("A[Lobby] B[Office] C[Supply Room] D[Stairs] E[Hide]")

    if level == "Second Floor":
        print("A[Break Room]  B[Board Room] C[Check Armoured Door] D[Stairs] ")


def Action(level):
    if level == "First Floor":
        if Action == "A":
            level = "Lobby"
        if Action == "B":
            level = "Office"
        if Action == "C":
            level = "Supply Room"
        if Action == "D":
            level = "Second Floor"
        


def character_stats(P1: player) -> None:
    print("Heartbeat Intensity:", P1.heartbeat)
    print("Stamina:", P1.stamina)


def Heartbeat(P1: player, ) -> None:
    P1.heartbeat += 1


typingPrint("You wake up in a strage place\n Its too dark to see clearly\nbut you feel as if your not alone.")
time.sleep(1)
clearScreen()
typingPrint("In your confusion, a voice comes over an intercom")
time.sleep(1)
clearScreen()
typingPrint("\033[0;31;40m You've been brought here by the creature that invaded this building")
typingPrint("\nIts begun its persuit of you already\n")
typingPrint("I dont know much, but \n")
typingPrint("the creature affects it's prey in strange ways\n")
typingPrint("Your heartbeat increases when it gets close, however\n")
typingPrint("you can hide from it when this happens\n")
typingPrint("Fortunatly,there are ways to avoid this creature\n")
time.sleep(.5)
typingPrint("Search the building.\n")
time.sleep(.5)
typingPrint("There are items that can help you escape.\n")
time.sleep(.5)
typingPrint("I will assist you from here.")
time.sleep(1)
clearScreen()
typingPrint("This is a game of cat and mouse\n Don't get caught.\033[0;31;0m")
time.sleep(1)
clearScreen()

level = "First Floor"

while level == "First Floor":
    if P1.stamina == 0:
        typingPrint("\033[0;31;40m IT FOUND YOU")
        break
    else: 

      if P1.stamina == 0:
        clearScreen()
        typingPrint("\033[0;31;40m IT FOUND YOU")
        break
      action = input("A[Lobby] B[Office] C[Supply Room] D[Stairs] E[Hide]\n>").title()
  
      if action == "A":
          level = "Lobby"
      if action == "B":
          level = "Office"
      if action == "C":
          level = "Supply Room"
      if action == "D":
          level = "Second Floor"
      if action == "E":
        typingPrint("the creature moves on\n")
        typingPrint("you regain your strength")
        time.sleep(2)
        P1.heartbeat = 0
        P1.stamina = 30
        clearScreen()
        
        
    
  
      while level == "Lobby":
          stamina_depleation(P1)
          Heartbeat(P1)
        
          print("your in the", level)
          character_stats(P1)
          if inventory.Letter1 == False:
              inventory.Letter1 = True
              typingPrint("You found a letter behind the desk")
              time.sleep(3)
              level = "First Floor"
              clearScreen()
          else:
              typingPrint("There is nothing else here")
              time.sleep(3)
              level = "First Floor"
              clearScreen()
  
      while level == "Office":
          stamina_depleation(P1)
          Heartbeat(P1)
        

        
          print("your in the", level)
          character_stats(P1)
          if inventory.Keycard == False:
              inventory.Keycard = True
              typingPrint("You found a Keycard\nIt probably opens a door close by.")
              time.sleep(3)
              level = "First Floor"
              clearScreen()
          else:
              typingPrint("There is nothing else here")
              time.sleep(2)
              level = "First Floor"
              clearScreen()
        
  
      while level == "Supply Room":
          stamina_depleation(P1)
          Heartbeat(P1)
          print("your in the", level)
          character_stats(P1)
          if inventory.Lighter == False:
              inventory.Lighter = True
              typingPrint("You found a Lighter.\n")
              time.sleep(2)
              level = "First Floor"
              clearScreen()
          else:
              typingPrint("There is nothing else here")
              time.sleep(2)
              level = "First Floor"
              clearScreen()
  
    while level == "Second Floor":
      if P1.stamina == 0:
        typingPrint("\033[0;31;40m IT FOUND YOU")
        break
      else: 
        stamina_depleation(P1)
        Heartbeat(P1)
      
        print("your in the", level)
        character_stats(P1)
        action = input(
            "A[Break Room]  B[Board Room] C[Check Armoured Door] D[Stairs] "
        )
        if action == "A":
            level = "Break Room"
        if action == "B":
            level = "Board Room"
        if action == "C":
            level = "Check Armoured Door"
        if action == "D":
            level = "First Floor"
    
        while level == "Break Room":
            print("your in the", level)
            character_stats(P1)
    
        while level == "Board Room":
            print("your in the", level)
            character_stats(P1)
    
        while level == "Check Armoured Door":
            print("your in the", level)
            character_stats(P1)


        
