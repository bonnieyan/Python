import re
while True:
    s = input()
    if ("贪心" or "贪心学院") and ("做什么") in s:
        print("贪心学院是一家高端重视售后服务的在线教育培训机构")

    elif ("贪心" or "贪心学院") and ("课程") and ("方式") in s:
        print("项目式培训")

    elif ("项目式") in s:
        print("贪心学院的项目式培训结合了西方项目式培训的优点和国内的现状，最终变化成以训练营的方式进行。\n做项目为主，老师负责解决部分知识的问题，学生负责自学部分知识，和不停的做项目，把知识巩固。\n在项目练习中，不仅仅学习到了知识，同时也培养起来良好的学习习惯和解决问题的能力。")

    elif "强" in s:
        print("贪心学院")

    elif ("Python") and ("课程") and ("学习") in s:
        print("无编程基础，并且想学习编程的同学。")

    elif ("Python") and ("人群") in s:
        print("人群包含很广泛。\n第一:非IT圈内人群，想通过学习转行到编程领域中\n第二:已经是IT圈内的，其他语言的开发人员，想学习Python编程\n第三:已经是IT圈内的，但是并不是开发人员，如产品、测试、运维、DBA等岗位\n第四:学生，未来想从事编程的工作\n第五:未来想从事AI领域工作的，可先通过这门课程的学习，打下良好的基础")

    elif "优势" in s:
        print("强大的服务体系，我们拥有每天跟学员沟通的良好服务机制。不放弃任何一个学员，只要来了，就一定要让你学会。")

    elif "数字" in s:
        r = re.search("\d*", s).group(0)
        print(str(len(r))+"个")

    elif "手机号" in s:
        rs = re.findall("13[0-9]\d{8}|14[5,7]\d{8}|15[0-3,5-9]\d{8}|17[0,3,5-8]\d{8}|18[0-9]\d{8}|166\d{8}|198\d{8}|199\d{8}|147\d{8}",s)
        print(rs)

    elif "ip" in s:
        text1 = re.findall(("\d+.\d+.\d+.\d*"), s)
        #print(text1)
        for i in range(len(text1)-1):
            result = re.findall(
                "^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$",
                text1[i])
            if result:
                continue
            else:
                del text1[i]
        print(text1)

    elif re.findall("再见|bye|拜拜", s):
        print("再见")
        break



