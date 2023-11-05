# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 15:50:19 2022

@author: yinku
"""

import os 
#print(os.curdir)                                  # Check for the directory of the code
def get_files_path(extension = '.html'):            # For extensions with .txt file
    find_path = os.path.join(os.curdir, 'Practice')
    path_list = os.listdir(find_path)                       # To list the full files in a directory path
    # run a for loop to get a path for each of thr files
    files_full_path = [os.path.join(find_path, f) for f in path_list if f.endswith(extension)]  # if extensions ends with .txt file
    return files_full_path
print(get_files_path())