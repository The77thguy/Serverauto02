import os
import pathlib
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)

dst = r"C:\Users\Dres\Desktop\Dest"

SRC_Path = input('What Directory Do you Wish To backup?\n')

sti = pathlib.Path(SRC_Path)
if sti.exists():
    print("\nA Valid Path Has Been Selected,\n")
    delay_print("Proceding..........\n")
else:
    print("Invalid Path Input")
    SRC_Path = input('What Directory Do you Wish To backup?\n')

Backup_Type = input('\nWhich Backup Type Would you like to perform?\n'
                    'Write 1 To Perform A Full Backup Of Your Selected Directory\n'
                    'Write 2 To Perform An Differential Backup\n')

if Backup_Type == "1":
    print("\nPerforming Full Backup Of Directory\n")
    delay_print("Proceeding..........\n")
    print(os.system("\nxcopy %s %s /f /y" % (SRC_Path, dst)))

if Backup_Type == "2":
    print("\nPerforming Differential Backup Of Directory\n")
    delay_print("Proceeding..........\n")
    print(os.system("\nxcopy %s %s /f /y /d" % (SRC_Path, dst)))

if Backup_Type == "1":
    forkert_indtastning1 = False
if Backup_Type != "1":
    forkert_indtastning1 = True

if Backup_Type == "2":
    forkert_indtastning2 = False
if Backup_Type != "2":
    forkert_indtastning2 = True

if forkert_indtastning1 == True and forkert_indtastning2 == True:
    print("no comprende")
    Backup_Type = input('Which Backup Type Would you like to perform?\n'
                        'Write 1 To Perform A Full Backup Of Your Selected Directory\n'
                        'Write 2 To Perform An Differential Backup\n')
    if Backup_Type == "1":
        print(os.system("xcopy %s %s /f /y" % (SRC_Path, dst)))

    if Backup_Type == "2":
        print(os.system("xcopy %s %s /f /y /d" % (SRC_Path, dst)))


