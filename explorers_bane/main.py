path = "D:/v1_0_0"

from copy import deepcopy
from tkinter import *
from random import randint
import os
import pickle

tk = Tk()
c = Canvas(tk,width=300,height=300,bg="#00ffff")
c.pack()
tk.update()

c.create_text(150,150,text="Loading",font=("Default",20))
c.create_text(150,180,text="anyidmap/idmap.txt")
tk.update()
a = open(f"{path}/explorers_bane/anyidmap/idmap.txt")
idmap = eval(a.read())
a.close()

c.delete(2)
c.create_text(150,180,text="anyidmap/entmap.txt")
tk.update()
a = open(f"{path}/explorers_bane/anyidmap/entmap.txt")
entmap = eval(a.read())
a.close()

c.delete(3)
c.create_text(150,180,text="recipes/recipes.txt")
tk.update()
a = open(f"{path}/explorers_bane/recipes/recipes.txt")
recipes = eval(a.read())
a.close()

c.delete(4)
c.create_text(150,180,text="recipes/rec_textures.txt")
tk.update()
a = open(f"{path}/explorers_bane/recipes/rec_textures.txt")
rectxt = eval(a.read())
a.close()

c.delete(5)
c.create_text(150,180,text="plain.txt")
tk.update()
a = open(f"{path}/explorers_bane/plain.txt")
world = eval(a.read())
a.close()

cmop = False

def generate():
    c.delete("all")
    if yaw == 0:
        for z_ in range(z+4,z,-1):
            for x_ in range(x-1,x+2):
                for y_ in range(y,y+3):
                    try:
                        back = z_-z-1
                        xa = (x_-x+1)*100
                        ya = (-(y_-y)+2)*100
                        color = idmap[world[(x_,y_,z_)]]["t"][back]
                        if back == 3:
                            if (x,y_,z-1) not in worldents and (x,y_,z-2) not in worldents and (x,y_,z-3) not in worldents:
                                dogen = True
                        if back == 2:
                            if (x,y_,z-1) not in worldents and (x,y_,z-2) not in worldents:
                                dogen = True
                        elif back == 1:
                            if (x,y_,z-1) not in worldents:
                                dogen = True
                        else:
                            dogen = True
                        if dogen:
                            c.create_rectangle(xa,ya,xa+100,ya+100,fill=color,outline="#ffffff")
                    except:
                        pass
    elif yaw == 1:
        for z_ in range(x+4,x,-1):
            for x_ in range(z+1,z-2,-1):
                for y_ in range(y,y+3):
                    try:
                        back = z_-x-1
                        xa = (-(x_-z)+1)*100
                        ya = (-(y_-y)+2)*100
                        color = idmap[world[(z_,y_,x_)]]["t"][back]
                        if back == 3:
                            if (x-1,y_,z) not in worldents and (x-2,y_,z) not in worldents and (x-3,y_,z) not in worldents:
                                dogen = True
                        if back == 2:
                            if (x-1,y_,z) not in worldents and (x-2,y_,z) not in worldents:
                                dogen = True
                        elif back == 1:
                            if (x-1,y_,z) not in worldents:
                                dogen = True
                        else:
                            dogen = True
                        if dogen:
                            c.create_rectangle(xa,ya,xa+100,ya+100,fill=color,outline="#ffffff")
                    except:
                        pass
    elif yaw == -1:
        for z_ in range(x-4,x):
            for x_ in range(z-1,z+2):
                for y_ in range(y,y+3):
                    try:
                        back = -(z_-x)-1
                        xa = (x_-z+1)*100
                        ya = (-(y_-y)+2)*100
                        color = idmap[world[(z_,y_,x_)]]["t"][back]
                        if back == 3:
                            if (x+1,y_,z) not in worldents and (x+2,y_,z) not in worldents and (x+3,y_,z) not in worldents:
                                dogen = True
                        if back == 2:
                            if (x+1,y_,z) not in worldents and (x+2,y_,z) not in worldents:
                                dogen = True
                        elif back == 1:
                            if (x+1,y_,z) not in worldents:
                                dogen = True
                        else:
                            dogen = True
                        if dogen:
                            c.create_rectangle(xa,ya,xa+100,ya+100,fill=color,outline="#ffffff")
                    except:
                        pass
    elif yaw == 2:
        for z_ in range(z-4,z):
            for x_ in range(x+1,x-2,-1):
                for y_ in range(y,y+3):
                    try:
                        back = -(z_-z)-1
                        xa = (-(x_-x)+1)*100
                        ya = (-(y_-y)+2)*100
                        color = idmap[world[(x_,y_,z_)]]["t"][back]
                        if back == 2:
                            if (x,y_,z+1) not in worldents and (x,y_,z+2) not in worldents:
                                dogen = True
                        elif back == 1:
                            if (x,y_,z+1) not in worldents:
                                dogen = True
                        else:
                            dogen = True
                        if dogen:
                            c.create_rectangle(xa,ya,xa+100,ya+100,fill=color,outline="#ffffff")
                    except:
                        pass
    if (x,y-1,z) in world:
        color = idmap[world[(x,y-1,z)]]["t"][back]
    else:
        color = None
    c.create_rectangle(0,300,300,320,fill=color,outline="#ffffff")
    c.create_text(57,310,text="Press Ctrl-H for help",fill="#ffffff")
    selec1 = "#000000"
    selec2 = "#000000"
    selec3 = "#000000"
    selec4 = "#000000"
    selec5 = "#000000"
    selec6 = "#000000"
    selec7 = "#000000"
    selec8 = "#000000"
    selec9 = "#000000"
    selec10 = "#000000"
    selec11 = "#000000"
    if pbid == 1:
        selec1 = "#ffffff"
    if pbid == 2:
        selec2 = "#ffffff"
    if pbid == 3:
        selec3 = "#ffffff"
    if pbid == 4:
        selec4 = "#ffffff"
    if pbid == 5:
        selec5 = "#ffffff"
    if pbid == 6:
        selec6 = "#ffffff"
    if pbid == 7:
        selec7 = "#ffffff"
    if pbid == 8:
        selec8 = "#ffffff"
    if pbid == 9:
        selec9 = "#ffffff"
    if pbid == 10:
        selec10 = "#ffffff"
    if pbid == 11:
        selec11 = "#ffffff"
    c.create_rectangle(0,320,300,380,fill="#ffffff")
    c.create_rectangle(0,320,30,350,fill="#00ff00",outline=selec1)
    c.create_rectangle(30,320,60,350,fill="#664400",outline=selec2)
    c.create_rectangle(60,320,90,350,fill="#555555",outline=selec3)
    c.create_rectangle(90,320,120,350,fill="#aa8800",outline=selec4)
    c.create_rectangle(130,320,140,350,fill="#886600",outline=selec5)
    c.create_rectangle(150,320,180,350,fill="#444444",outline=selec6)
    c.create_rectangle(198,320,208,350,fill="#886600",outline=selec7)
    c.create_rectangle(182,320,198,336,fill="#444444",outline=selec7)
    c.create_rectangle(228,320,238,350,fill="#886600",outline=selec8)
    c.create_rectangle(212,320,228,336,fill="#aa8800",outline=selec8)
    c.create_rectangle(240,320,255,335,fill="#ff3300",outline=selec9)
    c.create_rectangle(240,335,270,350,fill="#ff3300",outline=selec9)
    c.create_rectangle(270,320,300,350,fill="#00cc00",outline=selec10)
    c.create_rectangle(0,350,30,380,fill="#cccc66",outline=selec11)
    c.create_text(15,335,text=inventory[0])
    c.create_text(45,335,text=inventory[1])
    c.create_text(75,335,text=inventory[2])
    c.create_text(105,335,text=inventory[3])
    c.create_text(135,335,text=inventory[4])
    c.create_text(165,335,text=inventory[5],fill="#ffffff")
    c.create_text(190,328,text=inventory[6],fill="#ffffff")
    c.create_text(220,328,text=inventory[7])
    c.create_text(255,343,text=inventory[8])
    c.create_text(285,335,text=inventory[9])
    c.create_text(15,365,text=inventory[10])
    c.create_rectangle(228,8,292,24,fill="#ffffff")
    c.create_rectangle(228,8,(health/4)+228,24,fill="#ff0000")

