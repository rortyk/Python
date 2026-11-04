s = """\
AAA
BBB
CCC
DDD
"""
# with open('test.txt', 'w') as f:
#     f.write(s)
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')