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