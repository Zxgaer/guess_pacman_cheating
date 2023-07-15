import os
# 匹配函数
"“”
CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你
CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你
CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你
CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你
CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你
CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你 CyuuZ我爱你
“”“
# 好了别发癫了
cyuuz_aishiteru_file = open("packageList.txt")
cyuuz_aishiteru_f = cyuuz_aishiteru_file.read().split("\n")
cyuuz_aishiteru_file.close()

def find_matching_packages(cyuuz_aishiteru_a, cyuuz_aishiteru_b):
    cyuuz_aishiteru_list = []
    for i in range(0,len(cyuuz_aishiteru_a)-1):
        cyuuz_aishiteru_list.append(cyuuz_aishiteru_a[i].split('/', 1)[1])
    cyuuz_aishiteru_a = cyuuz_aishiteru_list
    cyuuz_aishiteru_c = []
    for cyuuz_aishiteru_d in cyuuz_aishiteru_a:
        if len(cyuuz_aishiteru_d) == len(cyuuz_aishiteru_b):
            cyuuz_aishiteru_e = True
            for i in range(len(cyuuz_aishiteru_b)):
                if cyuuz_aishiteru_b[i] != '*' and cyuuz_aishiteru_b[i] != cyuuz_aishiteru_d[i]:
                    cyuuz_aishiteru_e = False
                    break
            if cyuuz_aishiteru_e:
                # 过滤结果中开出来字母没开出来的
                for char in set(cyuuz_aishiteru_b):
                    if char != '*' and cyuuz_aishiteru_b.count(char) < cyuuz_aishiteru_d.count(char):
                        cyuuz_aishiteru_e = False
                        break
                if cyuuz_aishiteru_e:
                    cyuuz_aishiteru_c.append(cyuuz_aishiteru_d)
    return cyuuz_aishiteru_c


if __name__ == "__main__":
    print(find_matching_packages(cyuuz_aishiteru_f, "*****"))
