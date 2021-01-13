from pywinauto import Application, application, Desktop, keyboard, timings
import os, time, pywinauto, gdown, shutil, wget
from lastversion import lastversion

dsk=pywinauto.Desktop(backend='uia')
path=os.getcwd()
home = os.path.expanduser('~')
os.makedirs(rf"{home}\Desktop\ManualCrack", exist_ok=True)

def install_maya():
    timings.Timings.slow()
    gdown.download("https://drive.google.com/uc?export=download&id=1aegNaJNkPhueiSWu_JSOkDGwdDWsQZls", output=rf"{path}\software\Maya2020.4.7z")
    os.system('cls')
    os.system(rf"{path}\tools\7za.exe x {path}\software\Maya2020.4.7z -o{path}\software")
    os.system('cls')
    print('Installing Autodesk Maya 2020.....')
    os.system('".\\software\\Autodesk Maya 2020.4\\Setup.exe" --silent')
    Application(backend='uia').start("C:\\Program Files\\Autodesk\\Maya2020\\bin\\maya.exe")
    time.sleep(10)
    maya = Desktop(backend='uia').window(title="IE WebBrowser")
    maya.set_focus()
    maya.Hyperlink2.click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing")
    maya.set_focus()
    maya['I Agree Enter'].click_input()
    maya['Activate Enter'].click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activation Options") 
    maya.set_focus()
    maya.Edit1.click_input()
    maya.type_keys("666")
    maya.Edit2.click_input()
    maya.type_keys("69696969")
    maya.Next.click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activating")
    maya.set_focus()
    time.sleep(5)
    maya.Static12.click_input()
    maya['Yes Enter'].click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing")
    maya.set_focus()
    maya['Activate Enter'].click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activation Options")
    maya.set_focus()
    maya.Edit1.click_input()
    maya.type_keys("666")
    maya.Edit2.click_input()
    maya.type_keys("69696969")
    maya.Next.click_input()
    input("Please provide request code manually: ")
    Application(backend="uia").start(cmd_line='.\\software\\xf-adesk20_v2.exe')
    xforce = Desktop(backend='uia').window(title="Autodesk 2020 live Keymaker - X-FORCE")
    xforce.set_focus()
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
    maya.set_focus()
    maya['I have an activation code from Autodesk'].click_input()
    maya.Edit1.click_input()
    keyboard.send_keys("^v")
    maya.Next.click_input()
    maya = Desktop(backend='uia').window(title="Autodesk Licensing - Activation Complete")
    maya.FinishButton.click_input()
    time.sleep(3)
    os.system("TASKKILL /F /IM maya.exe")
    os.system('cls')

def install_flux():
    print('Installing f.lux.....')
    os.system("choco install f.lux -y")
    os.system("TASKKILL /F /IM flux.exe")
    os.system(rf"REG IMPORT {path}\software\flux_prefs.reg")
    os.system('cls')

def install_7zip():
    print('Installing 7zip.....')
    os.system("choco install 7zip.install -y")
    shutil.copy2(rf'{path}\software\config\7z.ico', 'C:\\Program Files\\7-Zip')
    shutil.copy2(rf'{path}\software\config\001.ico', 'C:\\Program Files\\7-Zip')
    os.system(rf"{path}\software\config\7zipassociate.bat")
    os.system("taskkill /im explorer.exe /F")
    os.system("start explorer.exe")
    os.system('cls')

def install_bcu():
    print('Installing Bulk Crap Uninstaller.....')
    os.system("choco install bulk-crap-uninstaller -y")
    os.system('cls')

def install_bleachbit():
    print('Installing BleachBit.....')
    os.system("choco install bleachbit -y")
    shutil.copyfile(os.path.join(rf'{path}\software\config', 'bleachbit.ini'), os.path.join(rf'{home}\AppData\Roaming\BleachBit', 'bleachbit.ini'))
    os.system('cls')

def install_memreduct():
    print('Installing MemReduct.....')
    os.system("choco install memreduct -y")
    shutil.copyfile(os.path.join(rf'{path}\software\config', 'memreduct.ini'), os.path.join(rf'{home}\AppData\Roaming\Henry++\Mem Reduct', 'memreduct.ini'))
    os.system('cls')

def install_msedge():
    print('Intalling Microsoft Edge.....')
    os.system("choco install microsoft-edge -y")
    os.system('cls')

def install_terminal():
    print('Installing Windows Terminal.....')
    os.system("choco install microsoft-windows-terminal -y")
    shutil.copyfile(os.path.join(rf'{path}\software\config', 'settings.json'), os.path.join(rf'{home}\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState', 'settings.json'))
    os.system('cls')

