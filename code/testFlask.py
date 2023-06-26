import time
from flask import (
    Flask, render_template, request, redirect, url_for, session)
import control 
import json
import random
import os

def secretKey():
    key_bytes = os.urandom(16)
    key = key_bytes.hex()
    return key

search = Flask(__name__)
search.secret_key = secretKey()

ctrl = control.control()

# 主页
@search.route('/Home', methods=['GET', 'POST'])
def Index():
    try:
        temp=random.randint(0, 200)
        detail=ctrl.get_book_detail_info(temp+1)
        return render_template(
            'index.html',
            status=session['status'],
            detail=detail,
            bookReID=temp
            )
    except:
        return redirect(url_for('PreProcessing'))

@search.route('/', methods=['GET','POST'])
def PreProcessing():
    # register--0|login--1|info--2
    session['status'] = 1
    # login error
    session['error'] = 0
    # register error pw!=pw2--1|not all--2
    session['retry'] = 0
    # user info
    session['User'] = {"id":"","name":"","pw":"","gender":"","tele":"","brief":""}
    # 从test进入
    session['test'] = 0
    # 从statistics进入
    session['stat'] = 0
    # 从题库抽出的问题
    session['ques'] = 0
    # 测试的开始时间
    session['starttime'] = 0
    # 是否进行过测试
    session['anytest'] = 0
    # 选择的内容
    session['choice'] = 0

    return redirect(url_for('Index'))

# 书籍概览    
@search.route('/books', methods=['GET', 'POST'])
def books():
    try:
        books=ctrl.get_book_brief_info()
        return render_template(
            'books.html',
            status=session['status'],
            book=books
        )
    except:
        return redirect(url_for('PreProcessing'))

# 书籍详情页
@search.route('/bookDetail/<int:id>', methods=['GET', 'POST'])
def bookDetail(id):
    try:
        detail=ctrl.get_book_detail_info(id+1)
        if (detail[16] or detail[17]):
            foreign=1
        else:
            foreign=0
        return render_template(
            "bookDetail.html",
            detail=detail,
            foreign=foreign,
            status=session['status'],
            i=id
        )
    except:
        return redirect(url_for('PreProcessing'))

# 测试界面
@search.route('/test', methods=['GET', 'POST'])
def test(): 
    try:
        if session['status'] == 1:
            session['test']=1
            session['stat']=0
            return render_template(
                "profile.html",
                status=session['status']
            )
        if session['status'] == 2:
            return render_template(
                'test.html',
                status=session['status'],
                )
    except:
        return redirect(url_for('PreProcessing'))

# 书籍详情页进入测试        
@search.route('/testID/<int:id>',methods=['GET', 'POST'])
def testID(id):
    try:
        whole=0
        head=['A','B','C','D']
        session['ques']=ctrl.get_question_by_bookid(id)
        session['starttime']=int(time.time())
        return render_template(
            "testStart.html",
            status=session['status'],
            test=session['ques'],
            head=head,
            whole=whole,
            length=len(session['ques'])
        )
    except:
        return redirect(url_for('PreProcessing'))

# 选取测试题目的类型
@search.route('/testSelected', methods=['GET', 'POST'])
def testSelected():
    try:
        data=json.loads(list(request.args.to_dict().keys())[0])
        testType=data["selected"][0]
        if testType=="random":                                          #随机出题测试
            test=ctrl.get_question_random()
        else:                                                           #指定类型随机出题测试
            test=ctrl.get_question_by_category(testType)
        session['ques']=test
        session['starttime']=int(time.time())
        return redirect(url_for('Index'))
    except:
        return redirect(url_for('PreProcessing'))
 
# 正式测试
@search.route('/testStart', methods=['GET', 'POST'])
def testStart():
    try:
        whole=0
        head=['A','B','C','D']
        return render_template(
            "testStart.html",
            status=session['status'],
            test=session['ques'],
            head=head,
            whole=whole,
            length=len(session['ques'])
        )
    except:
        return redirect(url_for('PreProcessing'))

# 提交
@search.route('/submit', methods=['GET', 'POST'])
def submit():
    try:
        returnData=json.loads(list(request.args.to_dict().keys())[0])           # {'titleID_choice': ['20_true']}
        choice=returnData["titleID_choice"]                                     # ['2_true', '5_true', '7_true', '9_芝麻,开门吧!', '20_true', '21_鲁贵', '24_true'] 0--24
        session['choice']=dict()
        for item in choice:
            session['choice'][item.split("_")[0]]=item.split("_")[1]
        
        test=session['ques']
        returnData.update({'test':test})
        returnData.update({"userid":session['User']["id"]})

        endtime=int(time.time())
        returnData.update({"starttime":session['starttime']})
        returnData.update({"endtime":endtime})
        returnData.update({"questionnum":len(session['ques'])})
        ctrl.check(returnData)

        return redirect(url_for('Index'))
    except:
        return redirect(url_for('PreProcessing'))

