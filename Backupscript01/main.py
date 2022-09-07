import os

dst = r"C:\DEST"
src = r"C:\SRC"

#de forskellige parametre efter XCOPY kan ændres alt efter hvordan man ønsker at tage sin backup
#der findes officiel dokumentation på XCOPY kommandoen fra microsoft
print (os.system("xcopy %s %s" % (src, dst)))