#SET THIS TO ALL YOUR INSTANCE DIRECTORIES
dir_paths = ["C:\\MultiMC\\instances\\1.16.1_i1\\.minecraft\\saves", "C:\\MultiMC\\instances\\1.16.1_i2\\.minecraft\\saves", "C:\\MultiMC\\instances\\1.16.1_i3\\.minecraft\\saves", "C:\\MultiMC\\instances\\1.16.1_i4\\.minecraft\\saves"]
#SET THIS TO ALL YOUR INSTANCE DIRECTORIES

#if you're using some mod that doesn't use Random Speedrun as the world name, set this to whatever it uses
world_name_start = "Random Speedrun"

from pathlib import Path
import shutil
import os
from time import sleep

a = 0
wc = 0
total = 0
worlds = []

for i in dir_paths:
    count = 0
    for path in os.listdir(dir_paths[a]): #loop through all folders
        if path.replace(f"{dir_paths[a]}\\", "").startswith(world_name_start):
            count += 1
    print(str(count) + " Folders found in " + dir_paths[a])
    worlds.append(count) #used in line 32 to check if folder is empty and line 42 to see progress
    a = a + 1 #next folder

a = 0 #reset to use again to loop through folders
input("Press Enter to start deleting worlds")
os.system("cls")
for i in dir_paths:
    if worlds[a] != 0: #if the current saves folder isn't empty
        print("Deleting from:", dir_paths[a])
        sleep(3)
    else:
        print(dir_paths[a] + " is empty, skipping...") #go next if it's empty

    files = Path(dir_paths[a]).glob('*') #set path (entire saves folder of an instance)
    for file in files: #loop through folders one by one
        if str(file).replace(f"{dir_paths[a]}\\", "").startswith(world_name_start):
            shutil.rmtree(str(file)) #delete file if it starts with world_name_start (set to Random Speedrun by default)
            wc = wc + 1 #worlds deleted in this instance
            print("Deleted " + str(file) + f" ({str(wc)}/{str(worlds[a])})") #print folder path and progress
            total = total + 1 #total worlds deleted
    wc = 0 #reset worlds deleted in this instance
    a = a + 1 #next folder

input("\nDone! Deleted " + str(total) + " worlds :)")