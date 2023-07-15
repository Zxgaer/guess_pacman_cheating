import os

# 匹配函数
def find_matching_packages(zxgaer_aishiteru_a, zxgaer_aishiteru_b):
    zxgaer_aishiteru_c = []
    for zxgaer_aishiteru_d in zxgaer_aishiteru_a:
        if len(zxgaer_aishiteru_d) == len(zxgaer_aishiteru_b):
            zxgaer_aishiteru_e = True
            for i in range(len(zxgaer_aishiteru_b)):
                if zxgaer_aishiteru_b[i] != '*' and zxgaer_aishiteru_b[i] != zxgaer_aishiteru_d[i]:
                    zxgaer_aishiteru_e = False
                    break
            if zxgaer_aishiteru_e:
                zxgaer_aishiteru_c.append(zxgaer_aishiteru_d)
    return zxgaer_aishiteru_c

# 用命令获取所有包，前提是系统为ArchLinux
zxgaer_aishiteru_f = os.popen('pacman -Ss | grep -oP "^[\w-]+/[\w-]+" | cut -d/ -f2').read().split('\n')

try:
    while True:
        # 获取用户输入内容
        zxgaer_aishiteru_g = input('Enter a package name with *:')
        # 查找匹配的软件包
        zxgaer_aishiteru_h = find_matching_packages(zxgaer_aishiteru_f, zxgaer_aishiteru_g)
        # 输出结果
        print(zxgaer_aishiteru_h)
except KeyboardInterrupt:
    # 退出
    print('\nGoodbye')