def gen_ent():
    if yaw == 0:
        for z_ in range(z+3,z,-1):
            for x_ in range(x-1,x+2):
                for y_ in range(y,y+3):
                    try:
                        back = z_-z-1
                        xa = (x_-x+1)*100
                        ya = (-(y_-y)+2)*100
                        entity = worldents[(x_,y_,z_)]
                        entdir = entity["yaw"] % 2
                        entid = entity["id"]
                        if entdir == 0:
                            dir_ = "fr"
                        else:
                            dir_ = "s"
                        color = entmap[entid]["f"][back]
                        c.create_rectangle(xa+50-entmap[entid][dir_]["w"],ya-(entmap[entid][dir_]["h"]-100),xa+50+entmap[entid][dir_]["w"],ya+100,fill=color)
                    except:
                        pass
    elif yaw == 1:
        for z_ in range(x+3,x,-1):
            for x_ in range(z+1,z-2,-1):
                for y_ in range(y,y+3):
                    try:
                        back = z_-x-1
                        xa = (-(x_-z)+1)*100
                        ya = (-(y_-y)+2)*100
                        entity = worldents[(z_,y_,x_)]
                        entdir = (entity["yaw"]+1) % 2
                        entid = entity["id"]
                        if entdir == 0:
                            dir_ = "fr"
                        else:
                            dir_ = "s"
                        color = entmap[entid]["f"][back]
                        c.create_rectangle(xa+50-entmap[entid][dir_]["w"],ya-(entmap[entid][dir_]["h"]-100),xa+50+entmap[entid][dir_]["w"],ya+100,fill=color)
                    except:
                        pass
    elif yaw == -1:
        for z_ in range(x-3,x):
            for x_ in range(z-1,z+2):
                for y_ in range(y,y+3):
                    try:
                        back = -(z_-x)-1
                        xa = (x_-z+1)*100
                        ya = (-(y_-y)+2)*100
                        entity = worldents[(z_,y_,x_)]
                        entdir = (entity["yaw"]+1) % 2
                        entid = entity["id"]
                        if entdir == 0:
                            dir_ = "fr"
                        else:
                            dir_ = "s"
                        color = entmap[entid]["f"][back]
                        c.create_rectangle(xa+50-entmap[entid][dir_]["w"],ya-(entmap[entid][dir_]["h"]-100),xa+50+entmap[entid][dir_]["w"],ya+100,fill=color)
                    except:
                        pass
    elif yaw == 2:
        for z_ in range(z-3,z):
            for x_ in range(x+1,x-2,-1):
                for y_ in range(y,y+3):
                    try:
                        back = -(z_-z)-1
                        xa = (-(x_-x)+1)*100
                        ya = (-(y_-y)+2)*100
                        entity = worldents[(x_,y_,z_)]
                        entdir = entity["yaw"] % 2
                        entid = entity["id"]
                        if entdir == 0:
                            dir_ = "fr"
                        else:
                            dir_ = "s"
                        color = entmap[entid]["f"][back]
                        c.create_rectangle(xa+50-entmap[entid][dir_]["w"],ya-(entmap[entid][dir_]["h"]-100),xa+50+entmap[entid][dir_]["w"],ya+100,fill=color)
                    except:
                        pass

