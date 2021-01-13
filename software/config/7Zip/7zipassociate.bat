@echo off
SETLOCAL
SET SC=HKLM\SOFTWARE\Classes
SET Extn=7z arj bz2 bzip2 cab cpio deb dmg gz gzip hfs iso lha lzh lzma rar rpm split swm tar taz tbz tbz2 tgz tpz wim xar z zip
FOR %%j IN (%Extn%) DO >nul (
	REG ADD %SC%\.%%j /VE /D "7-Zip.%%j" /F
	REG ADD %SC%\7-Zip.%%j /VE /D "7z Archive" /F
	REG ADD %SC%\7-Zip.%%j\DefaultIcon /VE /D "\"%PROGRAMFILES%\7-Zip\7z.ico"" /F
	REG ADD %SC%\7-Zip.%%j\shell\open\command /VE /D "\"%PROGRAMFILES%\7-Zip\7zFM.exe\" \"%%1\"" /F
)
REG ADD >nul %SC%\7-Zip.001\DefaultIcon /VE /D "\"%PROGRAMFILES%\7-Zip\001.ico"" /F
ENDLOCAL