def install_listary():
    print('Installing Listary.....')
    wget.download("https://www.listary.com/download/beta/listary6/ListaryInstaller.exe", rf"{path}\software\ListaryInstaller.exe")
    os.system('".\\software\\ListaryInstaller.exe" /VERYSILENT /SUPPRESSMSGBOXES /NORESTART')
    os.system('cls')

def install_qbittorent():
    print('Installing Qbittorrent.....')
    os.system("choco install qbittorrent -y")
    os.system('cls')

def install_blender():
    print('Installing Blender.....\n\nWarning this is a Blender Launcher not actual Blender')
    blender = lastversion.latest("DotBow/Blender-Launcher", output_format='assets')
    wget.download(blender[0], rf"{path}\software\Blender_Laucher.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\Blender_Launcher.zip -o{path}\software")
    os.makedirs('C:\\Program Files\\Blender Launcher', exist_ok=True)
    shutil.copy2(rf'{path}\software\Blender Launcher.exe', 'C:\\Program Files\\Blender Launcher')
    os.system('cls')

def install_mactype():
    print('Installing Mactype.....')
    os.system('choco install mactype -y')
    os.system('cls')

def install_localeemulator():
    print('Installing Locale Emulator.....')
    os.system('choco install locale-emulator -y')
    os.system('cls')

def install_imageglass():
    print('Installing Image Glass.....')
    imageglass = lastversion.latest("d2phap/ImageGlass", output_format='assets', assets_filter='x64.msi')
    wget.download(imageglass[0], rf"{path}\software\ImageGlass_x64.msi")
    os.system(rf"{path}\software\ImageGlass_x64.msi /VERYSILENT")
    shutil.copy2(rf'{path}\software\config\igstartup.profile', 'C:\\Program Files\\ImageGlass')
    shutil.copy2(rf'{path}\software\config\igconfig.xml', 'C:\\Program Files\\ImageGlass')
    shutil.copytree(rf'{path}\software\config\Windows 10 Dark', 'C:\\Program Files\\ImageGlass\\Themes\\Windows 10 Dark', dirs_exist_ok=False)
    os.system('cls')

def install_youtubedl():
    print('Installing Youtube-DL.....')
    os.system('choco install youtube-dl -y')
    os.system('cls')

def install_vcredist():
    print('Installing Visual C++ Redistributable AIO.....')
    vcredist = lastversion.latest("abbodi1406/vcredist", output_format='assets')
    wget.download(vcredist[0], rf"{path}\software\vcredist-aio.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\vcredist-aio.zip -o{path}\software")
    os.system(rf"{path}\software\VisualCppRedist_AIO_x86_x64.exe /ai /gm2")
    os.system("taskkill /im explorer.exe /F")
    os.system("start explorer.exe")
    os.system('cls')

def install_teracopy():
    print('Installing Teracopy.....')
    os.system('choco install teracopy -y')
    os.system('cls')

def install_steam():
    print('Installing Steam.....')
    os.system('choco install steam -y')
    os.system('cls')

def install_teamviewer():
    print('Installing Teamviewer.....')
    os.system('choco install teamviewer -y')
    os.system('cls')

def install_ffmpeg():
    print('Installing FFmpeg.....')
    os.system('choco install ffmpeg -y')
    os.system('cls')

def install_sharex():
    print('Installing ShareX.....')
    os.system('choco install sharex -y')
    shutil.copy2(rf'{path}\software\ApplicationConfig.json', rf'{home}\Documents\ShareX')
    shutil.copy2(rf'{path}\software\HotkeysConfig.json', rf'{home}\Documents\ShareX')
    shutil.copy2(rf'{path}\software\UploadersConfig.json', rf'{home}\Documents\ShareX')
    os.system("taskkill /im ShareX.exe /F")
    os.system('cls')

def install_quicklook():
    print('Installing QuickLook.....')
    os.system('choco install quicklook -y')
    os.system('cls')

def install_obs():
    print('Installing OBS Studio.....')
    os.system('choco install obs-studio -y')
    os.system('cls')

def install_modernflyouts():
    print('Installing ModernFlyOuts.....')
    os.system('choco install modernflyouts -y')
    os.system('cls')

def install_mediainfo():
    print('Installing MediaInfo.....')
    os.system('choco install mediainfo -y')
    os.system('cls')

def install_eartrumpet():
    print('Installing EarTrumpet.....')
    os.system('choco install eartrumpet -y')
    os.system('cls')

