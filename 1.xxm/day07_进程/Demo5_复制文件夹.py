import os, time
import multiprocessing


# 多任务拷贝文件夹
# 进程中产生-异常-不会报
def copy(filename, olddir, newdir, queue):
    '''复制文件'''
    time.sleep(1)
    try:
        # print(filename + '---' + olddir + "---" + newdir + '   进程号:' + str(os.getpid()))
        with open(olddir + '/' + filename, 'rb') as f:
            rr = f.read()
            ex=os.path.exists(newdir + "/" + filename)
            if not ex:
                print("文件不存在....")
                nf = open(newdir + "/" + filename, 'wb')
                nf.write(rr)
                queue.put(filename)
            else:
                print("文件存在....")
                if len(os.listdir(olddir))==len(os.listdir(newdir)):
                    queue.put(14)



    except Exception as e:
        print(e)


def main():
    # 读取原文件
    names = os.listdir("activeMq集群")
    # 创建同名文件
    try:
        os.makedirs("activeMq集群[附件]")
    except:
        # 如果已经存在再创建就会报错
        pass
    # 复制
    p = multiprocessing.Pool(3)
    queue = multiprocessing.Manager().Queue()

    for name in names:
        p.apply_async(copy, (name, 'activeMq集群', 'activeMq集群[附件]', queue))
    p.close()
    # p.join()
    # 显示进度--不关闭主线程---通过Queue
    x = 0
    while True:
        try:
            if x == len(names):
                print()
                print("文件夹拷贝完毕...")
                break

            qu = queue.get()
            if not qu==14:
                x += 1
                print("\r进度:%d  %0.2f %%" % (x, x * 100 / len(names)), end='')
            else:
                print('文件夹已经拷贝，请不要重复操作...')
                break


        except Exception as e:
            print("主线程异常:%s" % e)


if __name__ == '__main__':
    main()
