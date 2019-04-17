# 复杂度是较高
def numJewelsInStones(J, S):
    J_length = len(J)
    S_length = len(S)
    if J_length > 50 or S_length > 50:
        print("字符长度超长")
    count = 0
    for s in S:
        if s in J:
            count = count + 1
    return count


print(numJewelsInStones("ba", "aAAbbbb"))


# 复杂度O(n)
def numJewelsInStones(J, S):
    stores = {}
    for c in S:
        if c in stores:
            stores[c] = stores[c] + 1
        else:
            stores[c] = 1

    count = 0
    for c in J:
        if c in stores:
            count += stores[c]
    print(count)


J = "aA"
S = "aAAbbbb"
numJewelsInStones(J, S)
J = "z"
S = "ZZ"
numJewelsInStones(J, S)
