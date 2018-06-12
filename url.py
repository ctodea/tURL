#!/usr/bin/env python3
from pathlib import Path
import sys
import base64
class Url:
    
    #should be in external conf:
    DB_PATH = "./urls.db"

    def checkFile(self):
        db = Path(self.DB_PATH)
        if db.is_file(): return True
        else: return False


    #return false if no found, return line # if found
    def findInFile(self, file, target):
        with open(file) as myFile:
            for num, line in enumerate(myFile, 1):
                if target in line:
                    return num
        return False


    #empty file fails
    def getLastID(self):
        if self.checkFile() is True: 
            lastID = str(open(self.DB_PATH, "r").readlines()[-1]).split('\t',1)[0]
        return lastID
        
    
    #return ID of the url, False if not exists
    def getEntryID(self, url):
        currentEntry = self.findInFile(self.DB_PATH, url)
        if currentEntry is not False:
            return currentEntry
        else: 
            return False
        
    
    #writes and returns the base64(newID)
    def newUrl(self, url):
        nextEntryID = self.getEntryID(url)
        if nextEntryID is False:
            nextEntryID = int(self.getLastID()) + 1
            w = open(self.DB_PATH, "a")
            entry = str(nextEntryID) + "\t" + str(url) + "\n"
            w.write(entry)
            w.close()
        return base64.urlsafe_b64encode(str(nextEntryID).encode('ascii'))
        #print(newID)
