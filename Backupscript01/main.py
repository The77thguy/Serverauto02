import os

SRC_Path = input('What Directory Do you Wish To backup?\n')
Backup_Type = input('Which Backup Type Would you like to perform?\n'
                    'Write 1 To Perform A Full Backup Of Your Selected Directory\n'
                    'Write 2 To Perform An Differential Backup\n')

dst = r"C:\DEST"
src = SRC_Path

#de forskellige parametre efter XCOPY kan ændres alt efter hvordan man ønsker at tage sin backup
#der findes officiel dokumentation på XCOPY kommandoen fra microsoft

if Backup_Type == "1":
    print (os.system("xcopy %s %s" % (src, dst)))

else: print("Does Not Compute Seymore")