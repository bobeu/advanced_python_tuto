import os
import shutil

target = r"C:\Users\Dell\Desktop\backup"
source = r"C:\Users\Dell\Desktop\pbCore\PeerBrothers-core"

# Target main source at DESKTOP
def copy(currentDirectory, directoryToCopy, destination):
    dest = r"C:\Users\Dell\Documents" + destination
    os.chdir(r"C:\Users\Dell\Desktop" + currentDirectory)
    return shutil.copytree(directoryToCopy, dest)


p = copy("\pbCore", "PeerBrothers-core", "\pbcoreBackup")
print(p)
