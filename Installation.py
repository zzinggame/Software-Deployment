from pywinauto import Application, application, Desktop, keyboard, mouse, timings
from config import *
import os, time, pywinauto, gdown, shutil

dsk=pywinauto.Desktop(backend='uia')
path=os.getcwd()
home = os.path.expanduser('~')

def install_mayacrack():
    gdown.download("https://drive.google.com/uc?export=download&id=1aegNaJNkPhueiSWu_JSOkDGwdDWsQZls", output=rf"{path}\software\Maya2020.4.7z")
    os.system('cls')
    os.system(rf"{path}\tools\7za.exe x {path}\software\Maya2020.4.7z -o{path}\software")
    os.system('cls')
    print('Installing Autodesk Maya 2020...')
    os.system('".\\software\\Autodesk Maya 2020.4\\Setup.exe" --silent')
    Application(backend='uia').start("C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe")
    time.sleep(10)
    maya = Desktop(backend='uia').window(title="IE WebBrowser")
    maya.Hyperlink2.click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing")
    maya['I Agree Enter'].click_input()
    maya['Activate Enter'].click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activation Options") 
    maya.Edit1.click_input()
    maya.type_keys("666")
    maya.Edit2.click_input()
    maya.type_keys("69696969")
    maya.Next.click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activating")
    time.sleep(5)
    maya.Static12.click_input()
    maya['Yes Enter'].click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing")
    maya['Activate Enter'].click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activation Options")
    maya.Edit1.click_input()
    maya.type_keys("666")
    maya.Edit2.click_input()
    maya.type_keys("69696969")
    maya.Next.click_input()
    input("Please provide request code manually: ")
    Application(backend="uia").start(cmd_line='.\\software\\xf-adesk20_v2.exe')
    xforce = Desktop(backend='uia').window(title="Autodesk 2020 live Keymaker - X-FORCE")
    xforce['Request :Edit'].click_input(button="right")
    dsk.Context.SelectAll.click_input()
    keyboard.send_keys("{VK_DELETE}")
    keyboard.send_keys("^v")
    xforce.CButton.click_input()
    xforce.OKButton.click_input()
    xforce.GButton.click_input()
    xforce['Activation :Edit'].click_input(button="right")
    dsk.Context.SelectAll.click_input()
    keyboard.send_keys("^c")
    os.system("TASKKILL /F /IM xf-adesk20_v2.exe")
    maya['I have an activation code from Autodesk'].click_input()
    maya.Edit1.click_input()
    keyboard.send_keys("^v")
    maya.Next.click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activation Complete")
    maya.FinishButton.click_input()
    time.sleep(3)
    os.system("TASKKILL /F /IM maya.exe")
    os.system('cls')

def install_maya():
    gdown.download("https://drive.google.com/uc?export=download&id=1aegNaJNkPhueiSWu_JSOkDGwdDWsQZls", output=rf"{path}\software\Maya2020.4.7z")
    os.system('cls')
    os.system(rf"{path}\tools\7za.exe x {path}\software\Maya2020.4.7z -o{path}\software")
    os.system('cls')
    print('Installing Autodesk Maya 2020...')
    os.system('".\\software\\Autodesk Maya 2020.4\\Setup.exe" --silent')
    os.system('cls')

def install_flux():
    print('Installing f.lux...')
    os.system("choco install f.lux -y")
    os.system("TASKKILL /F /IM flux.exe")
    os.system(rf"REG IMPORT {path}\software\flux_prefs.reg")
    os.system('cls')

def install_7zip():
    print('Installing 7zip...')
    os.system("choco install 7zip.install -y")
    os.system(rf"{path}\software\7zipassociate.bat")
    os.system('cls')

def install_bcu():
    print('Installing Bulk Crap Uninstaller...')
    os.system("choco install bulk-crap-uninstaller -y")
    os.system('cls')

def install_bleachbit():
    print('Installing BleachBit...')
    os.system("choco install bleachbit -y")
    os.system('cls')

def install_memreduct():
    print('Installing MemReduct...')
    os.system("choco install memreduct -y")
    shutil.copyfile(os.path.join(rf'{path}\software', 'memreduct.ini'), os.path.join(rf'{home}\AppData\Roaming\Henry++\Mem Reduct', 'memreduct.ini'))
    os.system('cls')

def install_msedge():
    print('Intalling Microsoft Edge...')
    os.system("choco install microsoft-edge -y")
    os.system('cls')

def install_terminal():
    print('Installing Windows Terminal')
    os.system("choco install microsoft-windows-terminal")
    os.system('cls')