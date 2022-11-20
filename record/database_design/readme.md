# Design for database

## Books
| Attribute     | Translation | Type    | Chinese book | Foreign book |
| :------------ | :---------- | :------ | :----------: | :----------: |
| Id            | 排名        | int     |   &check;    |   &check;    |
| Name          | 书名        | varchar |   &check;    |   &check;    |
| Author        | 作者        | varchar |   &check;    |   &check;    |
| Country       | 国家        | varchar |   &check;    |   &check;    |
| Publisher     | 出版社      | varchar |   &check;    |   &check;    |
| Year          | 出版日期    | varchar |   &check;    |   &check;    |
| Page          | 页数        | varchar |   &check;    |   &check;    |
| Price         | 定价        | varchar |   &check;    |   &check;    |
| Frame         | 装帧        | varchar |   &check;    |   &check;    |
| Category      | 丛书        | varchar |   &check;    |   &check;    |
| Isbn          | isbn码      | varchar |   &check;    |   &check;    |
| Star          | 评分        | float   |   &check;    |   &check;    |
| Comment_num   | 评价数量    | int     |   &check;    |   &check;    |
| Brief         | 简介        | varchar |   &check;    |   &check;    |
| Douban_bookid | 豆瓣id      | varchar |   &check;    |   &check;    |
| Link          | 链接        | varchar |   &check;    |   &check;    |
| Name_o        | 原作名      | varchar |   &cross;    |   &check;    |
| Trans         | 译者        | varchar |   &cross;    |   &check;    |

## Questions

| Attribute    | Type    | Translation    | Note                       |
| :----------- | :------ | :------------- | :------------------------- |
| Id           | int     | 关联书本的id   |                            |
| Question     | varchar | 问题           |                            |
| Type         | int     | 类别           | 0-判断, 1-单选             |
| Question_num | int     | 选项数量       |                            |
| C1           | varchar | 选项1          |                            |
| C2           | varchar | 选项2          |                            |
| C3           | varchar | 选项3          |                            |
| C4           | varchar | 选项4          |                            |
| Ans          | varchar | 正确选项       | 必须与某个选项完全相同     |
| Category     | varchar | 问题内容的类别 | 如: 问作者, 书中人物, 情节 |


## User Data

| Attriubute | Type    | Translation |
| :--------- | :------ | :---------- |
| Id         | int     | 编号        |
| Name       | varchar | 姓名        |
| Gender     | char    | 性别        |
| Telephone  | varchar | 电话        |
| Password   | varchar | 密码        |
| Brief      | varchar | 简介        |


## Test data

| Attriubute  | Type  | Translation              |
| :---------- | :---- | :----------------------- |
| Userid      | int   | 用户id                   |
| Score       | float | 得分                     |
| Start       | int   | 开始时间(使用unix时间戳) |
| End         | int   | 结束时间(使用unix时间戳) |
| Duration    | int   | 答题时长(秒)             |
| A1          | int   |                          |
| A2          | int   |                          |
| A3          | int   |                          |
| A4          | int   |                          |
| A5          | int   |                          |
| B1          | int   |                          |
| B2          | int   |                          |
| B3          | int   |                          |
| B4          | int   |                          |
| B5          | int   |                          |
| Questionnum | int   | 问题数量                 |
| Rightnum    | int   | 正确数量                 |
| Wrongnum    | int   | 错误数量                 |
| Emptynum    | int   | 未回答数量               |