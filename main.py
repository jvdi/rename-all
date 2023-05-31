import os, glob, re
from .module import rename
from dotenv import load_dotenv

load_dotenv()

# Path
mypath = str(os.getenv('F_PATH'))

# Text for remove
text_for_remove = str(os.getenv('N_TEXT'))

# Tmp path
to_do_pth = [mypath]
    
rename()
# print(to_do_pth)