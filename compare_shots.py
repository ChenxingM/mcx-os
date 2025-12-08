# -*- coding: utf-8 -*-
"""
对比两个列表，找出差异
"""

# 第一个列表 (prores)
list1 = """MGJ_01,MGJ_01_006IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_01,MGJ_01_009IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_01,MGJ_01_011IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_01,MGJ_01_012IMAX_cmp_V8 | V8 | 1520x1064 | prores
MGJ_01,MGJ_01_014IMAX_cmp_V7 | V7 | 1520x1064 | prores
MGJ_01,MGJ_01_017IMAX_cmp_V12 | ? | ? | ?
MGJ_01,MGJ_01_020IMAX_cmp_V12 | V12 | 1520x1064 | prores
MGJ_01,MGJ_01_022IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_01,MGJ_01_024IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_01,MGJ_01_026IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_01,MGJ_01_027IMAX_cmp_V7 | ? | ? | ?
MGJ_01,MGJ_01_028IMAX_cmp_V8 | V8 | 1520x1064 | prores
MGJ_01,MGJ_01_034IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_01,MGJ_01_035IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_01,MGJ_01_036IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_01,MGJ_01_037IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_01,MGJ_01_038IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_01,MGJ_01_040IMAX_cmp_V7 | V7 | 1520x1064 | prores
MGJ_01,MGJ_01_041IMAX_cmp_V11 | V11 | 1520x1064 | prores
MGJ_01,MGJ_01_042IMAX_cmp_V1 | V1 | 1520x1064 | prores
MGJ_01,MGJ_01_044IMAX_cmp_V9 | V9 | 1520x1064 | prores
MGJ_01,MGJ_01_045IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_01,MGJ_01_051IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_01,MGJ_01_060IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_01,MGJ_01_066IMAX_cmp_V1 | V1 | 1520x1064 | prores
MGJ_01,MGJ_01_069IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_01,MGJ_01_070IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_01,MGJ_01_074IMAX_cmp_V14 | V14 | 1520x1064 | prores
MGJ_01,MGJ_01_075IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_01,MGJ_01_077IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_01,MGJ_01_079IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_01,MGJ_01_080IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_01,MGJ_01_096IMAX_cmp_V7 | V7 | 1520x1064 | prores
MGJ_01,MGJ_01_363IMAX_cmp_V8 | V8 | 1520x1064 | prores
MGJ_02,MGJ_02_096IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_02,MGJ_02_098IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_02,MGJ_02_118IMAX_cmp_V10 | V10 | 1520x1064 | prores
MGJ_02,MGJ_02_131IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_02,MGJ_02_133IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_02,MGJ_02_158IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_02,MGJ_02_161IMAX_cmp_V8 | V8 | 1520x1064 | prores
MGJ_02,MGJ_02_177IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_03,MGJ_03_146IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_03,MGJ_03_150IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_03,MGJ_03_169IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_03,MGJ_03_170IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_03,MGJ_03_171IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_03,MGJ_03_173IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_03,MGJ_03_174IMAX_cmp_V7 | ? | ? | ?
MGJ_03,MGJ_03_176IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_03,MGJ_03_178IMAX_cmp_V8 | V8 | 1520x1064 | prores
MGJ_03,MGJ_03_181IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_03,MGJ_03_183IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_03,MGJ_03_186IMAX_cmp_V7 | ? | ? | ?
MGJ_03,MGJ_03_187IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_03,MGJ_03_188IMAX_cmp_V4 | ? | ? | ?
MGJ_03,MGJ_03_189IMAX_cmp_V5 | V5 | 1520x1064 | prores
MGJ_03,MGJ_03_190IMAX_cmp_V2 | V2 | 1520x1064 | prores
MGJ_03,MGJ_03_290IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_03,MGJ_03_291IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_03,MGJ_03_301IMAX_cmp_V12 | V12 | 1520x1064 | prores
MGJ_04,MGJ_04_015IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_04,MGJ_04_022IMAX_cmp_V7 | V7 | 1520x1064 | prores
MGJ_04,MGJ_04_038IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_04,MGJ_04_131IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_04,MGJ_04_134IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_04,MGJ_04_135IMAX_cmp_V9 | V9 | 1520x1064 | prores
MGJ_04,MGJ_04_138IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_04,MGJ_04_148IMAX_cmp_V6 | ? | ? | ?
MGJ_04,MGJ_04_149IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_04,MGJ_04_156IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_04,MGJ_04_161IMAX_cmp_V9 | V9 | 1520x1064 | prores
MGJ_04,MGJ_04_164IMAX_cmp_V6 | V6 | 1520x1064 | prores
MGJ_04,MGJ_04_166IMAX_cmp_V4 | V4 | 1520x1064 | prores
MGJ_04,MGJ_04_174IMAX_cmp_V3 | V3 | 1520x1064 | prores
MGJ_04,MGJ_04_182IMAX_cmp_V9 | V9 | 1520x1064 | prores"""

