import os

class Repo:
    def __init__(self,wd):
        if not os.path.exists(wd):
            raise "Invalid Path"
        #creating required structure
        self.path = wd
        #create objects directory under.svcs directory
        os.makedirs(os.path.join(wd,".svcs","objects"))
        os.makedirs(os.path.join(wd,".svcs","tip"))

        pass