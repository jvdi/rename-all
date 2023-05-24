import os, glob, re
from dotenv import load_dotenv

load_dotenv()

# Path
mypath = str(os.getenv('F_PATH'))

# Text for remove
text_for_remove = str(os.getenv('N_TEXT'))

# Tmp path
to_do_pth = [mypath]

# Rename processing
def rename():
    for i in to_do_pth:
        # Set Directory
        os.chdir(i)
        FileAndFolderName = glob.glob('*')
        for name in FileAndFolderName:
            # print('Name is: '+name)
            sp_name = name.split()
            tmp_name = ''
            change = False
            for j in sp_name:
                if j == text_for_remove:
                    change = True
                elif re.search(text_for_remove, j):
                    change = True
                    text = j.replace(text_for_remove, '')
                    if tmp_name == '' or re.search(r".[\w]+$", text):
                        tmp_name = tmp_name+text
                    else:
                        tmp_name = tmp_name+' '+j.replace(text_for_remove, '')
                else:
                    if tmp_name == '':
                        tmp_name = tmp_name+j
                    else:
                        tmp_name = tmp_name+' '+j
            # Renaming process            
            if change == True:
                os.rename(name, tmp_name)
                print('Name: '+name+' -- Change to: '+tmp_name)
            ## else:
            ##     print('No change')
            # Check sub-folder
            path_for_check = str(i+tmp_name+'\\')
            if os.path.isdir(path_for_check):
                to_do_pth.append(path_for_check)
    
rename()
# print(to_do_pth)