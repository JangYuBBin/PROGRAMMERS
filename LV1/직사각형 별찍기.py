# 직사각형 별찍기

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(m):
    print("*" * n)
