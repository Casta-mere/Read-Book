from database import Database_conn as db
import control
import json

# databse=db.my_sql("readbook")
dir = "record/database_design/question.json"
mkdir2 = "record/questions/data"


def mkdir():
    for i in range(1, 201):
        with open(f"{mkdir2}/{i}.json", "w", encoding="utf-8") as f:
            f.write(
                '{"0": {"Bookid": 2,"Question": "xxx","Type": 3,"Options": ["xxxx","x","xx","xxx"],"Ans": "xxxx","Category": "xxxx"},}')
            f.close()


def load():
    with open(dir, encoding="utf-8") as f:
        c = control.control()
        data = json.load(f)
        for i in data:
            info = []
            print(data[i]["Bookid"])
            info.append(f'"{data[i]["Bookid"]}"')
            print(data[i]["Question"])
            info.append(f'"{data[i]["Question"]}"')
            print(data[i]["Type"])
            info.append(f'"{data[i]["Type"]}"')
            options = data[i]["Options"]
            num = len(options)
            info.append(f'"{num}"')
            count = 0
            for j in options:
                print("option :", j)
                info.append(f'"{j}"')
                count += 1
            for j in range(count, 4):
                info.append('""')
            print(data[i]["Ans"])
            info.append(f'"{data[i]["Ans"]}"')
            print(data[i]["Category"])
            info.append(f'"{data[i]["Category"]}"')
            c.database.Update_table("question", info)


def test():
    with open(dir, encoding="utf-8") as f:
        data = json.load(f)
        for i in data:
            try:
                print(data[i]["Bookid"])
                print(data[i]["Question"])
                print(data[i]["Type"])
                options = data[i]["Options"]
                for j in options:
                    print("option :", j)
                print(data[i]["Ans"])
                print(data[i]["Category"])
            except:
                print(f"error on {i}")


c = control.control()
# c.load_question(dir)
question=c.get_question_random()
