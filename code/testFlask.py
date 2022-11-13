import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)
import control 


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
        status=globals.status
    )

# 测试界面
@search.route('/test', methods=['GET', 'POST'])
def test():
    globals.test=1
    # test=globals.ctrl.get_test()
    test=[{
        "Bookid": 2,
        "Question": "《活着》采用的是第一人称叙事，以主人公福贵的口吻，从讲述“一个老百姓自己的故事”的角度，表现原先难以表述的对人及时代真相的认识。",
        "Type": 1,
        "Option_num": 2,
        "Options": [
            "T",
            "F"
        ],
        "Ans": "T",
        "Category": "content"
    },{
        "Bookid": 2,
        "Question": "下列关于《活着》中的人物表述，不正确的一项是",
        "Type": 2,
        "Option_num": 4,
        "Options": [
            "春生，比较精明会生存的人。春生在无数次的战争中活下来，从第一次在长江附近打仗到抗美援朝，顽强地和命运抗争着，甚至在文化大革命的时候，也可以九死一生。",
            "福贵一生是充满苦难。他的人生经历了从富裕到贫穷的巨大变化，甚至承受了亲人死在自己前面的残酷现实，面对一次又一次苦难遭遇的沉重打击，他总是忍耐、坚强、乐观的活着。",
            "二喜，善良，憨厚勤劳，他人残志不残。他是一个工人，有一定的阶级觉悟性，时代的觉悟性。",
            "福贵父亲，旧时的地主，他对福贵的教育反映了一种典型的中国式父子教育——表面上严格，其实包含着纵容溺爱。"
        ],
        "Ans": "春生，比较精明会生存的人。春生在无数次的战争中活下来，从第一次在长江附近打仗到抗美援朝，顽强地和命运抗争着，甚至在文化大革命的时候，也可以九死一生。",
        "Category": "figure"
    }]
    if globals.status == 1:
        return render_template(
            "profile.html",
            status=globals.status
        )
    if globals.status == 2:
        return render_template(
            'test.html',
            status=globals.status,
            test=test
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