def spawn_ent():
    for vox in world:
        above = (vox[0],vox[1]+1,vox[2])
        if above not in world:
            for ent in entmap:
                e_map = entmap[ent]
                btype = e_map["b"]
                mxy = e_map["mxy"]
                mny = e_map["mny"]
                if world[vox] == btype and above[1] >= mny and above[1] <= mxy and above not in worldents:
                    prob = randint(1,1)
                    if prob == 1 and len(worldents) < 256:
                        worldents[above] = {
                            "id":ent,
                            "yaw":randint(-1,2),
                            "age":0
                            }
    worldents[(0,0,-1)] = {
        "id":0,
        "yaw":randint(-1,2),
        "age":0
        }

def upd_ent():
    old_worldents = deepcopy(worldents)
    for ent in old_worldents:
        try:
            e_map = worldents[ent]
            e_map["age"] += 1
            e_yaw = e_map["yaw"]
            e_yaw += randint(-1,1)
            if e_map["age"]%64 == 0:
                if e_yaw == 3:
                    e_yaw = 2
                elif e_yaw == -2:
                    e_yaw = 2
                if e_yaw == 0:
                    bfr = (ent[0],ent[1],ent[2]+1)
                    ubfr = (ent[0],ent[1]+1,ent[2]+1)
                elif e_yaw == 1:
                    bfr = (ent[0]+1,ent[1],ent[2])
                    ubfr = (ent[0]+1,ent[1]+1,ent[2])
                elif e_yaw == -1:
                    bfr = (ent[0]-1,ent[1],ent[2])
                    ubfr = (ent[0]-1,ent[1]+1,ent[2])
                elif e_yaw == 2:
                    bfr = (ent[0],ent[1],ent[2]-1)
                    ubfr = (ent[0],ent[1]+1,ent[2]-1)
                if bfr not in world:
                    if bfr not in worldents:
                        worldents[bfr] = e_map
                        del worldents[ent]
                elif ubfr not in world and ubfr not in worldents:
                    worldents[ubfr] = e_map
                    del worldents[ent]
            if (ent[0],ent[1]-1,ent[2]) not in world:
                worldents[(ent[0],ent[1]-1,ent[2])] = e_map
                del worldents[ent]
        except:
            pass

def rem_ent():
    old_worldents = deepcopy(worldents)
    for ent in old_worldents:
        if worldents[ent]["age"] == 1024:
            del worldents[ent]

def ent_atk():
    global health
    if (x,y,z+1) in worldents and entmap[worldents[(x,y,z+1)]["id"]]["a"]:
        health -= 1
    if (x,y,z-1) in worldents and entmap[worldents[(x,y,z-1)]["id"]]["a"]:
        health -= 1
    if (x+1,y,z) in worldents and entmap[worldents[(x+1,y,z)]["id"]]["a"]:
        health -= 1
    if (x-1,y,z) in worldents and entmap[worldents[(x-1,y,z)]["id"]]["a"]:
        health -= 1
    if (x,y,z) in worldents and entmap[worldents[(x,y,z)]["id"]]["a"]:
        health -= 1

def fall():
    global y
    global fallt
    if (x,y-1,z) not in world or not idmap[world[(x,y-1,z)]]["m"]:
        fallt -= 0.03
    else:
        fallt = 1
    if fallt <= 0:
        fallt = 1
        y -= 1

def left(event):
    global yaw
    if yaw > -1:
        yaw -= 1
    elif yaw == -1:
        yaw = 2

def right(event):
    global yaw
    if yaw < 2:
        yaw += 1
    elif yaw == 2:
        yaw = -1

def up(event):
    global y
    if spc:
        y += 1
    elif (x,y+2,z) not in world or not idmap[world[(x,y+2,z)]]["m"]:
        if sbornot == 0:
            if (x,y-1,z) in world:
                y +=1
        else:
            y += 1

def down(event):
    global y
    if spc:
        y -= 1
    elif (x,y-1,z) not in world or not idmap[world[(x,y-1,z)]]["m"]:
        y -= 1

def forth(event):
    global x
    global z
    if yaw == 0:
        if spc:
            z += 1
        elif (x,y,z+1) not in world or not idmap[world[(x,y,z+1)]]["m"]:
            z += 1
    elif yaw == 1:
        if spc:
            x += 1
        elif (x+1,y,z) not in world or not idmap[world[(x+1,y,z)]]["m"]:
            x += 1
    elif yaw == -1:
        if spc:
            x -= 1
        elif (x-1,y,z) not in world or not idmap[world[(x-1,y,z)]]["m"]:
            x -= 1
    elif yaw == 2:
        if spc:
            z -= 1
        elif (x,y,z-1) not in world or not idmap[world[(x,y,z-1)]]["m"]:
            z -= 1

