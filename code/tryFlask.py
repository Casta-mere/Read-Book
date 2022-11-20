import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for)
import control 
import json



class globalsItem:
    def __init__(self):
        self.status = 1                                                                 # register--0|login--1|info--2
        self.error = 0                                                                  # login error
        self.retry = 0                                                                  # register error pw!=pw2--1|not all--2
        self.User = {"id":"","name":"","pw":"","gender":"","tele":"","brief":""}        # user info
        self.test = 0                                                                   # 从test进入
        self.stat = 0                                                                   # 从statistics进入
        self.ques = 0                                                                   # 从题库抽出的问题
        self.anytest = 0                                                                # 有无历史测试
        self.ctrl=control.control()                                                     # 导入control
        self.search=Flask(__name__)
    
    def set_status(self, status):
        self.status = status
    
    def get_status(self):
        return self.status
    
    def set_error(self, error):
        self.error = error
        
    def get_error(self):
        return self.error
    
    def set_retry(self, retry):
        self.retry = retry
        
    def get_retry(self):
        return self.retry
    
    def set_User(self, User):
        self.User = User
        
    def get_User(self):
        return self.User
    
    def set_test(self, test):
        self.test = test
        
    def get_test(self):
        return self.test
    
    def set_stat(self, stat):
        self.stat = stat
        
    def get_stat(self):
        return self.stat
    
    def set_ques(self, ques):
        self.ques = ques
        
    def get_ques(self):
        return self.ques
    
    def set_anytest(self, anytest):
        self.anytest = anytest
        
    def get_anytest(self):
        return self.anytest
    
    def set_ctrl(self, ctrl):
        self.ctrl = ctrl
        
    def get_ctrl(self):
        return self.ctrl

    

    # 主页
    @search.route('/', methods=['GET', 'POST'])
    def index(self):
        return render_template(
            'index.html',
            status=globalsItem.get_status(self)
            )

    # 书籍概览    
    @search.route('/books', methods=['GET', 'POST'])
    def books():
        books=globalsItem.ctrl.get_book_brief_info()
        # print(books)
        return render_template(
            'books.html',
            status=globalsItem.status,
            book=books
        )

    # 书籍详情页
    @search.route('/bookDetail/<int:id>', methods=['GET', 'POST'])
    def bookDetail(id):
        detail=globalsItem.ctrl.get_book_detail_info(id+1)
        if (detail[16] or detail[17]):
            foreign=1
        else:
            foreign=0
        return render_template(
            "bookDetail.html",
            detail=detail,
            foreign=foreign,
            status=globalsItem.status,
            i=id
        )

    # 测试界面
    @search.route('/test', methods=['GET', 'POST'])
    def test():
        globalsItem.test=1
        test=globalsItem.ctrl.get_question_random()
        globalsItem.ques=test
        globalsItem.starttime=int(time.time())
        if globalsItem.status == 1:
            return render_template(
                "profile.html",
                status=globalsItem.status
            )
        if globalsItem.status == 2:
            return render_template(
                'test.html',
                status=globalsItem.status,
                )

    # 正式测试
    @search.route('/testStart', methods=['GET', 'POST'])
    def testStart():
        # con=json.loads(request.get_json())
        # print(1)
        # print(con["choice"])
        whole=0
        head=['A','B','C','D']
        return render_template(
            "testStart.html",
            status=globalsItem.status,
            test=globalsItem.ques,
            head=head,
            whole=whole,
            length=len(globalsItem.ques)
        )

    # 整卷阅览
    @search.route('/testLook', methods=['GET', 'POST'])
    def testLook():
        whole=1
        head=['A','B','C','D']
        # 在这里就把选项都摘出来    
        # for item in returnData["choice"]:
        #     item = item.split(".")[1].rstrip()
        
        return render_template(
            "testStart.html",
            status=globalsItem.status,
            test=globalsItem.ques,
            head=head,
            whole=whole
        )

    # 提交
    @search.route('/submit', methods=['GET', 'POST'])
    def submit():

        returnData=json.loads(list(request.args.to_dict().keys())[0])
        test=globalsItem.ques
        returnData.update({'test':test})
        returnData.update({"userid":globalsItem.User["id"]})

        endtime=int(time.time())
        returnData.update({"starttime":globalsItem.starttime})
        returnData.update({"endtime":endtime})
        returnData.update({"questionnum":len(globalsItem.ques)})
        globalsItem.ctrl.check(returnData)

        return render_template(
            "index.html",
            status=globalsItem.status
        )

    # 处理数据
    @search.route('/process', methods=['GET', 'POST'])
    def process():
        return render_template(
            "index.html",
            status=globalsItem.status
        )

    @search.route('/statistics', methods=['GET', 'POST'])
    def statistics():
        globalsItem.anytest=0
        globalsItem.stat = 1
        globalsItem.test = 0
        if globalsItem.status == 1:
            return render_template(
                "profile.html",
                status=globalsItem.status
            )
        if globalsItem.status == 2:
            data = globalsItem.ctrl.get_user_statistics(int(globalsItem.User["id"]))
            if data == None:
                globalsItem.anytest = 1
                return render_template(
                    "statistics.html",
                    status=globalsItem.status,
                    anytest=globalsItem.anytest
                )
            else:
                return render_template(
                    'statistics.html',
                    status=globalsItem.status,
                    username=globalsItem.User["name"],
                    times=data["count"],
                    avgDuration=str(data["avgduration"]//60)+"分"+str(data["avgduration"]%60)+"秒",
                    avgAccuracy=int(data["avgscore"]),
                    lastDuration=str(data["lastduration"]//60)+"分"+str(data["lastduration"]%60)+"秒",
                    lastAccuracy=int(data["lastscore"]),
                    lastTime=time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime(data["lasttime"])),
                    anytest=globalsItem.anytest,
                    Testscore=data["scores"]
                    )

    # 个人信息    
    @search.route('/profile', methods=['GET', 'POST'])
    def profile():
        return render_template(
            'profile.html',
            status=globalsItem.status,
            id=globalsItem.User["id"],
            name=globalsItem.User["name"],
            gender=globalsItem.User["gender"],
            tele=globalsItem.User["tele"],
            brief=globalsItem.User["brief"]
            )

    # 登录界面    
    @search.route('/login', methods=['GET', 'POST'])
    def login():
        globalsItem.status = 1
        return render_template(
            'profile.html',
            status=globalsItem.status,
            error=globalsItem.error,
            retry=globalsItem.retry
            )

    # 注册界面
    @search.route('/register', methods=['GET', 'POST'])
    def register():
        globalsItem.status=0
        return render_template(
            "profile.html",
            status=globalsItem.status,
            error=globalsItem.error,
            retry=globalsItem.retry
            )

    # 注册确认
    @search.route('/registration',methods=['GET', 'POST'])
    def registration():
        globalsItem.error=0
        globalsItem.retry=0
        pw=request.args.get('pwReg')
        pw2=request.args.get('pw2Reg')
        if pw==pw2:
            name=request.args.get("nameReg")
            gender=request.args.get("genderReg")
            print(1)
            tele=request.args.get("teleReg")
            brief=request.args.get("briefReg")
            if(name and gender and tele and brief and pw and pw2):
                id=globalsItem.ctrl.new_user(name,gender,tele,pw,brief)
                print(1)
                globalsItem.status=1
                return render_template(
                    "validation.html",
                    status=globalsItem.status,
                    id=id
                )
            else:
                globalsItem.retry=2
                return render_template(
                    "profile.html",
                    status=globalsItem.status,
                    retry=globalsItem.retry
                )
        else:
            globalsItem.retry=1
            return render_template(
                "profile.html",
                status=globalsItem.status,
                retry=globalsItem.retry
            )

    # 登录确认
    @search.route('/validation', methods=['GET', 'POST'])
    def validation():
        globalsItem.error=0
        globalsItem.retry=0
        pw=str(request.form.get('pw'))
        id=request.form.get('id')
        temp=globalsItem.ctrl.get_user_info_by_id(id)
        try:
            if temp[4]==pw:
                globalsItem.User={"id":temp[0],"name":temp[1],"gender":temp[2],"tele":temp[3],"pw":temp[4],"brief":temp[5]}
                print(globalsItem.User)
                globalsItem.status = 2
                
                if globalsItem.test == 1:
                    globalsItem.test = 0
                    return redirect(url_for('test'))
                
                elif globalsItem.stat == 1:
                    globalsItem.stat = 0
                    return redirect(url_for('statistics'))
                
                else:
                    return render_template(
                        "index.html",
                        status=globalsItem.status,
                        error=globalsItem.error
                        )
            else:
                globalsItem.error=1
                return render_template(
                    "profile.html",
                    status=globalsItem.status,
                    error=globalsItem.error
                    )
        except:
            globalsItem.error=1
            return render_template(
                "profile.html",
                status=globalsItem.status,
                error=globalsItem.error
                )

    # 下线
    @search.route("/logout",methods=['GET', 'POST'])
    def logout():
        globalsItem.status=1
        return render_template(
            "index.html",
            status=globalsItem.status
        )    
def run():
    search=globalsItem()
    search.search.run(debug=True)

def server_run():
    search=globalsItem()
    search.search.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    run()
