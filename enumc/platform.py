from enum import Enum


class Platform(Enum):
    # 为序列值指定value值
    mini_program = 1
    admin_platform = 2


pf = Platform()

if __name__ == '__main__':
    Platform.mini_program
