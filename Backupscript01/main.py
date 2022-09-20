import os
from datetime import datetime

#Source og destination for backup
dst = r"C:\Users\rueag\Desktop\DEST"
src = r"C:\Users\rueag\Desktop\SRC"

#Dags dato
Dato = datetime.today()
#Dags dato konverteret til string
Datostr = Dato.strftime("%d/%m/%Y, %H:%M:%S")

# Er det full-backupdag(tirsdag)? (0 = Man, 1 = Tir, 2 = Ons ...)
if datetime.today().weekday() == 1 or datetime.today().weekday() == 3:
    Backup_Type = "1"

#Hvis det ikke er tirsdag eller torsdag....
else:
    Backup_Type = "2"

#Full backup
if Backup_Type == "1":
    (os.system("xcopy %s %s /f /y" % (src, dst)))
    #Der føres en simpel log til en TXT fil på destinationen
    #Filen oprettes hvis den ikke allerede eksisterer
    f = open(r"C:\Users\rueag\Desktop\DEST\Backuplog.txt", "a")
    f.write("\nFull backup was performed ")
    f.write(Datostr)
    f.close()

#Differential backup
if Backup_Type == "2":
    (os.system("xcopy %s %s /f /y /d" % (src, dst)))
    f = open(r"C:\Users\rueag\Desktop\DEST\Backuplog.txt", "a")
    f.write("\nDifferential backup was performed ")
    f.write(Datostr)
    f.close()
