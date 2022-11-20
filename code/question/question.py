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
    

class test():
    def __init__(self,l):
        self.category={}
        self.category.update({"figure":[0,0]})
        self.category.update({"writer":[0,0]})
        self.category.update({"main":[0,0]})
        self.category.update({"content":[0,0]})
        self.category.update({"detail":[0,0]})

        self.questions={}

        for i in l["test"]:
            try:
                self.category[i["Category"]][1]+=1
            except:
                e=1
        self.questionscategory={}
        for i in l["test"]:
            self.questions.update({i["q_id"]:i["Ans"]})
            self.questionscategory.update({i["q_id"]:i["Category"]})
        

        self.score=0
        self.right=0
        self.wrong=0
        self.null=0
        self.answer={}
        for i in l["titleID_choice"]:
            temp=i.split("_",1)
            self.answer.update({int(temp[0])+1:temp[1]})
        self.all=len(self.questions)
        for i in self.answer:
            if(self.answer[i]==self.questions[i]):
                self.right+=1
                try:
                    self.category[self.questionscategory[i]][0]+=1
                except:
                    e=1
            else:
                self.wrong+=1
        try:
            self.score=self.right/self.all*100
        except:
            self.score=0

        self.null=self.all-self.right-self.wrong




    def print(self):  
        print(f"score : {self.score}")
        print(f"right : {self.right}")
        print(f"wrong : {self.wrong}")
        print(f"null : {self.null}")
        print(f"all : {self.all}")

    def get_stat(self):
        return self.score,self.right,self.wrong,self.null

    def get_category(self):
        ans=[]
        for i in self.category:
            ans.append(self.category[i][0])
            ans.append(self.category[i][1])
        return ans[0],ans[1],ans[2],ans[3],ans[4],ans[5],ans[6],ans[7],ans[8],ans[9]