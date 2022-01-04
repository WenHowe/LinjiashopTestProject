# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 08:32
# software: PyCharm
import yaml


class ReadYaml(object):
    def read_yaml(self):
        # 读取yaml数据文件
        yaml_file = open('../data/test_login.yaml', encoding='utf-8')
        data = yaml.load(yaml_file, yaml.FullLoader)
        yaml_file.close()
        # print(data)
        return data



# if __name__ == '__main__':
#     read_yaml = ReadYaml()
#     read_yaml.read_yaml()
