import sys

sys.path.append("..")
import settings
from helper.singletons import *

@singleton
class SysConfig(object):

    def __init__(self):
        pass

    def getIpfsSources(self):
        return settings.ipfsSources
