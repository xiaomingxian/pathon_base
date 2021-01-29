from urllib.request import urlretrieve
from queue import Queue
import threading
import os

SAVE_DIR_PATH = 'C:\\Users\\仙\\Desktop\\2'


def prepare_links():
    queue = Queue()
    with open('C:\\Users\\仙\\Desktop\\1\\links_pure.txt', 'r') as infile:
        for line in infile.readlines():
            queue.put(line)
    print('共有链接', queue.qsize(), '个')
    return queue


def download(queue):
    while not queue.empty():
        url = queue.get()
        url = url.strip()
        if url != '' and url is not None:
            file_path_name = os.path.join(SAVE_DIR_PATH, url.split('/')[-1])
            if os.path.exists(file_path_name):
                print(file_path_name, '已存在，跳过！')
                continue
            urlretrieve(url, file_path_name)
            print(url, '下载成功!')


def main() -> object:
    queue = prepare_links()
    if queue and queue.qsize() > 0:
        threads = []
        for n in range(0, 32):
            thread = threading.Thread(target=download, args=[queue])
            threads.append(thread)

        for t in threads:
            t.start()
            t.join()


if __name__ == '__main__':
    main()