def minef(event):
    global inventory
    global world
    bid = None
    if yaw == 0:
        if (x,y+1,z+1) in world:
            bid = world[(x,y+1,z+1)]
            coords = (x,y+1,z+1)
        elif (x,y+1,z+2) in world:
            bid = world[(x,y+1,z+2)]
            coords = (x,y+1,z+2)
        elif (x,y+1,z+3) in world:
            bid = world[(x,y+1,z+3)]
            coords = (x,y+1,z+3)
    elif yaw == 1:
        if (x+1,y+1,z) in world:
            bid = world[(x+1,y+1,z)]
            coords = (x+1,y+1,z)
        elif (x+2,y+1,z) in world:
            bid = world[(x+2,y+1,z)]
            coords = (x+2,y+1,z)
        elif (x+3,y+1,z) in world:
            bid = world[(x+3,y+1,z)]
            coords = (x+3,y+1,z)
    elif yaw == -1:
        if (x-1,y+1,z) in world:
            bid = world[(x-1,y+1,z)]
            coords = (x-1,y+1,z)
        elif (x-2,y+1,z) in world:
            bid = world[(x-2,y+1,z)]
            coords = (x-2,y+1,z)
        elif (x-3,y+1,z) in world:
            bid = world[(x-3,y+1,z)]
            coords = (x-3,y+1,z)
    elif yaw == 2:
        if (x,y+1,z-1) in world:
            bid = world[(x,y+1,z-1)]
            coords = (x,y+1,z-1)
        elif (x,y+1,z-2) in world:
            bid = world[(x,y+1,z-2)]
            coords = (x,y+1,z-2)
        elif (x,y+1,z-3) in world:
            bid = world[(x,y+1,z-3)]
            coords = (x,y+1,z-3)
    if bid != None and idmap[bid]["m"]:
        if idmap[bid]["i"] == None:
            inventory[idmap[bid]["io"]] += 1
            del world[coords]
        elif inventory[idmap[bid]["i"]] > 0:
            inventory[idmap[bid]["io"]] += 1
            del world[coords]

def mineu(event):
    global inventory
    global world
    bid = None
    if (x,y+1,z) in world:
        bid = world[(x,y+1,z)]
        coords = (x,y+2,z)
    elif (x,y+2,z) in world:
        bid = world[(x,y+2,z)]
        coords = (x,y+2,z)
    if bid != None and idmap[bid]["m"]:
        if idmap[bid]["i"] == None:
            inventory[idmap[bid]["io"]] += 1
            del world[coords]
        elif inventory[idmap[bid]["i"]] > 0:
            inventory[idmap[bid]] += 1
            del world[coords]

def mined(event):
    global inventory
    global world
    if (x,y-1,z) in world:
        bid = world[(x,y-1,z)]
        coords = (x,y-1,z)
        if idmap[bid]["m"]:
            if idmap[bid]["i"] == None:
                inventory[idmap[bid]["io"]] += 1
                del world[coords]
            elif inventory[idmap[bid]["i"]] > 0:
                inventory[idmap[bid]["io"]] += 1
                del world[coords]

def mineld(event):
    global inventory
    global world
    bid = None
    if yaw == 0:
        if (x,y,z+1) in world:
            bid = world[(x,y,z+1)]
            coords = (x,y,z+1)
    elif yaw == 1:
        if (x+1,y,z) in world:
            bid = world[(x+1,y,z)]
            coords = (x+1,y,z)
    elif yaw == -1:
        if (x-1,y,z) in world:
            bid = world[(x-1,y,z)]
            coords = (x-1,y,z)
    elif yaw == 2:
        if (x,y,z-1) in world:
            bid = world[(x,y,z-1)]
            coords = (x,y,z-1)
    if bid != None and idmap[bid]["m"]:
        if idmap[bid]["i"] == None:
            inventory[idmap[bid]["io"]] += 1
            del world[coords]
        elif inventory[idmap[bid]["i"]] > 0:
            inventory[idmap[bid]["io"]] += 1
            del world[coords]
    

def placef(event):
    global inventory
    global world
    dosub = False
    if inventory[idmap[pbid]["in"]] > 0:
        if yaw == 0:
            if (x,y+1,z+2) in world:
                world[(x,y+1,z+1)] = pbid
                dosub = True
            elif (x,y+1,z+3) in world:
                world[(x,y+1,z+2)] = pbid
                dosub = True
        elif yaw == 1:
            if (x+2,y+1,z) in world:
                world[(x+1,y+1,z)] = pbid
                dosub = True
            elif (x+3,y+1,z) in world:
                world[(x+2,y+1,z)] = pbid
                dosub = True
        elif yaw == -1:
            if (x-2,y+1,z) in world:
                world[(x-1,y+1,z)] = pbid
                dosub = True
            elif (x-3,y+1,z) in world:
                world[(x-2,y+1,z)] = pbid
                dosub = True
        elif yaw == 2:
            if (x,y+1,z-2) in world:
                world[(x,y+1,z-1)] = pbid
                dosub = True
            elif (x,y+1,z-3) in world:
                world[(x,y+1,z-2)] = pbid
                dosub = True
        if dosub and not sbornot:
            inventory[idmap[pbid]["in"]] -= 1

def placeu(event):
    global inventory
    global world
    if inventory[idmap[bid]["in"]] > 0:
        if (x,y+2,z) not in world:
            world[(x,y+2,z)] = pbid
            if not sbornot:
                inventory[idmap[pbid]["in"]] -= 1

def placed(event):
    global inventory
    global world
    if inventory[idmap[pbid]["in"]] > 0:
        if (x,y-1,z) not in world:
            world[(x,y-1,z)] = pbid
            if not sbornot:
                inventory[idmap[pbid]["in"]] -= 1

