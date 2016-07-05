#-------------------------------------------------------------------------------
# Name:         DirectorySearch.py
#
# Purpose:      List all files and folders in a directory and walks the user
#               through steps to open desired item.
#
# Author:       Brian Kingery
#
# Created:      4/4/2016
# Copyright:    (c) bkingery 2016
#
# Directions:   Enter information when prompted 
#-------------------------------------------------------------------------------

import os, sys, webbrowser

def ListFiles(asdf):
    global basePath
    global FileList
    global FolderList
    
    basePath = asdf
    try:
        files   = 0
        folders = 0
        FileList    = []
        FolderList  = []
        directory = os.listdir(basePath)
        print '\nDirectory:',basePath
        for x in directory:
            if os.path.isfile(os.path.join(basePath, x)) and (x[-2:] != 'db'):
                files +=1
                FileList.append(x)
            else:
                if os.path.isdir(os.path.join(basePath, x)) and (x[-3:] == 'gdb' or x[-3:] == 'sde'):
                    files +=1
                    FileList.append(x)
                elif os.path.isdir(os.path.join(basePath, x)):
                    folders +=1
                    FolderList.append(x)

        if files == 0 and folders == 0:
            print '\nThe folder is empty.'
            print 'Program Complete'
        else:
            print '\nFiles:  ', str(files)
            print 'Folders:', str(folders)

            if files > 0:
                FileList.sort()
                print '\n~~~~~~~~~~~~~~~~~~~~~~~~ Files ~~~~~~~~~~~~~~~~~~~~~~~~\n'
                for x in FileList:
                    print x

            if folders > 0:                  
                FolderList.sort()
                print '\n~~~~~~~~~~~~~~~~~~~~~~~ Folders ~~~~~~~~~~~~~~~~~~~~~~~\n'
                for y in FolderList:
                    print y
                print ''
                
            print '-'*30

            if files == 1:
                OpenFile()
            elif files > 1 and folders == 0:
                OpenFiles()
            elif files > 1 and folders >= 1:
                OpenFiles()

            if files == 0 and folders == 1:
                FolderBreakdown()
            elif files == 0 and folders > 1:
                BreakdownSubfolders()
            elif folders == 1 and openfile == 0:
                FolderBreakdown()
            elif folders > 1 and openfile == 0:
                BreakdownSubfolders()
    except:
        print '\nProgram Error\n\nDirectory does not exist\nOR\nAccess Denied\nOR\nDirectory was incorrectly entered. Try using forward slashes "/"\n','~'*30,'\n'
        directory = raw_input('Directory: ')
        ListFiles(directory)

def OpenFiles():
    global openfile            
    ask = raw_input('\nDo you want to open one of the files listed above? Yes or No: ')
    print ''
    if ask.lower() == 'y' or ask.lower() == 'yes':
        openfile = 1
        FileDict = {}
        print ''
        ID = 0
        for x in FileList:
            ## Add items from the sorted list to the dictionary in the format of #:item
            FileDict[str(ID)] = x
            ID+=1
        ## Print choices
        ID = 0
        while ID < len(FileDict):
            if ID < 10:
                print str(ID), '   --->', FileDict[str(ID)]
            if ID >= 10 and ID < 999:
                print str(ID), '  --->', FileDict[str(ID)]
            if ID >= 1000:
                print str(ID), ' --->', FileDict[str(ID)]
            ID+=1
        def OPEN():
            choice = raw_input('\nFile Number: ')
            try:
                if choice.lower() == 'exit':
                    print 'Program Complete'
                else:                        
                    folderChoice = FileDict[choice]
                    webbrowser.open((os.path.join(basePath, folderChoice)))
            except:
                print 'Enter a number that is listed or type "EXIT" to quit program.'
                OPEN()
        OPEN()
    elif ask.lower() == 'n' or ask.lower() == 'no':
        openfile = 0
        print 'Program Complete'
    else:
        openfile = 0

def BreakdownSubfolders():
    print ''
    FolderDict = {}
    ID = 0
    for y in FolderList:
        ## Add items from the sorted list to the dictionary in the format of #:item
        FolderDict[str(ID)] = y
        ID+=1
    ## Print choices
    ID = 0
    while ID < len(FolderDict):
        if ID < 10:
            print str(ID), '   ---> ', FolderDict[str(ID)]
        elif ID >= 10 and ID < 999:
            print str(ID), '  ---> ', FolderDict[str(ID)]
        elif ID >= 1000:
            print str(ID), ' ---> ', FolderDict[str(ID)]
        ID+=1
    def BREAKDOWN():
        choice = raw_input('\nFolder Number: ')
        try:
            if choice.lower() == 'exit':
                print 'Program Complete'
            else:
                folderChoice = FolderDict[choice]
                ListFiles(os.path.join(basePath, folderChoice))
        except:
            print 'Enter a number that is listed or type "EXIT" to quit program.'
            BREAKDOWN()                    
    BREAKDOWN()

def OpenFile():
    global openfile   
    ask = raw_input('\nDo you want to open the file listed above? Yes or No: ')
    if ask.lower() == 'y' or ask.lower() == 'yes':
        openfile = 1
        webbrowser.open((os.path.join(basePath, FileList[0])))
    elif ask.lower() == 'n' or ask.lower() == 'no':
        openfile = 0
        print 'Program Complete'
    else:
        openfile = 0

def FolderBreakdown():
    print '\nThere is only one folder to breakdown.\n'
    ListFiles(os.path.join(basePath, FolderList[0]))

def RUN():
    directory = raw_input('Enter Directory: ')
    ListFiles(directory)
    x = raw_input('Start another search? Yes or No: ')
    if x.lower() == 'y' or x.lower() == 'yes':
        RUN()
    else:
        print 'Program Complete'    
    
################################################################################
################################################################################
################################################################################

try:
    RUN()
except:
    print 'Program Error'
    
################################################################################
################################################################################
################################################################################
