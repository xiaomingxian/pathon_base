import logging


def main():
    # 默认是  warning
    # 自己指定
    # logging.basicConfig(level=logging.INFO)

    # a 是追加  w是删了在写
    logging.basicConfig(level=logging.DEBUG, filename='./log.txt', filemode='a',
                        format='%(asctime)s-%(filename)s [line:%(lineno)d]-%(levelname)s: %(message)s')

    # 由低到高
    logging.debug('debug...')
    logging.info('info...')
    logging.warning('warning...')
    logging.error('error...')
    logging.critical('严重 critical ...')


if __name__ == '__main__':
    main()
