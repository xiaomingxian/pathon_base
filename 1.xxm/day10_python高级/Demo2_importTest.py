def c():
    print('cccccc----')


class A:
    def aa(self):
        print('aaaaaaaa')

ss = [1, 2, [2,2,2]]

kk=ss[:]
print(id(ss),id(kk))
print(id(ss[2]),id(kk[2]))


# k=ss[0:-1]
# print(k)
# kk=ss[len(ss)::-1]
# print(kk)