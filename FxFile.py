import time as t
from random import randint
from math import ceil

def grantXp(lvl, xp):
  xpadd = randint(5*lvl, 25*lvl)
  status = f" and {xpadd}XP "
  xp += xpadd
  if xp >= lvl*150:
    xp -= 150*lvl
    lvl += 1
    status = f", {xpadd}XP and 1 level up! \n you are now lvl {lvl}"
  return xp, lvl, status
    

def getArgs(input):
  cmd = ""
  args = []
  inplist = input.split(" ")
  for i in range(len(inplist)):
    if i == 0:
      cmd = inplist[i]
    else:
      args.append(inplist[i])
  return cmd, args

def calcTime():
  localtime = t.asctime(t.localtime(t.time())).split(" ")[4]
  return localtime
  
def load(cash, lvl, xp, hp, syntax, invlist):
  try:
      savefile = open("statsfile.txt")
      invfile = open("invfile.txt")
      savelist = savefile.readlines()
      values = savelist[0].split(",")
      cash, lvl, xp, hp, syntax = int(values[0]), int(values[1]), int(values[2]), int(values[3]), str(values[4])
      savefile.close()
      invlist = invfile.readlines()[0].split(",")
      for i in invlist:
        if i == "" or i == " ":
          invlist.remove(i)
      invfile.close()
      status = "files loaded"
  except:
      savefile = open("statsfile.txt", "w")
      savefile.write("0,1,0,100,!")
      savefile.close()
      invfile = open("invfile.txt", "w")
      invfile.write(",")
      invfile.close()
      status = "new files created! (if you had old ones these couldn't be found)"
  return cash, lvl, xp, hp, syntax, invlist, status

def save(cash, lvl, xp, hp, syntax, invlist):
  savefile = open("statsfile.txt", "w")
  savefile.write(str(cash)+","+str(lvl)+","+str(xp)+","+str(hp)+","+str(syntax))
  savefile.close()
  invfile = open("invfile.txt", "w")
  for i in range(len(invlist)):
    invfile.write(invlist[i])
    if i < len(invlist):
      invfile.write(",")
  invfile.close()
  status = "saved!"
  return status
  
def work(lvl):
  cashadd = randint(4*lvl, 10*lvl)
  status = f"you earned ${cashadd}"
  return cashadd, status    
  
def viewShop(shop):
  str_shop = ""
  for i in shop:
    str_shop += f"{i} | ${shop.get(i)} \n"
  return str_shop
  
def buyShop(shop, item, money, inv):
  item = item.lower()
  if item in shop:
    print(f"item {item} found for ${shop.get(item)}")
    if int(money) >= int(shop.get(item)):
      money -= int(shop.get(item))
      inv.append(item)
      print(f"inv: {inv}")
      status = f"item {item} bought for ${shop.get(item)}"
      return status, money
    else:
      status = f"not enough cash to buy {item} \nyou need ${shop.get(item)}"
      print(status)
      return status, money
      
  else:
    status = f"item {item} not found"
    return status, money
    
    
def useItem(item, list, inv, lvl):
  item = item.lower()
  cashadd = 0
  if item in list:
    if item in inv:
      itemslist = list.get(item)
      if item == "ammo":
        return itemslist[1], inv, 0, True
      cashadd = randint(0.8*itemslist[0]*lvl, 1.2*itemslist[0]*lvl)
      inv.remove(item)
      status = f"{itemslist[1]}${cashadd}"
      succes = True
    else:
      status = "item not owned"
      succes = False
  else:
    status = f"item \"{item}\" doesnt exist"
    succes = False
  return status, inv, cashadd, succes
  
def strinv(inv, list):
  str = "you own: \n"
  for i,j in enumerate(list):
    print(i, j)
    if inv.count(j) > 0:
      if i == len(list)-1:
       str += f"{inv.count(j)} {j}"
      else:
       str += f"{inv.count(j)} {j}\n"
    else:
      continue
  return str
  
def strhelp(list):

  return "\n".join(
  f" {j} | {list.get(j)}"
  for i,j in enumerate(list)
)
def checkInv(inv, lvl):
  if len(inv) >= (10*lvl)+1:
    return "full"
  else:
    return "fine"