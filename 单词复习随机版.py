import random
def change_table(dictionary):
    """实现键与键值的交换"""
    key = list(dictionary)
    keyword= list(dictionary.values())
    dictionary=dict(zip(keyword,key))
    return dictionary
            
def randomly_review(dictionary):
        chinese = list(dictionary.values())#中文为键值，提取出来在一个列表中
        right_counts=0#记录正确的个数
        Loop_counts = random.choice(list(range(10,21)))#在10到21次之间循环
        index = random.sample(list(range(0,len(chinese))),Loop_counts)#产生随机且不重复的索引列表（产生随机）
        for i in range(0,Loop_counts):
            random_chinese=chinese[index[i]]
            print(random_chinese)
            answer = input("请输入你的答案:")
            change_dictionary = change_table(dictionary)
            if answer == change_dictionary[random_chinese]: #直接在字典中查找对应英文
                right_counts+=1
            else:
                print("答错了,正确答案是:")
                print(change_dictionary[random_chinese])
        print("您的正确率为:")
        print(right_counts/Loop_counts*100)
        print("%")
