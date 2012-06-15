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
            
        parent = self.storage.get_tip()
        if parent!=None:
            parent = parent.id
        comObj = Commit(userId,commitMsg, date,parent,files)
        self.storage.store_object(comObj)
        self.storage.update_tip(comObj)

        return latestCommitId
    def getLogs(self):
        """ Returns all log entry in the current repo"""
        currentTip = self.storage.get_tip()
        c = currentTip.id
        logs =[]
        while c!=None:
            c = self.storage.get_object(c)
            logs.append({"id":c.files[0][1],"committer":c.committer, "message":c.message})
            c = c.parent
            pass
        return logs
        
        
        
            
        