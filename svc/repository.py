import os
class InvalidRepo(Exception): 
    def __init__(self, errMsg):
        Exception.__init__(self,errMsg)
        self.message = errMsg

class Repo:
    def __init__(self,wd):
        if not os.path.exists(wd):
            raise InvalidRepo("Invalid Repo path")
        #creating required structure
        self.path = wd
        #create objects directory under.svcs directory
        os.makedirs(os.path.join(wd,".svcs","objects"))
        os.makedirs(os.path.join(wd,".svcs","tip"))
    def commit(self,commitMsg, userId, listOfFiles):
        """stre all the give files"""
        
        pass