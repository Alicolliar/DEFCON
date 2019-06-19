#Primary WOPR Computer Program
#I was bored
#For use on the SBC Raspberry Pi, made by the brilliant The Raspberry Pi Foundation and is pure brilliance.
#Enjoy!
from random import randint
import RPi.GPIO as GPIO
import smtplib
#Pin Setup
def pin_setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(3, GPIO.OUT)
  GPIO.setup(5, GPIO.OUT)
  GPIO.setup(7, GPIO.OUT)
  GPIO.setup(11, GPIO.OUT)
  GPIO.setup(13, GPIO.OUT)
  GPIO.setup(15, GPIO.OUT)
  GPIO.setup(19, GPIO.OUT)
  GPIO.setup(21, GPIO.OUT)
  GPIO.setup(23, GPIO.OUT)
  GPIO.setup(29, GPIO.OUT)
  return

def mail_init():
  global mail_address
  mail_address = input("Command, please enter E-Mail Address.")
  global server
  server = smtplib.SMTP_SSL('smtplib.gmail.com', 456)
  server.login("your friend's gmail username here", "your buddy's gmail password here")
  return

def defcon():
    print("Welcome to the DefCon Selection Program")
    print("DefCon Level Meanings\n\n5.Low Threat.\n4. Low-Medium Threat.\n3. Medium Threat.\n2. Medium-High Threat.\n1. High Threat.\n")
    global level
    level = int(input("Please enter a DefCon level.\n>"))
    if level == 1:
        print("DefCon is 1, High Threat")
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, True)
    elif level == 2:
        print("Defcon is 2, Medium-High Threat")
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(13, False)
    elif level == 3:
        print("Defcon is 3, Medium Threat")
        GPIO.output(3, False)
        GPIO.output(5, False)
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(13, False)
    elif level == 4:
        print("Defcon is 4, Low-Medium Threat")
        GPIO.output(3, False)
        GPIO.output(5, True)
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
    elif level == 5:
        print("Defcon is 5, Low Threat")
        GPIO.output(3, True)
        GPIO.output(5, False)
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
    else:
        print("Level unavailable, try again.")
    return

def missile_test():
    chance = randint(1, 20)
    if chance >5:
        GPIO.output(15, True)
        GPIO.output(19, True)
        GPIO.output(21, True)
        GPIO.output(23, True)
        GPIO.output(29, True)
        print("All Missiles Functioning")
    elif chance == 2:
        GPIO.output(15, False)
        GPIO.output(19, True)
        GPIO.output(21, True)
        GPIO.output(23, True)
        GPIO.output(29, True)
        print("Failure On Missile 1, Report To Command And Check For System Malfunction.")
    elif chance == 3:
        GPIO.output(15, True)
        GPIO.output(19, False)
        GPIO.output(21, True)
        GPIO.output(23, True)
        GPIO.output(29, True)
        print("Failure On Missile 2, Report To Command And Check For System Malfunction.")
    elif chance == 4:
        GPIO.output(15, True)
        GPIO.output(19, True)
        GPIO.output(21, False)
        GPIO.output(23, True)
        GPIO.output(29, True)
        print("Failure On Missile 3, Report To Command And Check For System Malfunction.")
    elif chance == 5:
        GPIO.output(15, True)
        GPIO.output(19, True)
        GPIO.output(21, True)
        GPIO.output(23, False)
        GPIO.output(29, True)
        print("Failure On Missile 4, Report To Command And Check For System Malfunction.")
    else:
        GPIO.output(15, True)
        GPIO.output(19, True)
        GPIO.output(21, True)
        GPIO.output(23, True)
        GPIO.output(29, False)
        print("Failure On Missile 5, Report To Command And Check For System Malfunction.")
    return

def select():
  print("Welcome To The Target Selection Program.")
  global target
  target = []
  x=0
  while x < 5:
    target_input = str(input("Please enter a target.\n> "))
    target.append(target_input)
    x=x+1
  return

def firing():
  print("Welcome to the Firing Program.")
  while level < 2:
    print("Defense Condition is Low Enough To Continue With Launch Sequence.")
    print("Command Will Be Sent A Message Containing Launch Code Shortly.")
    code=randint(100000, 999999)
    codestr=str(code)
    server.sendmail("Frend's gmail address here.", mail_address, codestr)
    code_check = int(input("Please enter launch code here./n> ")
    if code_check == code:
        print("Welcome to the next stage")
    else:
        print("Hah, you gone done goofed it, son.")
        return
  else:
    print("Condition is not Low Enough for Firing.")
    return

def main():
  print("Welcome to the War Operations Planned Response (WOPR) Computer")
  print("Made By Colliar Industries")
  print("Please Make A Selection.")
  print("		1. DefCon Changer.\n")
  print("		2. Missile Test.\n")
  print("		3. Target Selection.\n")
  print("		4.Missile Firing.\n")
  choice = int(input("Make A Selection.\n>"))
  if choice == 1:
    defcon
  elif choice == 2:
    missile_test
  elif choice == 3:
    select
  elif choice == 4:
    firing
  else:
    print("Option not available, please try again.")

pin_setup
mail_init
main()