def placelu(event):
    global inventory
    global world
    if inventory[idmap[pbid]["in"]] > 0:
        if yaw == 0:
            if (x,y+1,z+1) in world and (x,y+2,z+1) not in world:
                world[(x,y+2,z+1)] = pbid
                dosub = True
        elif yaw == 1:
            if (x+1,y+1,z) in world and (x+1,y+2,z) not in world:
                world[(x+1,y+2,z)] = pbid
                dosub = True
        elif yaw == -1:
            if (x-1,y+1,z) in world and (x-1,y+2,z) not in world:
                world[(x-1,y+2,z)] = pbid
                dosub = True
        elif yaw == 2:
            if (x,y+1,z-1) in world and (x,y+2,z-1) not in world:
                world[(x,y+2,z-1)] = pbid
                dosub = True
        if dosub and not sbornot:
            inventory[idmap[pbid]["in"]] -= 1

def placeld(event):
    global inventory
    global world
    dosub = False
    if inventory[idmap[pbid]["in"]] > 0:
        if yaw == 0:
            if ((x,y+1,z+1) in world or (x,y-1,z+1) in world) and (x,y,z+1) not in world:
                world[(x,y,z+1)] = pbid
                dosub = True
        elif yaw == 1:
            if ((x+1,y+1,z) in world or (x+1,y-1,z) in world) and (x,y,z+1) not in world:
                world[(x+1,y,z)] = pbid
                dosub = True
        elif yaw == -1:
            if ((x-1,y+1,z) in world or (x-1,y-1,z) in world) and (x,y,z+1) not in world:
                world[(x-1,y,z)] = pbid
                dosub = True
        elif yaw == 2:
            if ((x,y+1,z-1) in world or (x,y-1,z-1) in world) and (x,y,z+1) not in world:
                world[(x,y,z-1)] = pbid
                dosub = True
        if dosub and not sbornot:
            inventory[idmap[pbid]["in"]] -= 1

def placell(event):
    global inventory
    global world
    if inventory[idmap[pbid]["in"]] > 0:
        if yaw == 0:
            if (x,y+1,z+1) in world and (x-1,y+1,z+1) not in world:
                world[(x-1,y+1,z+1)] = pbid
                dosub = True
        elif yaw == 1:
            if (x+1,y+1,z) in world and (x+1,y+1,z+1) not in world:
                world[(x+1,y+1,z+1)] = pbid
                dosub = True
        elif yaw == -1:
            if (x-1,y+1,z) in world and (x-1,y+1,z-1) not in world:
                world[(x-1,y+1,z-1)] = pbid
                dosub = True
        elif yaw == 2:
            if (x,y+1,z-1) in world and (x+1,y+1,z-1) not in world:
                world[(x+1,y+1,z-1)] = pbid
                dosub = True
        if dosub and not sbornot:
            inventory[idmap[pbid]["in"]] -= 1

def placelr(event):
    global inventory
    global world
    if inventory[idmap[pbid]["in"]] > 0:
        if yaw == 0:
            if (x,y+1,z+1) in world and (x+1,y+1,z+1) not in world:
                world[(x+1,y+1,z+1)] = pbid
                dosub = True
        elif yaw == 1:
            if (x+1,y+1,z) in world and (x+1,y+1,z-1) not in world:
                world[(x+1,y+1,z-1)] = pbid
                dosub = True
        elif yaw == -1:
            if (x-1,y+1,z) in world and (x-1,y+1,z+1) not in world:
                world[(x-1,y+1,z+1)] = pbid
                dosub = True
        elif yaw == 2:
            if (x,y+1,z-1) in world and (x-1,y+1,z-1) not in world:
                world[(x-1,y+1,z-1)] = pbid
                dosub = True
        if dosub and not sbornot:
            inventory[idmap[pbid]["in"]] -= 1

def pickb(event):
    global pbid
    if yaw == 0:
        if (x,y+1,z+1) in world:
            pbid = world[(x,y+1,z+1)]
        elif (x,y+1,z+2) in world:
            pbid = world[(x,y+1,z+2)]
        elif (x,y+1,z+3) in world:
            pbid = world[(x,y+1,z+3)]
    elif yaw == 1:
        if (x+1,y+1,z) in world:
            pbid = world[(x+1,y+1,z)]
        elif (x+2,y+1,z) in world:
            pbid = world[(x+2,y+1,z)]
        elif (x+3,y+1,z) in world:
            pbid = world[(x+3,y+1,z)]
    elif yaw == -1:
        if (x-1,y+1,z) in world:
            pbid = world[(x-1,y+1,z)]
        elif (x-2,y+1,z) in world:
            pbid = world[(x-2,y+1,z)]
        elif (x-3,y+1,z) in world:
            pbid = world[(x-3,y+1,z)]
    elif yaw == 2:
        if (x,y+1,z-1) in world:
            pbid = world[(x,y+1,z-1)]
        elif (x,y+1,z-2) in world:
            pbid = world[(x,y+1,z-2)]
        elif (x,y+1,z-3) in world:
            pbid = world[(x,y+1,z-3)]

def pickr(event):
    global pbid
    if pbid < 11:
        pbid += 1

def pickl(event):
    global pbid
    if pbid > 1:
        pbid -= 1

def makebc(event):
    global bx
    global by
    global bz
    global byaw
    bx = x
    by = y
    bz = z
    byaw = yaw

def gotobc(event):
    global x
    global y
    global z
    global yaw
    x = bx
    y = by
    z = bz
    yaw = byaw