def install_discord():
    print('Installing Discord.....')
    os.system('choco install eartrumpet -y')
    os.system("taskkill /im explorer.exe /F")
    os.system("start explorer.exe")
    os.system('cls')

def install_winauth():
    print('Installing WinAuth.....')
    wget.download('https://github.com/winauth/winauth/releases/download/3.6.2/WinAuth-3.6.2.zip', rf"{path}\software\WinAuth.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\WinAuth.zip -o{path}\software")
    os.makedirs('C:\\Program Files\\WinAuth', exist_ok=True)
    shutil.copy2(rf'{path}\software\WinAuth.exe', 'C:\\Program Files\\WinAuth')
    os.system('cls')

def install_taskbarx():
    print('Installing TaskbarX.....')
    taskbarx = lastversion.latest("ChrisAnd1998/TaskbarX", output_format='assets', assets_filter='x64.zip')
    wget.download(taskbarx[0], rf"{path}\software\TaskbarX.zip")
    os.system(rf'"{path}\tools\7za.exe x {path}\software\TaskbarX.zip -o"C:\Program Files\TaskBarX""')
    os.system('cls')

def install_davinciresolve():
    print('Installing Davinci Resolve 17.....')
    gdown.download("https://drive.google.com/uc?export=download&id=1ODF_0i6JZfHNIQ6Lng2Ht4mqa8R6vUjo", output=rf"{path}\software\DavinciResolve.7z")
    os.system(rf"{path}\tools\7za.exe x {path}\software\DavinciResolve.7z -o{path}\software")
    os.system(r'".\software\Blackmagic Design DaVinci Resolve Studio 17.0.0b.0018 Beta 6\DaVinci_Resolve_Studio_17.0b6_Windows.exe" /q')
    shutil.copyfile(os.path.join(rf'{path}\software\Blackmagic Design DaVinci Resolve Studio 17.0.0b.0018 Beta 6\Crack', 'fraunhoferdcp.dll'), os.path.join(r'C:\Program Files\Blackmagic Design\DaVinci Resolve', 'fraunhoferdcp.dll'))
    shutil.copyfile(os.path.join(rf'{path}\software\Blackmagic Design DaVinci Resolve Studio 17.0.0b.0018 Beta 6\Crack', 'Resolve.exe'), os.path.join(r'C:\Program Files\Blackmagic Design\DaVinci Resolve', 'Resolve.exe'))
    os.system('cls')

def install_qttabbar():
    print('Installing Qttabbar.....')
    wget.download('http://qttabbar.wdfiles.com/local--files/qttabbar1/QTTabBar_1043.zip', rf"{path}\software\QTTabBar.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\QTTabBar.zip -o{path}\software")
    os.system(rf"{path}\software\QTTabBar.exe /qi")
    qttabbar = False
    for win in Desktop(backend="uia").windows():
        if win.class_name() == "CabinetWClass":
            break
    else:
        qttabbar = True
        Application(backend="uia").start('explorer.exe')
        win = Desktop(backend="uia").window(class_name="CabinetWClass")
    win.set_focus()
    keyboard.send_keys("{VK_MENU}")
    keyboard.send_keys("{V}")
    time.sleep(0.5)
    keyboard.send_keys("{Y}")
    keyboard.send_keys("{DOWN}")
    keyboard.send_keys("{DOWN}")
    keyboard.send_keys("{DOWN}")
    keyboard.send_keys("{ENTER}")
    if qttabbar:
        win.close()
    os.system('cls')

def install_nuke():
    print('Installing Foundry Nuke.....')
    wget.download('https://www.foundry.com/products/download_product?file=Nuke-12.2v4-win-x86-64-installer.zip', rf"{path}\software\Nuke12.2v4.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\Nuke12.2v4.zip -o{path}\software")
    os.system('".\\software\\Nuke-12.2v4-win-x86-64-installer.exe" /S /ACCEPT-FOUNDRY-EULA')
    os.system('cls')

def install_mari():
    print('Installing Foundry Mari.....')
    wget.download('https://www.foundry.com/products/download_product?file=Mari4.7v1-win-x86-release-64.zip', rf"{path}\software\Mari4.7v1.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\Mari4.7v1.zip -o{path}\software")
    os.system('".\\software\\Mari4.7v1-win-x86-release-64.exe" /S')
    os.system('cls')

