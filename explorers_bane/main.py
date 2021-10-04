from tkinter import *
import pickle

tk = Tk()
c = Canvas(tk, width=300, height=320, bg="#00ffff")
c.pack()

idmap = {
    0:("#00ff00","#00aa00","#008800"),
    1:("#664400","#443300","#332200"),
    2:("#555555","#444444","#333333"),
    3:("#aa8800","#886600","#554400"),
    4:("#00cc00","#009900","#006600"),
    }

def generate():
    c.delete("all")
    if yaw == 0:
        for z_ in range(z+3,z,-1):
            for x_ in range(x-1,x+2):
                for y_ in range(y,y+3):
                    try:
                        back = z_-z-1
                        xa = (x_-x+1)*100
                        ya = (-(y_-y)+2)*100
                        color = idmap[world[(x_,y_,z_)]][back]
                        c.create_rectangle(xa,ya,xa+100,ya+100,fill=color)
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
                        color = idmap[world[(z_,y_,x_)]][back]
                        c.create_rectangle(xa,ya,xa+100,ya+100,fill=color)
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
                        color = idmap[world[(z_,y_,x_)]][back]
                        c.create_rectangle(xa,ya,xa+100,ya+100,fill=color)
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
                        color = idmap[world[(x_,y_,z_)]][back]
                        c.create_rectangle(xa,ya,xa+100,ya+100,fill=color)
                    except:
                        pass
    if (x,y-1,z) in world:
        color = idmap[world[(x,y-1,z)]][back]
    else:
        color = "#00ffff"
    c.create_rectangle(0,300,300,320,fill=color)
    c.create_text(60,10,text="Explorer's Bane v0.0.0",fill="#ffffff")
    c.create_text(57,310,text="Press Ctrl-H for help",fill="#ffffff")

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
    if (x,y+2,z) not in world:
        y += 1

def down(event):
    global y
    if (x,y-1,z) not in world:
        y -= 1

def forth(event):
    global x
    global z
    if yaw == 0:
        if (x,y,z+1) not in world:
            z += 1
    elif yaw == 1:
        if (x+1,y,z) not in world:
            x += 1
    elif yaw == -1:
        if (x-1,y,z) not in world:
            x -= 1
    elif yaw == 2:
        if (x,y,z-1) not in world:
            z -= 1

def minef(event):
    global world
    if yaw == 0:
        if (x,y+1,z+1) in world:
            del world[(x,y+1,z+1)]
        elif (x,y+1,z+2) in world:
            del world[(x,y+1,z+2)]
        elif (x,y+1,z+3) in world:
            del world[(x,y+1,z+3)]
    elif yaw == 1:
        if (x+1,y+1,z) in world:
            del world[(x+1,y+1,z)]
        elif (x+2,y+1,z) in world:
            del world[(x+2,y+1,z)]
        elif (x+3,y+1,z) in world:
            del world[(x+3,y+1,z)]
    elif yaw == -1:
        if (x-1,y+1,z) in world:
            del world[(x-1,y+1,z)]
        elif (x-2,y+1,z) in world:
            del world[(x-2,y+1,z)]
        elif (x-3,y+1,z) in world:
            del world[(x-3,y+1,z)]
    elif yaw == 2:
        if (x,y+1,z-1) in world:
            del world[(x,y+1,z-1)]
        elif (x,y+1,z-2) in world:
            del world[(x,y+1,z-2)]
        elif (x,y+1,z-3) in world:
            del world[(x,y+1,z-3)]

def mineu(event):
    global world
    if (x,y+2,z) in world:
        del world[(x,y+2,z)]

def mined(event):
    global world
    if (x,y-1,z) in world:
        del world[(x,y-1,z)]

def placef(event):
    global world
    if yaw == 0:
        if (x,y+1,z+2) in world:
            world[(x,y+1,z+1)] = pbid
        elif (x,y+1,z+3) in world:
            world[(x,y+1,z+2)] = pbid
    elif yaw == 1:
        if (x+2,y+1,z) in world:
            world[(x+1,y+1,z)] = pbid
        elif (x+3,y+1,z) in world:
            world[(x+2,y+1,z)] = pbid
    elif yaw == -1:
        if (x-2,y+1,z) in world:
            world[(x-1,y+1,z)] = pbid
        elif (x-3,y+1,z) in world:
            world[(x-2,y+1,z)] = pbid
    elif yaw == 2:
        if (x,y+1,z-2) in world:
            world[(x,y+1,z-1)] = pbid
        elif (x,y+1,z-3) in world:
            world[(x,y+1,z-2)] = pbid

def placeu(event):
    if (x,y+2,z) not in world:
        world[(x,y+2,z)] = pbid

def placed(event):
    if (x,y-1,z) not in world:
        world[(x,y-1,z)] = pbid

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