# 第二个列表 (dnxhd)
list2 = """  MGJ_01,006IMAX | V3 | 1920x1080 | dnxhd
  MGJ_01,009IMAX | V5 | 1920x1080 | dnxhd
  MGJ_01,011IMAX | V2 | 1920x1080 | dnxhd
  MGJ_01,012IMAX | V8 | 1920x1080 | dnxhd
  MGJ_01,014IMAX | V7 | 1920x1080 | dnxhd
  MGJ_01,017IMAX | V12 | 1920x1080 | dnxhd
  MGJ_01,020IMAX | V12 | 1920x1080 | dnxhd
  MGJ_01,022IMAX | V3 | 1920x1080 | dnxhd
  MGJ_01,024IMAX | V2 | 1920x1080 | dnxhd
  MGJ_01,026IMAX | V5 | 1920x1080 | dnxhd
  MGJ_01,027IMAX | V7 | 1920x1080 | dnxhd
  MGJ_01,028IMAX | V8 | 1920x1080 | dnxhd
  MGJ_01,030IMAX | V7 | 1920x1080 | dnxhd
  MGJ_01,031IMAX | V13 | 1920x1080 | dnxhd
  MGJ_01,033IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,034IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,035IMAX | V6 | 1920x1080 | dnxhd
  MGJ_01,036IMAX | V3 | 1920x1080 | dnxhd
  MGJ_01,037IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,038IMAX | V6 | 1920x1080 | dnxhd
  MGJ_01,040IMAX | V7 | 1920x1080 | dnxhd
  MGJ_01,041IMAX | V11 | 1920x1080 | dnxhd
  MGJ_01,042IMAX | V1 | 1920x1080 | dnxhd
  MGJ_01,044IMAX | V9 | 1920x1080 | dnxhd
  MGJ_01,045IMAX | V3 | 1920x1080 | dnxhd
  MGJ_01,046IMAX | V2 | 1920x1080 | dnxhd
  MGJ_01,050IMAX | V6 | 1920x1080 | dnxhd
  MGJ_01,051IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,056IMAX | V10 | 1920x1080 | dnxhd
  MGJ_01,060IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,066IMAX | V1 | 1920x1080 | dnxhd
  MGJ_01,069IMAX | V3 | 1920x1080 | dnxhd
  MGJ_01,070IMAX | V2 | 1920x1080 | dnxhd
  MGJ_01,074IMAX | V14 | 1920x1080 | dnxhd
  MGJ_01,075IMAX | V3 | 1920x1080 | dnxhd
  MGJ_01,077IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,079IMAX | V5 | 1920x1080 | dnxhd
  MGJ_01,080IMAX | V2 | 1920x1080 | dnxhd
  MGJ_01,096IMAX | V7 | 1920x1080 | dnxhd
  MGJ_01,098IMAX | V6 | 1920x1080 | dnxhd
  MGJ_01,338IMAX | V4 | 1920x1080 | dnxhd
  MGJ_01,345IMAX | V9 | 1920x1080 | dnxhd
  MGJ_01,363IMAX | V8 | 1920x1080 | dnxhd
  MGJ_02,096IMAX | V5 | 1920x1080 | dnxhd
  MGJ_02,098IMAX | V5 | 1920x1080 | dnxhd
  MGJ_02,118IMAX | V10 | 1920x1080 | dnxhd
  MGJ_02,131IMAX | V4 | 1920x1080 | dnxhd
  MGJ_02,133IMAX | V4 | 1920x1080 | dnxhd
  MGJ_02,158IMAX | V5 | 1920x1080 | dnxhd
  MGJ_02,161IMAX | V8 | 1920x1080 | dnxhd
  MGJ_02,162IMAX | V6 | 1920x1080 | dnxhd
  MGJ_02,187IMAX | V2 | 1920x1080 | dnxhd
  MGJ_02,190IMAX | V4 | 1920x1080 | dnxhd
  MGJ_02,191IMAX | V2 | 1920x1080 | dnxhd
  MGJ_02,238IMAX | V4 | 1920x1080 | dnxhd
  MGJ_03,146IMAX | V4 | 1920x1080 | dnxhd
  MGJ_03,150IMAX | V3 | 1920x1080 | dnxhd
  MGJ_03,169IMAX | V3 | 1920x1080 | dnxhd
  MGJ_03,170IMAX | V2 | 1920x1080 | dnxhd
  MGJ_03,171IMAX | V3 | 1920x1080 | dnxhd
  MGJ_03,173IMAX | V2 | 1920x1080 | dnxhd
  MGJ_03,174IMAX | V7 | 1920x1080 | dnxhd
  MGJ_03,176IMAX | V6 | 1920x1080 | dnxhd
  MGJ_03,177IMAX | V9 | 1920x1080 | dnxhd
  MGJ_03,178IMAX | V8 | 1920x1080 | dnxhd
  MGJ_03,181IMAX | V3 | 1920x1080 | dnxhd
  MGJ_03,183IMAX | V4 | 1920x1080 | dnxhd
  MGJ_03,186IMAX | V7 | 1920x1080 | dnxhd
  MGJ_03,187IMAX | V4 | 1920x1080 | dnxhd
  MGJ_03,188IMAX | V4 | 1920x1080 | dnxhd
  MGJ_03,189IMAX | V5 | 1920x1080 | dnxhd
  MGJ_03,190IMAX | V2 | 1920x1080 | dnxhd
  MGJ_03,290IMAX | V4 | 1920x1080 | dnxhd
  MGJ_03,291IMAX | V3 | 1920x1080 | dnxhd
  MGJ_03,293IMAX | V5 | 1920x1080 | dnxhd
  MGJ_03,296IMAX | V2 | 1920x1080 | dnxhd
  MGJ_03,297IMAX | V3 | 1920x1080 | dnxhd
  MGJ_03,299IMAX | V6 | 1920x1080 | dnxhd
  MGJ_03,300IMAX | V6 | 1920x1080 | dnxhd
  MGJ_03,301IMAX | V12 | 1920x1080 | dnxhd
  MGJ_03,302IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,001IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,002IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,003IMAX | V4 | 1920x1080 | dnxhd
  MGJ_04,004IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,005IMAX | V7 | 1920x1080 | dnxhd
  MGJ_04,006IMAX | V4 | 1920x1080 | dnxhd
  MGJ_04,007IMAX | V2 | 1920x1080 | dnxhd
  MGJ_04,008IMAX | V2 | 1920x1080 | dnxhd
  MGJ_04,009IMAX | V8 | 1920x1080 | dnxhd
  MGJ_04,011IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,015IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,016IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,022IMAX | V7 | 1920x1080 | dnxhd
  MGJ_04,038IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,057IMAX | V2 | 1920x1080 | dnxhd
  MGJ_04,058IMAX | V4 | 1920x1080 | dnxhd
  MGJ_04,062IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,063IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,131IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,134IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,135IMAX | V9 | 1920x1080 | dnxhd
  MGJ_04,137IMAX | V4 | 1920x1080 | dnxhd
  MGJ_04,138IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,142IMAX | V13 | 1920x1080 | dnxhd
  MGJ_04,143IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,144IMAX | V2 | 1920x1080 | dnxhd
  MGJ_04,145IMAX | V12 | 1920x1080 | dnxhd
  MGJ_04,146IMAX | V10 | 1920x1080 | dnxhd
  MGJ_04,148IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,149IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,154IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,161IMAX | V9 | 1920x1080 | dnxhd
  MGJ_04,164IMAX | V6 | 1920x1080 | dnxhd
  MGJ_04,166IMAX | V4 | 1920x1080 | dnxhd
  MGJ_04,171IMAX | V8 | 1920x1080 | dnxhd
  MGJ_04,172IMAX | V7 | 1920x1080 | dnxhd
  MGJ_04,173IMAX | V2 | 1920x1080 | dnxhd
  MGJ_04,174IMAX | V3 | 1920x1080 | dnxhd
  MGJ_04,181IMAX | V11 | 1920x1080 | dnxhd
  MGJ_04,182IMAX | V9 | 1920x1080 | dnxhd
  MGJ_04,183IMAX | V5 | 1920x1080 | dnxhd
  MGJ_04,188IMAX | V4 | 1920x1080 | dnxhd
  MGJ_04,191IMAX | V8 | 1920x1080 | dnxhd
  MGJ_04,193IMAX | V12 | 1920x1080 | dnxhd
  MGJ_04,194IMAX | V7 | 1920x1080 | dnxhd
  MGJ_05,142IMAX | V17 | 1920x1080 | dnxhd
  MGJ_06,163IMAX | V6 | 1920x1080 | dnxhd
  MGJ_07,735IMAX | V6 | 1920x1080 | dnxhd
  MGJ_07,762IMAX | V1 | 1920x1080 | dnxhd
  MGJ_07,789IMAX | V6 | 1920x1080 | dnxhd
  MGJ_07,793IMAX | V1 | 1920x1080 | dnxhd"""

