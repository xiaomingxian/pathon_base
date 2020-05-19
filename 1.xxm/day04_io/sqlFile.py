def m1():
    ff = open("C:/Users/xxm/Desktop/aioa_activiti_test.sql", 'r', encoding='UTF-8')
    insertFile = open('insertFile.sql', 'w', encoding='UTF-8')
    insertFile_act = open('act_insertFile.sql', 'w', encoding='UTF-8')
    constructFile = open('construct.sql', 'w', encoding='UTF-8')
    while True:

        oneLine = ff.readline()
        if oneLine:
            if oneLine.find('INSERT') >= 0:
                if oneLine.find('NSERT INTO `act_') >= 0:
                    insertFile_act.writelines(oneLine)
                    insertFile_act.flush()
                else:
                    insertFile.writelines(oneLine)
                    insertFile.flush()
            else:
                constructFile.writelines(oneLine)
                constructFile.flush()
        else:
            break
    insertFile.close()
    constructFile.close()
    insertFile_act.close()
    ff.close()


if __name__ == '__main__':
    m1()
