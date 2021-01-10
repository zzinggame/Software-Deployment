from Installation import *
from config import *

if ( Maya=='true' and CrackMaya == 'true' ):
    install_mayacrack()

if ( Maya == 'true' and CrackMaya != 'true' ):
    install_maya()

if ( Flux == 'true' ):
    install_flux()

if ( Zip == 'true' ):
    install_7zip()

if ( Bulk_Crap_Uninstaller == 'true' ):
    install_bcu()

if ( BleachBit == 'true' ):
    install_bleachbit()

if ( memreduct == 'true' ):
    install_memreduct()

if ( MicrosoftEdge == 'true' ):
    install_msedge()

if ( WindowsTerminal == 'true' ):
    install_terminal()

if ( Listary == 'true' ):
    install_listary()