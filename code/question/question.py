import random
class question():
    def __init__(self, l) :
        self.book_id = l[0]
        self.question = l[1]
        self.type = l[2]
        self.option_num = l[3]
        self.option = []
        for i in range(4, 4+self.option_num):
            self.option.append(l[i])
        random.shuffle(self.option)
        self.ans = l[8]
        self.category = l[9]
    
    def output(self):
        ans={}
        ans["Bookid"]=self.book_id
        ans["Question"]=self.question
        ans["Type"]=self.type
        ans["Option_num"]=self.option_num
        ans["Options"]=self.option
        ans["Ans"]=self.ans
        ans["Category"]=self.category
        return ans