def craftmenu(event):
    global cgui
    global ciip
    global cm
    global items
    cm = Tk()
    cgui = Canvas(cm,width=30,height=30)
    cgui.pack()
    items = []
    for item in recipes:
        itemmap = recipes[item]
        show = True
        for ing in itemmap:
            if inventory[ing] < itemmap[ing]:
                show = False
        if show:
            items.append(item)
    if len(items) > 0:
        ciip = 0
        cgui.bind_all("<Return>",craft)
        cgui.bind_all("<KeyPress-Up>",goupc)
        cgui.bind_all("<KeyPress-Down>",godownc)
        exec(rectxt[items[ciip]])
        cm.update()
    else:
        cm.destroy()

def craft(event):
    global cgui
    global inventory
    iid = items[ciip]
    itemmap = recipes[iid]
    for item in itemmap:
        inventory[item] -= itemmap[item]
    inventory[iid] += 1
    cm.destroy()

def goupc(event):
    global ciip
    if ciip == 0:
        ciip = len(items)-1
    else:
        ciip -= 1
    exec(rectxt[items[ciip]])
    cm.update()

def godownc(event):
    global ciip
    if ciip == len(items)-1:
        ciip = 0
    else:
        ciip += 1
    exec(rectxt[items[ciip]])
    cm.update()

def eat(event):
    global health
    global inventory
    if inventory[8] > 0 and health < 256:
        health += 16
        if health > 256:
            health = 256
        inventory[8] -= 1

def kill(event):
    global inventory
    global worldents
    eid = None
    if yaw == 0:
        if (x,y,z+1) in worldents:
            eid = worldents[(x,y,z+1)]
            coords = (x,y,z+1)
    elif yaw == 1:
        if (x+1,y,z) in worldents:
            eid = worldents[(x+1,y,z)]
            coords = (x+1,y,z)
    elif yaw == -1:
        if (x-1,y,z) in worldents:
            eid = worldents[(x-1,y,z)]
            coords = (x-1,y,z)
    elif yaw == 2:
        if (x,y,z-1) in worldents:
            eid = worldents[(x,y,z-1)]
            coords = (x,y,z-1)
    if eid != None and entmap[eid["id"]]["io"] != None:
        inventory[entmap[eid["id"]]["io"]] += 1
        del worldents[coords]

def save(event):
    a = open(f"{path}/explorers_bane/save/x.txt","w+b")
    a.write(pickle.dumps(x))
    a.close()
    a = open(f"{path}/explorers_bane/save/y.txt","w+b")
    a.write(pickle.dumps(y))
    a.close()
    a = open(f"{path}/explorers_bane/save/z.txt","w+b")
    a.write(pickle.dumps(z))
    a.close()
    a = open(f"{path}/explorers_bane/save/yaw.txt","w+b")
    a.write(pickle.dumps(yaw))
    a.close()
    a = open(f"{path}/explorers_bane/save/bx.txt","w+b")
    a.write(pickle.dumps(bx))
    a.close()
    a = open(f"{path}/explorers_bane/save/by.txt","w+b")
    a.write(pickle.dumps(by))
    a.close()
    a = open(f"{path}/explorers_bane/save/bz.txt","w+b")
    a.write(pickle.dumps(bz))
    a.close()
    a = open(f"{path}/explorers_bane/save/byaw.txt","w+b")
    a.write(pickle.dumps(byaw))
    a.close()
    a = open(f"{path}/explorers_bane/save/pbid.txt","w+b")
    a.write(pickle.dumps(pbid))
    a.close()
    a = open(f"{path}/explorers_bane/save/world.txt","w+b")
    a.write(pickle.dumps(world))
    a.close()
    a = open(f"{path}/explorers_bane/save/fallt.txt","w+b")
    a.write(pickle.dumps(fallt))
    a.close()
    a = open(f"{path}/explorers_bane/save/health.txt","w+b")
    a.write(pickle.dumps(health))
    a.close()
    a = open(f"{path}/explorers_bane/save/inventory.txt","w+b")
    a.write(pickle.dumps(inventory))
    a.close()
    a = open(f"{path}/explorers_bane/save/worldents.txt","w+b")
    a.write(pickle.dumps(worldents))
    a.close()
    a = open(f"{path}/explorers_bane/save/spc.txt","w+b")
    a.write(pickle.dumps(spc))
    a.close()
    a = open(f"{path}/explorers_bane/save/sbornot.txt","w+b")
    a.write(pickle.dumps(sbornot))
    a.close()

def load(event):
    global x
    global y
    global z
    global yaw
    global bx
    global by
    global bz
    global byaw
    global pbid
    global world
    global fallt
    global health
    global inventory
    global worldents
    global spc
    global mode
    a = open(f"{path}/explorers_bane/save/x.txt","rb")
    b = a.read()
    x = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/y.txt","rb")
    b = a.read()
    y = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/z.txt","rb")
    b = a.read()
    z = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/yaw.txt","rb")
    b = a.read()
    yaw = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/bx.txt","rb")
    b = a.read()
    bx = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/by.txt","rb")
    b = a.read()
    by = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/bz.txt","rb")
    b = a.read()
    bz = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/byaw.txt","rb")
    b = a.read()
    byaw = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/pbid.txt","rb")
    b = a.read()
    pbid = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/world.txt","rb")
    b = a.read()
    world = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/fallt.txt","rb")
    b = a.read()
    fallt = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/health.txt","rb")
    b = a.read()
    health = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/inventory.txt","rb")
    b = a.read()
    inventory = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/worldents.txt","rb")
    b = a.read()
    worldents = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/spc.txt","rb")
    b = a.read()
    spc = pickle.loads(b)
    a.close()
    a = open(f"{path}/explorers_bane/save/sbornot.txt","rb")
    b = a.read()
    sbornot = pickle.loads(b)
    a.close()

