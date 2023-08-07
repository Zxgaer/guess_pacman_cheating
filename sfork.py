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
                # 过滤结果中开出来字母没开出来的
                for char in set(zxgaer_aishiteru_b):
                    if char != '*' and zxgaer_aishiteru_b.count(char) < zxgaer_aishiteru_d.count(char):
                        zxgaer_aishiteru_e = False
                        break
                if zxgaer_aishiteru_e:
                    zxgaer_aishiteru_c.append(zxgaer_aishiteru_d)
    return zxgaer_aishiteru_c



zxgaer_aishiteru_f = os.popen('type test.txt | grep -oP "^[\w-]+/[\w-]+" | cut -d/ -f2').read().split('\n')

try:
    while True:
        # 获取用户输入内容
        zxgaer_aishiteru_g = input('请您输入捏:')
        # 查找匹配的软件包
        zxgaer_aishiteru_h = find_matching_packages(zxgaer_aishiteru_f, zxgaer_aishiteru_g)
        # 输出结果
        print(zxgaer_aishiteru_h)
except KeyboardInterrupt:
    # 退出
    print('\n拜拜')