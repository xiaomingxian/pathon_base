idList = []

print('*' * 30)
print("1.新建名片")
print("2.显示名片")
print('3.查询名片')
print("4.退出")
print("5.修改")
print('*' * 30)

while True:
    i = input('请输入你的选择:')
    if i == '1':
        name = input("name：")
        age = input("age：")
        sex = input("性别：")
        idList.append({'name': name, 'age': age, 'sex': sex})
    elif i == '2':
        if len(idList) == 0:
            print('当前数据库没有内容')
        else:
            print("name\tage\tsex")
            for id1 in idList:
                print(id1['name'],'\t',id1['age'],'\t',id1['sex'])
    elif i == '3':
        name = input('请输入你的姓名:')
        find=0
        for id2 in idList:
            if name==id2['name']:
                print(id2['name'], '\t', id2['age'], '\t', id2['sex'])
                find=1
        if find==0:
            print('您要查找的数据不存在。')

    elif i == '4':
        break
    elif i == '5':
        name = input('请输入你的姓名:')
        find = 0
        for id2 in idList:
            find=0
            if name == id2['name']:
                print(id2['name'], '\t', id2['age'], '\t', id2['sex'])
                age2=input("请输入age:")
                sex2=input("请输入sex:")
                id2['age']=age2
                id2['sex']=sex2
                print('修改成功')
                find=1
        if find == 0:
            print('您要查找的数据不存在。')

    else:
        print("您输入的指令有误请重新输入:")

