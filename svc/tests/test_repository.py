import py
import os

from ..repository import Repo


def test_initrepo():
    """Testing Inilialization of repository"""
    curDir = "/tmp/test"
    repo.init(curDir)
