from tkinter import Tk, Label, Button, mainloop, Entry, END
from FxFile import getArgs, calcTime, load, save, work, viewShop, buyShop, useItem, grantXp, strinv, checkInv, strhelp
from time import sleep
from math import ceil

version = "PRE 1.0.1"


cash = 0
lvl = 1
xp = 0
hp = 100
syntax ="!"
inv = []
status = "unloaded"
cash, lvl, xp, hp, syntax, inv, status = load(cash, lvl, xp, hp, syntax, inv)

shoplist = {
  "apple": 5,
  "coffee": 5,
  "ready-made-noodles": 10,
  "water-bottle": 10,
  "ammo": 20,
  "water-bucket": 35,
  "random-key": 50,
  "water-pistol": 75,
  "dynamite": 100,
  "tnt": 250,
  "gun": 500,
  "ak-47":750,
  "tsarbomba":1000000,
}

uselist ={
  "apple" : [5, "u won a bet against the doctor \nyou earned "],
  "coffee": [10, "U drank too much coffee \nyou got a caffeïne overdose so you did some \nchores for money and earned "],
  "ready-made-noodles": [25, "u ate da holy food \nsuddenly money appeared in ur hand \nu earned "],
  "water-bottle": [20, "you gave this bottle to a stranger \nhe gave you "],
  "ammo": [0, "this item is used for your guns, \ntherefore you must use your gun or ak-47 \nto use this item!"],
  "water-bucket": [50, "you did the best MLG water bucket \nin history and won "],
  "random-key": [75, "you dug up a random treasure \nchest and found "], 
  "water-pistol": [100, "you won a water fight and earned "],
  "dynamite": [150, "you robbed a bank and earned "],
  "tnt": [500, "you robbed a jewelry store at night \nyou got away with "],
  "gun": [750, "you did a job as hitman \nyour gun broke and you earned "],
  "ak-47": [1000, "you hosted a riot and earned "],
  "tsarbomba": [2000000, "you bombed a planet from outer space \nthe aliens gave you "]
}

cmdlist = {
  "inv": "shows inventory",
  "shop": "use this to buy / sell items",
  "changesyn": "change syntax",
  "time": "sends time",
  "use": "use an item",
  "work": "earn some money",
  "close": "saves and exits program",
  "save": "saves data",
  "balance": "shows your amount of cash",
  "lvlup": "shows required xp to lvl up",
  "help": "shows this :)"
}

def handle_keypress(event):
  print("enter!")
  execute()

def lbl(resp):
  response["text"] = resp
 
def updateStats():
  global cash, lvl, xp, hp, syntax, inv, status, version
  if cash >= 1000 and cash < 1000000:
    stats["text"] = f"cash: ${ceil((cash/1000)*10)/10}K lvl: {lvl} XP: {xp} HP: {hp} V: {version}"
  elif cash >= 1000000:
    stats["text"] = f"cash: ${ceil((cash/1000000)*10)/10}M lvl: {lvl} XP: {xp} HP: {hp} V: {version}"
  else:
    stats["text"] = f"cash: ${cash} lvl: {lvl} XP: {xp} HP: {hp} V: {version}"
  
  
def execute(): #event parameter from the Return-key keybind 
  print("executing")
  global cash, lvl, xp, hp, syntax, inv, status, app
  cmd, args = getArgs(input.get())
  cmd = cmd.lower()
  
  if cmd == syntax+"time":
    lbl(calcTime())
    
  elif cmd == syntax+"work":
    cashadd, status = work(lvl)
    cash += int(cashadd)
    cashstatus = status
    xpadd, lvl, status = grantXp(lvl,xp)
    xp = xpadd
    lbl(cashstatus+status)
    updateStats()
   
  elif cmd == syntax+"updatetop":
    print("updatin top")
    updateStats()
    
  elif cmd == syntax+"save":
    lbl(save(cash, lvl, xp, hp, syntax, inv))
    
  elif cmd == syntax+"viewshop":
    lbl(viewShop(shoplist))
    
  elif cmd == syntax+"buy":
    if checkInv(inv, lvl) == "full":
      lbl("inventory "+checkInv(inv, lvl))  
    else:
      status, cash = buyShop(shoplist, args[0], cash, inv)
      lbl(status)
      updateStats()
    
  elif cmd == syntax+"changesyn" or cmd == syntax+"changesyntax":
    syntax = args[0]
    lbl(f"syntax set to {syntax}")
    print(f"syntax set to {syntax}")
    
  elif cmd == "syntax":
    lbl(f"Syntax is {syntax}")
    
  elif cmd == syntax+"use":
    used = useItem(args[0], uselist, inv, lvl)
    if used[3] == True:
      cash += used[2]
      inv = used[1]
      cashstatus = status
      if args[0] != "ammo":
        xpadd, lvl, status = grantXp(lvl,xp)
        xp = xpadd
        lbl(used[0]+status)
      else:
        lbl(used[0])
      updateStats()
    else:
      lbl("failed to use item")
  elif cmd == syntax+"inv":
    lbl(strinv(inv, uselist))
    
  elif cmd == syntax+"help":
    lbl(strhelp(cmdlist))
    
  elif cmd == syntax+"lvlup":
    lbl(f"you need {lvl*150}XP to level up! \nyou have {xp}XP")
  else:
    lbl(f"something went wrong, \ncheck if you did these things: \n-Correct Syntax (currently: {syntax}) \n-Correct command spelling \n and try again")
  input.delete(0, END)

app = Tk()
stats = Label(width = 50, text = f"cash: ${cash} lvl: {lvl} XP: {xp} HP: {hp} V: {version}")
response = Label(text="execute your command, or run !help")
exeBtn = Button(text="execute", command=execute)
input = Entry(app)

app.bind("<Return>", handle_keypress)

stats.pack()
response.pack()
input.pack()
exeBtn.pack()

lbl(status)
updateStats()

app.mainloop()

#still need to implement:  !lvl