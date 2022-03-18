from report import NWPU_Yqtb_Site
import os


if __name__ == '__main__':
    username = os.getenv('NWPU_USERNAME')
    password = os.getenv('NWPU_PASSWORD')
    yqtb = NWPU_Yqtb_Site()
    yqtb.login(username, password)
    yqtb.init_info()
    yqtb.submit()
