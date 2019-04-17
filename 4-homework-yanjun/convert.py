#z字形变换--
'''
L   C   I   R
E T O E S I I G
E   D   H   N
'''
def convert(s, numRows):

    rows = [''] * numRows
    #必须为False，否则数据越界，本来角标为len-1
    isInc = False
    curro = 0
    for c in s:
        rows[curro] += c
        if curro == 0 or curro == numRows - 1:
            isInc = not isInc
        if isInc:
            curro += 1
        else:
            curro -= 1
    return ''.join(rows)

print(convert("LEETCODEISHIRING",4))
print(convert("LEETCODEISHIRING",3))
#ok