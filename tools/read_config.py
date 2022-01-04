# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 08:31
# software: PyCharm
import configparser


class ReadConfig(object):
    @staticmethod
    def read_config():
        # 创建读取config ini文件的对象
        conf = configparser.ConfigParser()
        # 读取config ini文件
        conf.read('../config/config.ini')
        url = conf.get('ENV', 'test_url')
        # print(url)
        return url


# if __name__ == '__main__':
#     readconfig = ReadConfig()
#     r = readconfig.read_config()
