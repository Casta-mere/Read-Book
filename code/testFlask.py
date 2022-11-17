import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)
import control 
import json


search = Flask(__name__)

# register--0|login--1|info--2
globals.status = 1
# login error
globals.error = 0
# register error pw!=pw2--1|not all--2
globals.retry = 0
# user info
globals.User = {"id":"","name":"","pw":"","gender":"","tele":"","brief":""}
# 从test进入
globals.test = 0

globals.ctrl=control.control()

# 主页
@search.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html',
        status=globals.status
        )

# 书籍概览    
@search.route('/books', methods=['GET', 'POST'])
def books():
    books=globals.ctrl.get_book_brief_info()
    print(books)
    return render_template(
        'books.html',
        status=globals.status,
        book=books
    )

# 书籍详情页
@search.route('/bookDetail/<int:id>', methods=['GET', 'POST'])
def bookDetail(id):
    detail=globals.ctrl.get_book_detail_info(id+1)
    if (detail[16] or detail[17]):
        foreign=1
    else:
        foreign=0
    return render_template(
        "bookDetail.html",
        detail=detail,
        foreign=foreign,
        status=globals.status,
        i=id
    )

# 测试界面
@search.route('/test', methods=['GET', 'POST'])
def test():
    globals.test=1
    if globals.status == 1:
        return render_template(
            "profile.html",
            status=globals.status
        )
    if globals.status == 2:
        return render_template(
            'test.html',
            status=globals.status,
            )

# 正式测试
@search.route('/testStart', methods=['GET', 'POST'])
def testStart():
    # con=json.loads(request.get_json())
    # print(1)
    # print(con["choice"])
    whole=0
    head=['A','B','C','D']
    test=globals.ctrl.get_question_random()

    return render_template(
        "testStart.html",
        status=globals.status,
        test=test,
        head=head,
        whole=whole
    )

# 整卷阅览
@search.route('/testLook', methods=['GET', 'POST'])
def testLook():
    whole=1
    head=['A','B','C','D']
    test=globals.ctrl.get_question_random()
    return render_template(
        "testStart.html",
        status=globals.status,
        test=test,
        head=head,
        whole=whole
    )

# 提交
@search.route('/submit', methods=['GET', 'POST'])
def submit():
    # ImmutableMultiDict([('{"choice":["9_3"]}', '')]) -- 原始数据
    # con=request.args.to_dict() -- {'{"choice":["9_3"]}': ''}
    # temp=json.loads(list(con.keys())[0]) -- {'choice': ['9_3']}
    # temp1=temp["choice"][0] -- 9_3 -->多个temp["choice"][i]
    # temp2=temp1.split("_")[1] -- 3
    
    # 多个就写循环
    choice=list()
    temp=json.loads(list(request.args.to_dict().keys())[0])["choice"][0].split("_")[1]
    choice.append(int(temp))
    choice.append(int(temp))
    
    # 所有的选择
    print(choice)
    return render_template(
        "index.html",
        status=globals.status
    )

# 处理数据
@search.route('/process', methods=['GET', 'POST'])
def process():
    return render_template(
        "index.html",
        status=globals.status
    )

@search.route('/statistics', methods=['GET', 'POST'])
def statistics():
    return render_template(
        'statistics.html',
        status=globals.status
        )

# 个人信息    
@search.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template(
        'profile.html',
        status=globals.status,
        id=globals.User["id"],
        name=globals.User["name"],
        gender=globals.User["gender"],
        tele=globals.User["tele"],
        brief=globals.User["brief"]
        )

# 登录界面    
@search.route('/login', methods=['GET', 'POST'])
def login():
    globals.status = 1
    return render_template(
        'profile.html',
        status=globals.status,
        error=globals.error,
        retry=globals.retry
        )

# 注册界面
@search.route('/register', methods=['GET', 'POST'])
def register():
    globals.status=0
    return render_template(
        "profile.html",
        status=globals.status,
        error=globals.error,
        retry=globals.retry
        )

# 注册确认
@search.route('/registration',methods=['GET', 'POST'])
def registration():
    globals.error=0
    globals.retry=0
    pw=request.args.get('pwReg')
    pw2=request.args.get('pw2Reg')
    if pw==pw2:
        name=request.args.get("nameReg")
        gender=request.args.get("genderReg")
        print(1)
        tele=request.args.get("teleReg")
        brief=request.args.get("briefReg")
        if(name and gender and tele and brief and pw and pw2):
            id=globals.ctrl.new_user(name,gender,tele,pw,brief)
            print(1)
            globals.status=1
            return render_template(
                "validation.html",
                status=globals.status,
                id=id
            )
        else:
            globals.retry=2
            return render_template(
                "profile.html",
                status=globals.status,
                retry=globals.retry
            )
    else:
        globals.retry=1
        return render_template(
            "profile.html",
            status=globals.status,
            retry=globals.retry
        )

# 登录确认
@search.route('/validation', methods=['GET', 'POST'])
def validation():
    globals.error=0
    globals.retry=0
    pw=str(request.form.get('pw'))
    id=request.form.get('id')
    temp=globals.ctrl.get_user_info_by_id(id)
    try:
        if temp[4]==pw:
            globals.User={"id":temp[0],"name":temp[1],"gender":temp[2],"tele":temp[3],"pw":temp[4],"brief":temp[5]}
            print(globals.User)
            globals.status = 2
            if globals.test == 1:
                globals.test = 0
                return redirect(url_for('test'))
            return render_template(
                "index.html",
                status=globals.status,
                error=globals.error
                )
        else:
            globals.error=1
            return render_template(
                "profile.html",
                status=globals.status,
                error=globals.error
                )
    except:
        globals.error=1
        return render_template(
            "profile.html",
            status=globals.status,
            error=globals.error
            )

# 下线
@search.route("/logout",methods=['GET', 'POST'])
def logout():
    globals.status=1
    return render_template(
        "index.html",
        status=globals.status
    )    
def run():
    search.run(debug=True)

if __name__ == '__main__':
    run()