@echo off
echo Alyssa Software Deployment
echo .
echo Ensure your running cmd in Administrator
echo .
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
choco feature enable -n=allowGlobalConfirmation
cls
choco install python -y
cls
call refreshenv
cls
pip install -r requirements.txt --user
cls
python Install.py