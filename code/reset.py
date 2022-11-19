from database import Database_conn as db
import control

def reset():
    d=db.my_sql("readbook")
    d.Create_Database()

    db.reset_book()
    db.reset_question()
    db.reset_user()
    db.reset_statistics()

    with open('code/database/book_info.sql', 'r', encoding="utf-8") as f:
        sql = f.readline().strip('\n')
        while(sql):
            d.execute_sql(sql)
            sql = f.readline().strip('\n')

    c = control.control()
    for i in range (1, 201):
        c.load_question(f"record/questions/data/{i}.json")

reset()