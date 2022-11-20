from database import Database_conn as db
from question import question as q
import random
# from webcrawer import douban_webcrawer as dw


class control():
    def __init__(self):
        self.database = db.my_sql("readbook")
        self.user_id = self.get_all_user_id()

    def get_all_user_id(self):
        users = self.database.get_data("user")
        exist = []
        for i in users:
            exist.append(i[0])
        return exist

    def get_user_info_by_id(self, id):
        try:
            ans = list(self.database.get_data_by_attr("user", 'id', id)[0])
        except:
            ans = []
        return ans

    # 创建新用户
    def new_user(self, name, gender, tele, pw, brief):
        import random
        id = random.randint(0, 10000)
        while(id in self.user_id):
            id = random.randint(0, 10000)
        self.database.Update_user(id, name, gender, tele, pw, brief)
        return id

    # 获取书籍排名，名字，作者
    def get_book_brief_info(self):
        brief_info = self.database.get_specific_data(
            "book", ["id", "name", "author"])
        return brief_info

    # 获取书籍详细信息,用于展示界面
    def get_book_detail_info(self, id):

        detail_info = self.database.get_data_by_attr("book", "id", id)
        return list(detail_info[0])

    # load question from json file
    def load_question(self, filename):
        import json
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
            for i in data:
                if (i == "0"):
                    continue
                info = []
                try:
                    info.append(f'"{data[i]["Bookid"]}"')
                    info.append(f'"{data[i]["Question"]}"')
                    info.append(f'"{data[i]["Type"]}"')
                    options = data[i]["Options"]
                    num = len(options)
                    info.append(f'"{num}"')
                    count = 0
                    for j in options:
                        info.append(f'"{j}"')
                        count += 1
                    for j in range(count, 4):
                        info.append('""')
                    info.append(f'"{data[i]["Ans"]}"')
                    info.append(f'"{data[i]["Category"]}"')
                    self.database.Update_table("question", info)
                except:
                    print(f"error on {filename}, question {i}")
    # 随机出题
    def get_question_random(self):
        questions = list(self.database.get_data("question"))
        ans = []
        for i in questions:
            ques = q.question(list(i))
            ans.append(ques.output())
        random.shuffle(ans)
        if(len(ans) > 25):
            ans = ans[:25]
        count = 1
        for i in ans:
            i.update({"q_id": count})
            count += 1
        return ans

    # 根据类别出题
    def get_question_by_category(self, category):
        questions = list(self.database.get_data_by_attr("question", "category", category))
        ans = []
        for i in questions:
            ques = q.question(list(i))
            ans.append(ques.output())
        random.shuffle(ans)
        if(len(ans) > 25):
            ans = ans[:25]
        count = 1
        for i in ans:
            i.update({"q_id": count})
            count += 1
        return ans
    # 根据书籍id出题
    def get_question_by_bookid(self, bookid):
        questions = list(self.database.get_data_by_attr("question", "bookid", bookid))
        ans = []
        for i in questions:
            ques = q.question(list(i))
            ans.append(ques.output())
        random.shuffle(ans)
        if(len(ans) > 25):
            ans = ans[:25]
        count = 1
        for i in ans:
            i.update({"q_id": count})
            count += 1
        return ans
    # 改卷 
    def check(self, info):

        print("*************")
        test = q.test(info)
        test.print()
        print("*************")
        userid = info["userid"]
        score, correctnum, wrongnum, emptynum = test.get_stat()
        start = info["starttime"]
        end = info["endtime"]
        duration = end-start
        a1, b1, a2, b2, a3, b3, a4, b4, a5, b5 = test.get_category()
        questionnum = info["questionnum"]

        self.database.Update_statistics(userid, score, start, end, duration, a1, a2,
                                        a3, a4, a5, b1, b2, b3, b4, b5, questionnum, correctnum, wrongnum, emptynum)

    # 获取用户答题数据
    def get_user_statistics(self, userid):
        try:
            returnvalue = {}
            item = []
            item.append("a1")
            item.append("b1")
            item.append("a2")
            item.append("b2")
            item.append("a3")
            item.append("b3")
            item.append("a4")
            item.append("b4")
            item.append("a5")
            item.append("b5")
            sql_ans = self.database.get_sepcific_data_by_attr(
                "statistics", item, "userid", userid)
            returnvalue.update({"count": len(sql_ans)})
            scores = []
            sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for i in sql_ans:
                scores.append(list(i))

            for i in scores:
                for j in range(10):
                    sum[j] += i[j]
            one = scores[-1]

            scores = []
            for i in range(5):
                if(one[2*i+1] != 0):
                    scores.append(int(one[2*i]/one[2*i+1]*100))
                else:
                    scores.append(0)

            for i in range(5):
                if(sum[2*i+1] != 0):
                    scores.append(int(sum[2*i]/sum[2*i+1]*100))
                else:
                    scores.append(0)
            returnvalue.update({"scores": scores})
            item = []
            item.append("end")

            sql_ans = self.database.get_sepcific_data_by_attr(
                "statistics", item, "userid", userid)
            ans = []
            for i in sql_ans:
                ans.append(i[0])
            returnvalue.update({"lasttime": ans[-1]})

            item = []
            item.append("duration")
            item.append("questionnum")
            item.append("rightnum")
            sql_ans = self.database.get_sepcific_data_by_attr(
                "statistics", item, "userid", userid)
            ans = []
            for i in sql_ans:
                ans.append(list(i))

            returnvalue.update({"lastduration": ans[-1][0]})
            returnvalue.update({"lastscore": ans[-1][2]/ans[-1][1]*100})

            sum = [0, 0, 0]
            for i in ans:
                sum[0] += i[0]
                sum[1] += i[1]
                sum[2] += i[2]
            returnvalue.update({"avgduration": int(sum[0]/len(ans))})
            returnvalue.update({"avgscore": sum[2]/sum[1]*100})

            return returnvalue
        except:
            return None

# print(c.get_user_info_by_id(1))
# print(c.new_user(1, 2, 3, 4, 5))
# with open("book.txt", "w", encoding="utf-8") as f:
#     books=c.get_book_brief_info()
#     for i in books:
#         # print(i[0],i[1])
#         f.write(str(i[0])+" "+str(i[1])+"\n")
# info= c.get_book_detail_info(183)
# print(info)