def help_(event):
    hwin = Tk()
    i = Canvas(hwin,width=390,height=250,bg="#000000")
    i.pack()
    i.create_text(195,10,text="Walk forward with W",fill="#ffffff")
    i.create_text(195,20,text="Move vertically with arrow keys",fill="#ffffff")
    i.create_text(195,30,text="Turn with A/D",fill="#ffffff")
    i.create_text(195,40,text="Mine with G",fill="#ffffff")
    i.create_text(195,50,text="Mine up/down with T/B",fill="#ffffff")
    i.create_text(195,60,text="Place with K",fill="#ffffff")
    i.create_text(195,70,text="Place up/down with I/M",fill="#ffffff")
    i.create_text(195,80,text="Pick voxel with L",fill="#ffffff")
    i.create_text(195,90,text="Make beacon with Z",fill="#ffffff")
    i.create_text(195,100,text="Go to beacon with C",fill="#ffffff")
    i.create_text(195,110,text="Save game with Ctrl-S",fill="#ffffff")
    i.create_text(195,120,text="Load game with Ctrl-O",fill="#ffffff")
    i.create_text(195,130,text="Craft item with E",fill="#ffffff")
    i.create_text(195,140,text="While crafting, scroll with arrow keys",fill="#ffffff")
    i.create_text(195,150,text="Eat with Q",fill="#ffffff")
    i.create_text(195,160,text="Kill entity with space",fill="#ffffff")
    i.create_text(195,170,text="Pull up help section with Ctrl-H",fill="#ffffff")
    i.create_text(195,180,text="The nine squares in front of you are your vision",fill="#ffffff")
    i.create_text(195,190,text="They darken when they are farther away",fill="#ffffff")
    i.create_text(195,200,text="The long rectangle in front of you is the block under you",fill="#ffffff")
    i.create_text(195,210,text="Use number keys to obtain the corresponding voxel",fill="#ffffff")
    i.create_text(195,220,text="0 is grass, 1 is dirt, 2 is stone, 3 is wood, 4 is rocks, 5 is leaves, 6 is sand",fill="#ffffff")
    i.create_text(195,230,text="Mine the voxel below in front of you with V",fill="#ffffff")
    i.create_text(195,240,text="Place the voxel up/down/left/right in front of you with U/N/J/O",fill="#ffffff")
    c.unbind_all("<Control-h>")

def credits_():
    cwin = Tk()
    j = Canvas(cwin,width=390,height=250,bg="#000000")
    j.pack()
    j.create_text(195,10,text="CODING",fill="#ffffff")
    j.create_text(195,20,text="UnbihexiumFan",fill="#ffffff")
    j.create_text(195,30,text="IDEAS",fill="#ffffff")
    j.create_text(195,40,text="UnbihexiumFan",fill="#ffffff")
    j.create_text(195,50,text="Nolan559",fill="#ffffff")

