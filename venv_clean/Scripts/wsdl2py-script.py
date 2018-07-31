#!C:\data\kronshtadt\QA\BL\AutomationFrameworkDesign\bl_frame_work\venv_clean\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'infi.ZSI==2.2.2','console_scripts','wsdl2py'
__requires__ = 'infi.ZSI==2.2.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('infi.ZSI==2.2.2', 'console_scripts', 'wsdl2py')()
    )
