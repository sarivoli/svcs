import py
import os
import shutil

from ..repository import Repo

def test_initrepo():
    """Testing Inilialization of repository"""
    curDir = "/tmp/test"
    #Check if the directory exists or not
    if os.path.exists(curDir):
        shutil.rmtree(curDir)
    curRepo = Repo(curDir)
    
    #After initilizing the repo need to check repo structure
    assert os.path.exists(os.path.join(curDir , '.svc','objects'))
    