def install_foundrycrack():
    print('Patching Foundry Product.....')
    gdown.download("https://drive.google.com/uc?export=download&id=1J7-tfUVy2-CgBxwPEkHGkRMIf32NpEKm", output=rf"{path}\software\FoundryRLM.zip")
    os.system(rf'"{path}\tools\7za.exe x {path}\software\FoundryRLM.zip -o"{path}\software\FoundryRLM""')
    shutil.copytree(rf"{path}\software\FoundryRLM\RLM_Windows", r"C:\RLM_Windows")
    os.chdir(r"C:\RLM_Windows")
    os.system("rlm_install.cmd")
    os.system('cls')

def install_mpv():
    print('Installing mpv.....')
    os.system('choco install mpv -y')
    gdown.download("https://drive.google.com/uc?export=download&id=1DFygOXuNQfuLP2muQ6gnnh6r_KnJQF52", output=rf"{path}\software\mpv.7z")
    os.system(rf'"{path}\tools\7za.exe x {path}\software\mpv.7z -o"{path}\software\mpv""')
    shutil.copytree(rf"{path}\software\mpv", rf"{home}\AppData\Roaming\mpv", dirs_exist_ok=True)
    os.system('cls')

def install_zbrush():
    print('Installing Zbrush 2021.....')
    gdown.download("https://drive.google.com/uc?export=download&id=1uNOQhrOMJF9IRuf2AU-cVcavQssjw2Mc", output=rf"{path}\software\Zbrush2021.5.7z")
    os.system(rf"{path}\tools\7za.exe x {path}\software\Zbrush2021.5.7z -o{path}\software")
    os.system(rf'"{path}\software\Pixologic ZBrush 2021.5\ZBrush_2021.5_Full Installer.exe --mode unattended"')
    shutil.copy2(rf'{path}\software\Pixologic ZBrush 2021.5\ZBrush_2021.5_Updater for 2021.exe', 'C:\\Program Files\\Pixologic\\ZBrush 2021')
    os.chdir(r"C:\\Program Files\\Pixologic\\ZBrush 2021")
    os.system('""ZBrush_2021.5_Updater for 2021.exe" --mode unattended"')
    os.chdir(path)
    os.system(rf'"{path}\tools\7z.exe x -aoa "{path}\software\Pixologic ZBrush 2021.5\ZBrush 2021.5 CRACK.rar" -o"C:\Program Files\Pixologic\ZBrush 2021""')
    os.system('cls')

def install_houdini():
    print('Installing Houdini.....')
    gdown.download("https://drive.google.com/uc?export=download&id=1fD8vteczhZmfWSscOhXd6XSIv6WQBKa0", output=rf"{path}\software\Houdini_18.5.408.7z")
    os.system(rf"{path}\tools\7za.exe x {path}\software\Houdini_18.5.408.7z -o{path}\software")
    os.system(rf'""{path}\software\SideFX Houdini FX 18.5.408 Win x64\Houdini185408x64WinSetup.exe" /S /AcceptEULA=2020-05-05 /HoudiniServer=Yes /EngineMaya=Yes /EngineUnreal=Yes /HQueueServer=No /HQueueClient=No /IndustryFileAssociations=Yes /MainApp=Yes /Registry=Yes"')
    shutil.copy2(rf'{path}\software\SideFX Houdini FX 18.5.408 Win x64\Fix\Houdini-18.5-Keygen-Win.exe', rf'{home}\Desktop\Manual_Crack')
    os.system('cls')

def install_creativecloud():
    print('Installing Adobe Creative Cloud.....\n\nWarning: This installation need user input.....')
    wget.download('https://prod-rel-ffc-ccm.oobesaas.adobe.com/adobe-ffc-external/core/v1/wam/download?sapCode=KCCC&productName=Creative%20Cloud&os=win&environment=prod&api_key=CCHomeWeb1', rf"{path}\software\CreativeCloud.exe")
    os.system(rf'""{path}\software\CreativeCloud.exe" /quiet"')
    os.system('"TASKKILL /F /IM "Creative Cloud.exe""')
    gdown.download("https://drive.google.com/uc?export=download&id=1eBTzqQAWLS_OzqyG-O5MEDUDTh7O53hA", output=rf"{path}\software\GenP_2.7.zip")
    os.system(rf"{path}\tools\7za.exe x {path}\software\GenP_2.7.zip -o{home}\Desktop\Manual_Crack")
    os.system('cls')

def install_vscode():
    print('Installing Visual Studio Code.....')
    os.system('choco install vscode -y')
    os.system('cls')

def install_soulseek():
    print('Installing SoulSeek.....')
    os.system('choco install  soulseek -y')
    os.system('cls')