def start(mode=0):
    global world
    global x
    global y
    global z
    global yaw
    global fallt
    global bx
    global by
    global bz
    global byaw
    global pbid
    global health
    global worldents
    global inventory
    global spc
    global sbornot
    
    c.config(height=380)
    
    spc = mode == 2
    sbornot = bool(mode)

    play.destroy()
    play_s.destroy()
    play_sp.destroy()
    cred.destroy()
    
    x = 0
    y = 0
    z = 0
    yaw = 0
    fallt = 1
    bx = 0
    by = 0
    bz = 0
    byaw = 0
    pbid = 1
    health = 256
    inventory = {
        0:sbornot,
        1:sbornot,
        2:sbornot,
        3:sbornot,
        4:sbornot,
        5:sbornot,
        6:sbornot,
        7:sbornot,
        8:sbornot,
        9:sbornot,
        10:sbornot
        }
    worldents = {}

    add_text = ""

    for tree in range(31):
        x_ = randint(-32,31)
        z_ = randint(-32,31)
        if x_ != 0 and z_ != 0 and (x_,0,z_) not in world:
            world[(x_,0,z_)] = 3
            world[(x_,1,z_)] = 3
            world[(x_,2,z_)] = 3
            world[(x_,3,z_)] = 3
            world[(x_+1,3,z_)] = 4
            world[(x_-1,3,z_)] = 4
            world[(x_,3,z_+1)] = 4
            world[(x_,3,z_-1)] = 4
            world[(x_,4,z_)] = 4

    for rock in range(128):
        x_ = randint(-32,31)
        z_ = randint(-32,31)
        if x_ != 0 and z_ != 0 and (x_,0,z_) not in world:
            world[(x_,0,z_)] = 6

    for cave in range(8):
        x_ = randint(-29,28)
        y_ = randint(-21,-10)
        z_ = randint(-29,28)
        bfd = [(x_,y_,z_),(x_+1,y_,z_),(x_-1,y_,z_),(x_,y_,z_+1),(x_,y_,z_-1),(x_,y_+1,z_),(x_,y_-1,z_),(x_,y_+2,z_),(x_,y_+1,z_),(x_+1,y_+1,z_),(x_-1,y_+1,z_),(x_,y_+1,z_+1),(x_,y_+1,z_-1),(x_+2,y_,z_),(x_+1,y_,z_+1),(x_,y_,z_+2),(x_-1,y_,z_+1),(x_-2,y_,z_),(x_-1,y_,z_-1),(x_,y_,z_-2),(x_+1,y_,z_-1),(x_,y_-1,z_),(x_+1,y_-1,z_),(x_-1,y_-1,z_),(x_,y_-1,z_+1),(x_,y_-1,z_-1),(x_,y_-2,z_)]
        for vox in bfd:
            if vox in world:
                del world[vox]

    for lake in range(64):
        x_ = randint(-30,29)
        z_ = randint(-30,29)
        if x_ != 0 and z_ != 0 and (x_,0,z_) not in world and (x_-1,0,z_) not in world and (x_,0,z_+1) not in world and (x_,0,z_-1) not in world:
            world[(x_,-1,z_)] = 5
            world[(x_+1,-1,z_)] = 5
            world[(x_-1,-1,z_)] = 5
            world[(x_,-1,z_+1)] = 5
            world[(x_,-1,z_-1)] = 5
            bfs = [(x_+2,-1,z_),(x_+1,-1,z_+1),(x_,-1,z_+2),(x_-1,-1,z_+1),(x_-2,-1,z_),(x_-1,-1,z_-1),(x_,-1,z_-2),(x_+1,-1,z_-1)]
            for vox in bfs:
                world[vox] = 7

    c.configure(bg="#000000")

    c.bind_all("<KeyPress-a>",left)
    c.bind_all("<KeyPress-d>",right)
    c.bind_all("<KeyPress-Up>",up)
    c.bind_all("<KeyPress-w>",forth)
    c.bind_all("<KeyPress-g>",minef)
    c.bind_all("<KeyPress-t>",mineu)
    c.bind_all("<KeyPress-b>",mined)
    c.bind_all("<KeyPress-v>",mineld)
    c.bind_all("<KeyPress-k>",placef)
    c.bind_all("<KeyPress-i>",placeu)
    c.bind_all("<KeyPress-m>",placed)
    c.bind_all("<KeyPress-u>",placelu)
    c.bind_all("<KeyPress-n>",placeld)
    c.bind_all("<KeyPress-j>",placell)
    c.bind_all("<KeyPress-o>",placelr)
    c.bind_all("<KeyPress-l>",pickb)
    c.bind_all("<KeyPress-Left>",pickl)
    c.bind_all("<KeyPress-Right>",pickr)
    c.bind_all("<KeyPress-e>",craftmenu)
    c.bind_all("<KeyPress-q>",eat)
    c.bind_all("<Return>",kill)
    c.bind_all("<Control-s>",save)
    c.bind_all("<Control-o>",load)
    c.bind_all("<Control-h>",help_)

    while True:
        tk.geometry("304x384")
        gen_ent()
        generate()
        spawn_ent()
        upd_ent()
        rem_ent()
        if not sbornot:
            ent_atk()
            fall()
        tk.update()
        if not mode and (y < -25 or x > 31 or x < -32 or z > 31 or z < -32 or health == 0):
            world = {}
            c.unbind_all("<KeyPress-a>")
            c.unbind_all("<KeyPress-d>")
            c.unbind_all("<KeyPress-Down>")
            c.unbind_all("<KeyPress-Up>")
            c.unbind_all("<KeyPress-w>")
            c.unbind_all("<KeyPress-g>")
            c.unbind_all("<KeyPress-t>")
            c.unbind_all("<KeyPress-b>")
            c.unbind_all("<KeyPress-v>")
            c.unbind_all("<KeyPress-k>")
            c.unbind_all("<KeyPress-i>")
            c.unbind_all("<KeyPress-m>")
            c.unbind_all("<KeyPress-u>")
            c.unbind_all("<KeyPress-n>")
            c.unbind_all("<KeyPress-j>")
            c.unbind_all("<KeyPress-o>")
            c.unbind_all("<KeyPress-l>")
            c.unbind_all("<KeyPress-0>")
            c.unbind_all("<KeyPress-1>")
            c.unbind_all("<KeyPress-2>")
            c.unbind_all("<KeyPress-3>")
            c.unbind_all("<KeyPress-4>")
            c.unbind_all("<KeyPress-5>")
            c.unbind_all("<KeyPress-6>")
            c.unbind_all("<KeyPress-z>")
            c.unbind_all("<KeyPress-c>")
            c.unbind_all("<KeyPress-e>")
            c.unbind_all("<KeyPress-q>")
            c.unbind_all("<Return>")
            c.unbind_all("<Control-s>")
            c.unbind_all("<Control-o>")
            c.unbind_all("<Control-h>")
            c.create_text(150,150,text="You Died",font=("Default",20),fill="#ff0000")
            break

def sb():
    start(1)

def sp():
    start(2)

c.delete("all")
logo = PhotoImage(file=f"{path}/explorers_bane/logo.png")
c.create_image(150,62,image=logo)
play = Button(tk,text="Play!",command=start,width=12,bg="#aa8800")
play.place(x=150,y=150,anchor=CENTER)
play_s = Button(tk,text="Sandbox Mode",command=sb,width=12,bg="#aa8800")
play_s.place(x=150,y=180,anchor=CENTER)
play_sp = Button(tk,text="Spectate Mode",command=sp,width=12,bg="#aa8800")
play_sp.place(x=150,y=210,anchor=CENTER)
cred = Button(tk,text="Credits",command=credits_,width=12,bg="#aa8800")
cred.place(x=150,y=240,anchor=CENTER)
c.create_text(127,280,text="Explorer's Bane v1.0.0-a2: Nighty Night Update",fill="#ffffff")
c.create_text(76,290,text="Created by UnbihexiumFan",fill="#ffffff")

while True:
    tk.geometry("304x304")
    tk.update()
