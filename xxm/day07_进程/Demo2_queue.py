import multiprocessing

q = multiprocessing.Queue()
q.put((1, 2))
q.put(0)
q.put(['d', 'k'])

print(q.get())
print(q.get())
print(q.get())
# 没有内容会阻塞 ---
# print(q.get())
# 没有内容会报错---get_nowait
# print(q.get_nowait())
# while True:
#
#     if not q.empty():
#         x = q.get()
#         print(x)
#     else:
#         break
