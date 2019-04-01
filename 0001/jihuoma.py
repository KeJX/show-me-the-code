import random



class code_generator(object):
    def __init__(self):
        """
        将0~9,a~z,A~Z保存到list中，用random.sample从list中取固定位数
        """
        self.code_list = []
        for i in range(10):
            self.code_list.append(str(i))
        # print i
        for i in range(65, 91):
            self.code_list.append(chr(i))
        # print chr(i)
        for i in range(97, 123):
            self.code_list.append(chr(i))

    def gen_code(self,length=8):
        myslice = random.sample(self.code_list, length)
        veri_code = ''.join(myslice)
        return veri_code

    def get_code(self,num=200):
        i=0
        code_list = []
        while i <num:
            i+=1
            a = self.gen_code()
            code_list.append(a)
            sta_code_list = tuple(code_list)
        return sta_code_list

i=0
cg = code_generator()
a = cg.get_code(200)
for n in a:
    i+=1
    print(n)
print(i)

