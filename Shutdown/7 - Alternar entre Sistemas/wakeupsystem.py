import sys
import os

SystemFlag = sys.argv[1]

if SystemFlag == 'kodi'
	os.system("kodi-standalone")
elif SystemFlag == 'retropie'
	os.system("emulationstation")
else
	os.system("clear")
	print("Kodi/Retropie inativos.")