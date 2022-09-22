import sys

sys.path.append("..")
import settings
from helper.singletons import *

class SysConfig(metaclass=SingletonMeta):

    def __init__(self):
        pass

    def getIpfsSources(self):
        return settings.ipfsSources
