import os
import datetime
from  storage import FileStorage,File,Commit
class InvalidRepo(Exception): pass        
class InvalidFile(IOError): pass
        
class Repo:
    def __init__(self, repoDir):
        if not os.path.exists(repoDir):
            raise InvalidRepo("Invalid Repo path")
        #creating required structure
        self.path = repoDir
        self.storage  = FileStorage(os.path.join(repoDir,".svcs"))
        #create objects directory under.svcs directory
        #os.makedirs(os.path.join(wd,".svcs","objects"))
        #os.makedirs(os.path.join(wd,".svcs","tip"))
        
        
    def commit(self,commitMsg, userId, listOfFiles):
        """stre all the give files"""
        latestCommitId =None
        date = datetime.datetime.utcnow().replace(microsecond = 0)
        #parent = None
        files =[]
        for itm in listOfFiles:
            filePath = os.path.join(self.path,itm)
            if not os.path.exists(filePath):
                raise InvalidFile
            
            fd= open(filePath, "r")
            fileObj =File(fd.read())
            self.storage.store_object(fileObj)
            fd.close()
            latestCommitId = fileObj.id
            files.append([itm,fileObj.id])
            
        parent = self.storage.tip
        if parent.find('TIP')>-1:
            parent=None
        comObj = Commit(userId,commitMsg, date,parent,files)
        self.storage.store_object(comObj)
        self.storage.update_tip(comObj)

        return latestCommitId
            
        