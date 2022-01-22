path = input("Please enter the file path for the explorers_bane folder. If you\
 are unsure that you have clicked on setup.py before, then click on main.py. If\
 Explorer's Bane is ready then you have clicked on setup.py before and don't\
 need to click on it again. Please enter the full file location: ")
a = open(f"{path}/explorers_bane/main.py")
b = a.read()
a.close()
c = open(f"{path}/explorers_bane/main.py","w")
c.write(f"path = \"{path}\"\n\n")
c.write(b)
