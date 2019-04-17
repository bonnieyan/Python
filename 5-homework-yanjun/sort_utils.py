class SortUtils:
    def sort(self, f, s):
        if f == "bubble":
            #最好写成函数调用
            for i in range(len(s) - 1):
                for j in range(len(s) - i - 1):
                    if s[j] > s[j+1]:
                        s[j], s[j+1] = s[j+1], s[j]
                    print(s)
            #print(s)
        if f == "quick":
            #这里可以通过使用构造方法来处理 
            #如果使用这一调用方法里面的self就没有意义的 可以用静态装饰器
            SortUtils.__quick_sort(self, s, 0, len(s)-1)

    def __quick_sort(self, sort_list, start_index, end_index):
        # print(sort_list)
        if start_index < end_index:  # 如果角标左侧小于右侧则开始排序，否则退出
            basic, i, j = sort_list[start_index], start_index, end_index

            while i < j:  # 保证左侧的index一定比右侧的小

                while i < j and basic <= sort_list[j]:  # 基准值比j(右侧)小，那么该值不做任何运算
                    j -= 1  # 角标左移
                while i < j and basic >= sort_list[i]:  # 基准值比i(左侧)大，那么该值不做任何运算
                    i += 1  # 角标右移

                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
                print("i=" + str(i) + "&&&" + "j=" + str(j) + "$$$" + "sort_list=" + str(sort_list))

            sort_list[i], sort_list[start_index] = sort_list[start_index], sort_list[i]
            SortUtils.__quick_sort(self, sort_list, start_index, i - 1)
            SortUtils.__quick_sort(self, sort_list, i + 1, end_index)


p = SortUtils()
p.sort("bubble", [10, 5, 2, 16, 4, 9, 13, 8])
p.sort("quick", [10, 5, 2, 16, 4, 9, 13, 8])