# 处理数据
@search.route('/process', methods=['GET', 'POST'])
def process():
    try:
        whole=0
        head=['A','B','C','D']
        return render_template(
            "process.html",
            status=session['status'],
            whole=whole,
            head=head,
            length=len(session['ques']),
            test=session['ques'],
            choice=session['choice']
        )
    except:
        return redirect(url_for('PreProcessing'))

# 数据分析
@search.route('/statistics', methods=['GET', 'POST'])
def statistics():
    try:
        session['anytest']=0
        session['stat'] = 1
        session['test'] = 0
        if session['status'] == 1:
            return render_template(
                "profile.html",
                status=session['status']
            )
        if session['status'] == 2:
            data = ctrl.get_user_statistics(int(session['User']["id"]))
            if data == None:
                session['anytest'] = 1
                return render_template(
                    "statistics.html",
                    status=session['status'],
                    anytest=session['anytest']
                )
            else:
                return render_template(
                    'statistics.html',
                    status=session['status'],
                    username=session['User']["name"],
                    times=data["count"],
                    avgDuration=str(data["avgduration"]//60)+"分"+str(data["avgduration"]%60)+"秒",
                    avgAccuracy=int(data["avgscore"]),
                    lastDuration=str(data["lastduration"]//60)+"分"+str(data["lastduration"]%60)+"秒",
                    lastAccuracy=int(data["lastscore"]),
                    lastTime=time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime(data["lasttime"])),
                    anytest=session['anytest'],
                    Testscore=data["scores"]
                    )
    except:
        return redirect(url_for('PreProcessing'))

# 个人信息    
@search.route('/profile', methods=['GET', 'POST'])
def profile():
    try:
        return render_template(
            'profile.html',
            status=session['status'],
            id=session['User']["id"],
            name=session['User']["name"],
            gender=session['User']["gender"],
            tele=session['User']["tele"],
            brief=session['User']["brief"]
            )
    except:
        return redirect(url_for('PreProcessing'))

# 登录界面    
@search.route('/login', methods=['GET', 'POST'])
def login():
    try:
        session['status'] = 1
        session['test'] = 0
        session['stat'] = 0
        return render_template(
            'profile.html',
            status=session['status'],
            error=session['error'],
            retry=session['retry']
            )
    except:
        return redirect(url_for('PreProcessing'))

# 注册界面
@search.route('/register', methods=['GET', 'POST'])
def register():
    try:
        session['status']=0
        return render_template(
            "profile.html",
            status=session['status'],
            error=session['error'],
            retry=session['retry']
            )
    except:
        return redirect(url_for('PreProcessing'))

# 注册确认
@search.route('/registration',methods=['GET', 'POST'])
def registration():
    try:
        session['error']=0
        session['retry']=0
        pw=request.args.get('pwReg')
        pw2=request.args.get('pw2Reg')
        if pw==pw2:
            name=request.args.get("nameReg")
            gender=request.args.get("genderReg")
            tele=request.args.get("teleReg")
            brief=request.args.get("briefReg")
            if(name and gender and tele and brief and pw and pw2):
                id=ctrl.new_user(name,gender,tele,pw,brief)
                session['status']=1
                return render_template(
                    "validation.html",
                    status=session['status'],
                    id=id
                )
            else:
                session['retry']=2
                return render_template(
                    "profile.html",
                    status=session['status'],
                    retry=session['retry']
                )
        else:
            session['retry']=1
            return render_template(
                "profile.html",
                status=session['status'],
                retry=session['retry']
            )
    except:
        return redirect(url_for('PreProcessing'))

# 登录确认
@search.route('/validation', methods=['GET', 'POST'])
def validation():
    try:
        session['error']=0
        session['retry']=0
        pw=str(request.form.get('pw'))
        id=request.form.get('id')
        temp=ctrl.get_user_info_by_id(id)
        try:
            # 是否输对密码
            if temp[4]==pw:
                session['User']={"id":temp[0],"name":temp[1],"gender":temp[2],"tele":temp[3],"pw":temp[4],"brief":temp[5]}
                session['status'] = 2

                # 如果从test栏进入，返回test界面
                if session['test'] == 1:
                    session['test'] = 0
                    return redirect(url_for('test'))
                
                # 如果从stat栏进入，返回stat界面
                elif session['stat'] == 1:
                    session['stat'] = 0
                    return redirect(url_for('statistics'))
                
                # 否则返回首页
                else:
                    try:
                        return redirect(url_for('Index'))
                    except:
                        return redirect(url_for('login'))

            # 输错密码
            else:
                print(2)
                session['error']=1
                return render_template(
                    "profile.html",
                    status=session['status'],
                    error=session['error']
                    )
        # 没输入密码
        except:
            print(3)
            session['error']=1
            return render_template(
                "profile.html",
                status=session['status'],
                error=session['error']
                )
    except:
        return redirect(url_for('PreProcessing'))

# 下线
@search.route("/logout",methods=['GET', 'POST'])
def logout():
    try:
        session['status']=1
        return redirect(url_for('Index'))
    except:
        return redirect(url_for('PreProcessing'))
  
def run():
    search.run(debug=True)
    
def run_local():
    search.run()

def server_run():
    search.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    run()
