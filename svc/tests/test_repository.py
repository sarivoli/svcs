import py
import os
import popen2
import shutil

from ..repository import Repo

def test_initrepo():
    """Testing Inilialization of repository"""
    curDir = "/tmp/test"
    #Check if the directory exists or not
    if os.path.exists(curDir):
        shutil.rmtree(curDir)
    os.mkdir(curDir)
    curRepo = Repo(curDir)
    
    #After initilizing the repo need to check repo structure
    assert os.path.exists(os.path.join(curDir , '.svcs','objects'))
    assert os.path.exists(os.path.join(curDir , '.svcs','TIP'))
    
def test_commit():
    """ Testing commit process"""
    curDir = "/tmp/test"
    #Check if the directory exists or not
    if os.path.exists(curDir):
        shutil.rmtree(curDir)
    os.mkdir(curDir)
    curRepo = Repo(curDir)
    fileName = "myfile.txt"
    userId = "sarivoli@zeomega.com"
    fd= open(os.path.join(curDir,fileName), "w")
    fd.write("This is a new content to commit")
    fd.close()
    latestCommitId = curRepo.commit("Committing a new file",userId,[fileName])
    assert os.path.exists(os.path.join(curDir,'.svcs','objects',latestCommitId))

def test_logs():
    """ Testing to get logs for a given repo"""
    curDir = "/tmp/test"
    #Check if the directory exists or not
    if not os.path.exists(curDir):
        os.mkdir(curDir)
    curRepo = Repo(curDir)
    
    #commit a new file
    fileName = "myfile1.txt"
    userId = "sarivoli@zeomega.com"
    commitMsg = "New File to commit"

    fd= open(os.path.join(curDir,fileName), "w")
    fd.write("This is a new content to commit to check log")
    fd.close()
    
    latestCommitId = curRepo.commit(commitMsg,userId,[fileName])

    logs = curRepo.getLogs()
    found = False
    for itm in logs:
        print itm.id + "   " + itm.message
        if itm.id ==latestCommitId:
            found=True
    assert found
        
    