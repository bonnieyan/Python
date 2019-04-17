words = ["gin", "zen", "gig", "msg"]
mima = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
        "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-",
        "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
word = ""
list_code = []
count = 0
# 外层循环获取字符gin
for i in words:
    # 内层循环获取字母对应的摩斯密码
    for j in i:
        word += mima[j]
    # 将对应字符gin的摩斯密码组合放入s
    s = word
    if s not in list_code:
        count += 1
        # 将不一样的摩斯密码组合放入list_code
        list_code.append(s)
    # 清空组合的摩斯密码以便外层循环存放新的摩斯密码
    word = ""
print(count)
print(list_code)






morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

# 根据ascii 小写97 a 开始创建字典
morse_dict = {chr(i + 97): morse[i] for i in range(0, len(morse))}


def uniqueMorseRepresentations(words):
    # 使用set 用来去重
    unique = set()
    for word in words:
        unique.add(toMorseCode(word))
    return len(unique)


def toMorseCode(word):
    morse_code = ""
    for char in word.lower():
        morse_code += morse_dict.get(char)
    return morse_code


check_words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(check_words))