import re

def parse_list1(text):
    """解析prores列表，提取 MGJ_XX + 镜头号IMAX + 版本号"""
    items = set()
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        # 格式: MGJ_01,MGJ_01_006IMAX_cmp_V3 | V3 | ...
        parts = line.split(',')
        if len(parts) >= 2:
            mgj = parts[0].strip()
            # 从第二部分提取镜头号和版本
            rest = parts[1].split('|')[0].strip()
            # MGJ_01_006IMAX_cmp_V3 -> 提取 006IMAX 和 V3
            match = re.search(r'_(\d+IMAX)_cmp_(V\d+)', rest)
            if match:
                shot = match.group(1)
                version = match.group(2)
                items.add((mgj, shot, version))
    return items

def parse_list2(text):
    """解析dnxhd列表，提取 MGJ_XX + 镜头号IMAX + 版本号"""
    items = set()
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        # 格式: MGJ_01,006IMAX | V3 | ...
        parts = line.split(',')
        if len(parts) >= 2:
            mgj = parts[0].strip()
            rest = parts[1].split('|')
            if len(rest) >= 2:
                shot = rest[0].strip()
                version = rest[1].strip()
                items.add((mgj, shot, version))
    return items

# 解析两个列表
set1 = parse_list1(list1)
set2 = parse_list2(list2)

# 找出共同的项目
common = set1 & set2

# 只在list1中的（prores有，dnxhd没有）
only_in_list1 = set1 - set2

# 只在list2中的（dnxhd有，prores没有）
only_in_list2 = set2 - set1

print("="*60)
print(f"列表1 (prores) 总数: {len(set1)}")
print(f"列表2 (dnxhd) 总数: {len(set2)}")
print(f"共同项目数: {len(common)}")
print("="*60)

print(f"\n只在 prores 中 (共 {len(only_in_list1)} 个):")
for item in sorted(only_in_list1):
    print(f"  {item[0]},{item[1]} | {item[2]}")

print(f"\n只在 dnxhd 中 (共 {len(only_in_list2)} 个):")
for item in sorted(only_in_list2):
    print(f"  {item[0]},{item[1]} | {item[2]}")
