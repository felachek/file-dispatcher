#!/usr/bin/python

import os
import shutil

# paths
downloadsPath = os.path.expanduser("~") + '/Downloads'
picturesPath = os.path.expanduser("~") + '/Pictures'
MusicPath = os.path.expanduser("~") + '/Music'
VideosPath = os.path.expanduser("~") + '/Videos'
documentsPath = os.path.expanduser("~") + '/Documents'
presentationsPath = documentsPath + '/Presentations'
spreadsheetsPath = documentsPath + '/Spreadsheets'
ebooksPath = documentsPath + '/Ebooks'
docsPath = documentsPath + '/Docs'
tempsPath = documentsPath + '/Temps'
# list to store files
files = []
# files extensions
fileTypes = {
    'Pictures': ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico', '.svg'),
    'Music': ('.mp3', '.wav'),
    'Videos': ('.mp4', '.mov'),
    'Documents/Fonts': ('.ttf', '.otf', '.woff', '.ufo'),
    'Documents/Presentations': ('.odp', '.ppt', '.pptx'),
    'Document/Spreadsheets': ('.csv', '.xls', '.xlsx', '.ods'),
    'Documents/Ebooks': ('.pdf', '.mobi', '.epub'),
    'Documents/Docs': ('.odt', '.doc', '.docx'),
    'Temps': ('.exe', '.iso', '.tmp', '.deb', '.bin', '.zip'),
}

def moveFileToDirectory(file):
    try:
        _, file_extension_found = os.path.splitext(file)
        for key in fileTypes:
            for file_extension_in_dict in fileTypes[key]:
                if file_extension_in_dict == file_extension_found:
                    oldPath = downloadsPath + '/' + file
                    newDir = os.path.expanduser("~") + '/' + key

                    if os.path.exists(newDir):
                        shutil.move(oldPath, newDir)
                    else:
                        os.mkdir(newDir)
                        shutil.move(oldPath, newDir)
    except FileNotFoundError:
        print("not found file: " + file)
    except:
        print("Something went wrong with this file: " + file)

# Iterate Downloads directory to get all files
for path in os.listdir(downloadsPath):
    # check if current path is a file
    try: 
        if os.path.isfile(os.path.join(downloadsPath, path)):
            files.append(path)
    except:
        print("Something went wrong with this path: " + path)

# Iterate all files to specific directory
for file in files:
    moveFileToDirectory(file)


