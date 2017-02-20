#-*- coding:utf8 -*-
import ConfigParser

class Conf(object):

    def __init__(self, file_path):
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read(file_path)


    def get(self, section, option):
        result = ""
        try:
            result = self.cfg.get(section, option)
        except:
            result = ""
        return result



conf = Conf("conf.ini")