def save(event):
    a = open("save/x.txt","w+b")
    a.write(pickle.dumps(x))
    a.close()
    a = open("save/y.txt","w+b")
    a.write(pickle.dumps(y))
    a.close()
    a = open("save/z.txt","w+b")
    a.write(pickle.dumps(z))
    a.close()
    a = open("save/yaw.txt","w+b")
    a.write(pickle.dumps(yaw))
    a.close()
    a = open("save/bx.txt","w+b")
    a.write(pickle.dumps(bx))
    a.close()
    a = open("save/by.txt","w+b")
    a.write(pickle.dumps(by))
    a.close()
    a = open("save/bz.txt","w+b")
    a.write(pickle.dumps(bz))
    a.close()
    a = open("save/byaw.txt","w+b")
    a.write(pickle.dumps(byaw))
    a.close()
    a = open("save/pbid.txt","w+b")
    a.write(pickle.dumps(pbid))
    a.close()
    a = open("save/world.txt","w+b")
    a.write(pickle.dumps(world))
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
    a = open("save/x.txt","rb")
    b = a.read()
    x = pickle.loads(b)
    a.close()
    a = open("save/y.txt","rb")
    b = a.read()
    y = pickle.loads(b)
    a.close()
    a = open("save/z.txt","rb")
    b = a.read()
    z = pickle.loads(b)
    a.close()
    a = open("save/yaw.txt","rb")
    b = a.read()
    yaw = pickle.loads(b)
    a.close()
    a = open("save/bx.txt","rb")
    b = a.read()
    bx = pickle.loads(b)
    a.close()
    a = open("save/by.txt","rb")
    b = a.read()
    by = pickle.loads(b)
    a.close()
    a = open("save/bz.txt","rb")
    b = a.read()
    bz = pickle.loads(b)
    a.close()
    a = open("save/byaw.txt","rb")
    b = a.read()
    byaw = pickle.loads(b)
    a.close()
    a = open("save/pbid.txt","rb")
    b = a.read()
    pbid = pickle.loads(b)
    a.close()
    a = open("save/world.txt","rb")
    b = a.read()
    world = pickle.loads(b)
    a.close()
    

def help_(event):
    i = Canvas(tk,width=300,height=170,bg="#000000")
    i.pack()
    i.create_text(150,10,text="Walk forward with W",fill="#ffffff")
    i.create_text(150,20,text="Move vertically with arrow keys",fill="#ffffff")
    i.create_text(150,30,text="Turn with A/D",fill="#ffffff")
    i.create_text(150,40,text="Mine with G",fill="#ffffff")
    i.create_text(150,50,text="Mine up/down with T/B",fill="#ffffff")
    i.create_text(150,60,text="Place with K",fill="#ffffff")
    i.create_text(150,70,text="Place up/down with I/M",fill="#ffffff")
    i.create_text(150,80,text="Pick block with L",fill="#ffffff")
    i.create_text(150,90,text="Make beacon with Z",fill="#ffffff")
    i.create_text(150,100,text="Go to beacon with C",fill="#ffffff")
    i.create_text(150,110,text="Save game with Ctrl-S",fill="#ffffff")
    i.create_text(150,120,text="Load game with Ctrl-O",fill="#ffffff")
    i.create_text(150,130,text="Pull up help section with Ctrl-H",fill="#ffffff")
    i.create_text(150,140,text="The nine squares in front of you are your vision",fill="#ffffff")
    i.create_text(150,150,text="They darken when they are farther away",fill="#ffffff")
    i.create_text(150,160,text="The long rectangle in front of you is the block under you",fill="#ffffff")

x = 0
y = 0
z = 0
yaw = 0
bx = 0
by = 0
bz = 0
byaw = 0
pbid = 1

add_text = ""

a = open("plain.txt")
world = eval(a.read())
a.close()

c.bind_all("<KeyPress-a>",left)
c.bind_all("<KeyPress-d>",right)
c.bind_all("<KeyPress-Down>",down)
c.bind_all("<KeyPress-Up>",up)
c.bind_all("<KeyPress-w>",forth)
c.bind_all("<KeyPress-g>",minef)
c.bind_all("<KeyPress-t>",mineu)
c.bind_all("<KeyPress-b>",mined)
c.bind_all("<KeyPress-k>",placef)
c.bind_all("<KeyPress-i>",placeu)
c.bind_all("<KeyPress-m>",placed)
c.bind_all("<KeyPress-l>",pickb)
c.bind_all("<KeyPress-z>",makebc)
c.bind_all("<KeyPress-c>",gotobc)
c.bind_all("<Control-s>",save)
c.bind_all("<Control-o>",load)
c.bind_all("<Control-h>",help_)

while True:
    tk.update()
    generate()
