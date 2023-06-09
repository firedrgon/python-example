# 一个列表中的元素还是列表
'''
# 一维列表
list1 = [12,3,56,68,46]
print(list1)  # [12, 3, 56, 68, 46]

# 二维列表
list2 = ['白酒','啤酒','红酒',['白兰地','人头马','威士忌','伏特加']]
print(list2)  # ['白酒', '啤酒', '红酒', ['白兰地', '人头马', '威士忌', '伏特加']]
print(list2[3][1])  # 人头马
'''
# 三维列表
list3 = ['白酒','啤酒','红酒',['白兰地','人头马','威士忌','伏特加',['百威','乌苏','大绿棒子']]]
print(list3[3][4][1])  # 乌苏