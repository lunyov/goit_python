import os
import pathlib
from pathlib import Path
import os.path


categories = {'IMAGES':'JPEG, PNG, JPG, SVG','ARCHIVES':'ZIP, GZ, TAR','VIDEO':'AVI, MP4, MOV, MKV','MUSIC':'MP3, OGG, WAV, AMR','DOCUMENTS':'DOC, DOCX, TXT, PDF, XLSX, PPTX'}

def sort_catalog():
    directory = input('INPUT DIRECTORY NAME--->')
    for category in categories.keys():
        type_str= categories.get(category)
        print(category)
        print('------------------')
        type_list = list(type_str.split(", "))
        for ext in type_list:
            for txt_path in Path(directory).glob("**/*."+ext):
                    print(txt_path)
            
        print('----------------------------')     

### searching unknown extentions
    files_ext_list= []

    for category in categories.keys():
        
        type_str= categories.get(category)
        type_list= list(type_str.split(", "))

        for ext in type_list:
            files_ext_list.append(ext)
                

    directory_ext_list= []

    for txt_path in Path(directory).glob("**/*.*"):
        
        ext= os.path.splitext(txt_path)[1][1:].upper()    
        directory_ext_list.append(ext)
        all_ext_ist= set(directory_ext_list)
        all_ext_ist= list(all_ext_ist)

    unknown= []
    unknown= set(all_ext_ist) - set(files_ext_list)
    unknown= list(unknown)
    print('FILE TYPES',files_ext_list)
    print('----------------------------')
    print('FILE TYPES IN CATALOG',directory,'--->',files_ext_list)
    print('----------------------------')
    print('UNKNOWN FILE TYPES  ',unknown)
    print('----------------------------')







if __name__ == "__main__":

    
    
    sort_catalog()
