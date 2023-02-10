import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\sadiq\\PycharmProjects\\ApoPro\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsermail():
        username = config.get('common info', 'Email')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
