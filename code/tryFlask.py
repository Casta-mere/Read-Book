import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for)
import control 
import json
import multiprocessing
from multiprocessing import Process
import random
from werkzeug.local import Local

search = Flask(__name__)

class gVal:

    # register--0|login--1|info--2
    status = 1
    # login error
    error = 0
    # register error pw!=pw2--1|not all--2
    retry = 0
    # user info
    User = {"id":"","name":"","pw":"","gender":"","tele":"","brief":""}
    # 从test进入
    test = 0
    # 从statistics进入
    stat = 0
    # 从题库抽出的问题
    ques = 0
    # 测试的开始时间
    starttime = 0
    # 是否进行过测试
    anytest = 0
    # 选择的内容
    choice = 0

    # 引入control的函数
    ctrl=control.control()

class gFunc:
    def __init__(self):
        self.g = gVal()
        self.g.ctrl=control.control()

    def index(self):
        self.g = gVal()
        temp=random.randint(0, 200)
        detail=self.g.ctrl.get_book_detail_info(temp+1)
        return render_template(
            'index.html',
            status=self.g.status,
            detail=detail,
            bookReID=temp
            )
        
    def index1(self):
        temp=random.randint(0, 200)
        detail=self.g.ctrl.get_book_detail_info(temp+1)
        return render_template(
            'index.html',
            status=self.g.status,
            detail=detail,
            bookReID=temp
            )

    def books(self):
        books=self.g.ctrl.get_book_brief_info()
        return render_template(
            'books.html',
            status=self.g.status,
            book=books
        )
    
    def bookDetail(self, id):
        detail=self.g.ctrl.get_book_detail_info(id+1)
        if (detail[16] or detail[17]):
            foreign=1
        else:
            foreign=0
        return render_template(
            "bookDetail.html",
            detail=detail,
            foreign=foreign,
            status=self.g.status,
            i=id
        )
    
    #here
    def test(self): 
        if self.g.status == 1:
            self.g.test=1
            self.g.stat=0
            return render_template(
                "profile.html",
                status=self.g.status
            )
        if self.g.status == 2:
            return render_template(
                'test.html',
                status=self.g.status,
                )
            
    def testID(self, id):
        whole=0
        head=['A','B','C','D']
        self.g.ques=self.g.ctrl.get_question_by_bookid(id)
        self.g.starttime=int(time.time())
        return render_template(
            "testStart.html",
            status=self.g.status,
            test=self.g.ques,
            head=head,
            whole=whole,
            length=len(self.g.ques)
    )
        
    def testSelected(self):
        data=json.loads(list(request.args.to_dict().keys())[0])
        testType=data["selected"][0]
        if testType=="random":                                          #随机出题测试
            test=self.g.ctrl.get_question_random()
        else:                                                           #指定类型随机出题测试
            test=self.g.ctrl.get_question_by_category(testType)
        self.g.ques=test
        self.g.starttime=int(time.time())
        return redirect(url_for('index1'))
    
    def testStart(self):
        whole=0
        head=['A','B','C','D']
        return render_template(
            "testStart.html",
            status=self.g.status,
            test=self.g.ques,
            head=head,
            whole=whole,
            length=len(self.g.ques)
        )
        
    def submit(self):
    
        returnData=json.loads(list(request.args.to_dict().keys())[0])           # {'titleID_choice': ['20_true']}
        choice=returnData["titleID_choice"]                                     # ['2_true', '5_true', '7_true', '9_芝麻,开门吧!', '20_true', '21_鲁贵', '24_true'] 0--24
        self.g.choice=dict()
        for item in choice:
            self.g.choice[item.split("_")[0]]=item.split("_")[1]
        
        test=self.g.ques
        returnData.update({'test':test})
        returnData.update({"userid":self.g.User["id"]})

        endtime=int(time.time())
        returnData.update({"starttime":self.g.starttime})
        returnData.update({"endtime":endtime})
        returnData.update({"questionnum":len(self.g.ques)})
        self.g.ctrl.check(returnData)

        return redirect(url_for('index1'))
    
    def process(self):
        whole=0
        head=['A','B','C','D']
        return render_template(
            "process.html",
            status=self.g.status,
            whole=whole,
            head=head,
            length=len(self.g.ques),
            test=self.g.ques,
            choice=self.g.choice
        )
        
    def statistics(self):
        self.g.anytest=0
        self.g.stat = 1
        self.g.test = 0
        if self.g.status == 1:
            return render_template(
                "profile.html",
                status=self.g.status
            )
        if self.g.status == 2:
            data = self.g.ctrl.get_user_statistics(int(self.g.User["id"]))
            if data == None:
                self.g.anytest = 1
                return render_template(
                    "statistics.html",
                    status=self.g.status,
                    anytest=self.g.anytest
                )
            else:
                return render_template(
                        'statistics.html',
                        status=self.g.status,
                        username=self.g.User["name"],
                        times=data["count"],
                        avgDuration=str(data["avgduration"]//60)+"分"+str(data["avgduration"]%60)+"秒",
                        avgAccuracy=int(data["avgscore"]),
                        lastDuration=str(data["lastduration"]//60)+"分"+str(data["lastduration"]%60)+"秒",
                        lastAccuracy=int(data["lastscore"]),
                        lastTime=time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime(data["lasttime"])),
                        anytest=self.g.anytest,
                        Testscore=data["scores"]
                    )
    
    def profile(self):
        return render_template(
            'profile.html',
            status=self.g.status,
            id=self.g.User["id"],
            name=self.g.User["name"],
            gender=self.g.User["gender"],
            tele=self.g.User["tele"],
            brief=self.g.User["brief"]
        )
        
    def login(self):
        self.g.status = 1
        self.g.test = 0
        self.g.stat = 0
        return render_template(
            'profile.html',
            status=self.g.status,
            error=self.g.error,
            retry=self.g.retry
            )
        
    def register(self):
        self.g.status=0
        return render_template(
            "profile.html",
            status=self.g.status,
            error=self.g.error,
            retry=self.g.retry
            )
        
    def registration(self):
        self.g.error=0
        self.g.retry=0
        pw=request.args.get('pwReg')
        pw2=request.args.get('pw2Reg')
        if pw==pw2:
            name=request.args.get("nameReg")
            gender=request.args.get("genderReg")
            tele=request.args.get("teleReg")
            brief=request.args.get("briefReg")
            if(name and gender and tele and brief and pw and pw2):
                id=self.g.ctrl.new_user(name,gender,tele,pw,brief)
                self.g.status=1
                return render_template(
                    "validation.html",
                    status=self.g.status,
                    id=id
                )
            else:
                self.g.retry=2
                return render_template(
                    "profile.html",
                    status=self.g.status,
                    retry=self.g.retry
                )
        else:
            self.g.retry=1
            return render_template(
                "profile.html",
                status=self.g.status,
                retry=self.g.retry
            )
    
    def validation(self):
        self.g.error=0
        self.g.retry=0
        pw=str(request.form.get('pw'))
        id=request.form.get('id')
        temp=self.g.ctrl.get_user_info_by_id(id)
        try:
            # 是否输对密码
            if temp[4]==pw:
                self.g.User={"id":temp[0],"name":temp[1],"gender":temp[2],"tele":temp[3],"pw":temp[4],"brief":temp[5]}
                self.g.status = 2

                # 如果从test栏进入，返回test界面
                if self.g.test == 1:
                    self.g.test = 0
                    return redirect(url_for('test'))
                
                # 如果从stat栏进入，返回stat界面
                elif self.g.stat == 1:
                    self.g.stat = 0
                    return redirect(url_for('statistics'))
                
                # 否则返回首页
                else:
                    try:
                        return redirect(url_for('index1'))
                    except:
                        return redirect(url_for('login'))

            # 输错密码
            else:
                print(2)
                self.g.error=1
                return render_template(
                    "profile.html",
                    status=self.g.status,
                    error=self.g.error
                    )
        # 没输入密码
        except:
            print(3)
            self.g.error=1
            return render_template(
                "profile.html",
                status=self.g.status,
                error=self.g.error
                )
    
    def logout(self):
        self.g.status=1
        return redirect(url_for('index1'))

globals=gVal()
globalsF=gFunc()

# 主页
@search.route('/', methods=['GET', 'POST'])
def index():
    return globalsF.index()

# 伪首页
@search.route('/index', methods=['GET', 'POST'])
def index1():
    return globalsF.index1()

# 书籍概览    
@search.route('/books', methods=['GET', 'POST'])
def books():
    return globalsF.books()

# 书籍详情页
@search.route('/bookDetail/<int:id>', methods=['GET', 'POST'])
def bookDetail(id):
    return globalsF.bookDetail(id)

# 测试界面
@search.route('/test', methods=['GET', 'POST'])
def test(): 
    return globalsF.test()

# 书籍详情页进入测试        
@search.route('/testID/<int:id>',methods=['GET', 'POST'])
def testID(id):
    return globalsF.testID(id)

# 选取测试题目的类型
@search.route('/testSelected', methods=['GET', 'POST'])
def testSelected():
    return globalsF.testSelected()
 
# 正式测试
@search.route('/testStart', methods=['GET', 'POST'])
def testStart():
    return globalsF.testStart()

# 提交
@search.route('/submit', methods=['GET', 'POST'])
def submit():
    return globalsF.submit()

# 处理数据
@search.route('/process', methods=['GET', 'POST'])
def process():
    return globalsF.process()

# 数据分析
@search.route('/statistics', methods=['GET', 'POST'])
def statistics():
    return globalsF.statistics()

# 个人信息    
@search.route('/profile', methods=['GET', 'POST'])
def profile():
    return globalsF.profile()

# 登录界面    
@search.route('/login', methods=['GET', 'POST'])
def login():
    return globalsF.login()

# 注册界面
@search.route('/register', methods=['GET', 'POST'])
def register():
    return globalsF.register()

# 注册确认
@search.route('/registration',methods=['GET', 'POST'])
def registration():
    return globalsF.registration()

# 登录确认
@search.route('/validation', methods=['GET', 'POST'])
def validation():
    return globalsF.validation()

# 下线
@search.route("/logout",methods=['GET', 'POST'])
def logout():
    return globalsF.logout()
  
def run():
    search.run(debug=True)
    
def run_local():
    search.run()

def server_run():
    search.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    run()
