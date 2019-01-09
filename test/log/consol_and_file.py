import logging


def main():
    log = logging.getLogger()
    log.setLevel(logging.INFO)  # 总级别设置

    # 创建handler保存本地设置
    logfile = './b.txt'
    flog = logging.FileHandler(logfile, mode='a')
    flog.setLevel(logging.DEBUG)  # 输出到文件的 级别

    # 创建 控制台 handler
    cos = logging.StreamHandler()
    cos.setLevel(logging.DEBUG)

    # 定义handler输出格式---并添加到flog 和 cos
    ft = logging.Formatter('%(asctime)s-%(filename)s [line:%(lineno)d]-%(levelname)s')
    flog.setFormatter(ft)
    cos.setFormatter(ft)

    # log 对象添加 flog和cos对象
    log.addHandler(flog)
    log.addHandler(cos)

    # 日志
    log.debug('deubg msg ...')
    log.info('info msg ...')
    log.warning('warning msg ...')
    log.error('error msg ...')
    log.critical('critical msg ...')


if __name__ == '__main__':
    main()
