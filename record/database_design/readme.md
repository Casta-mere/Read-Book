# Design for database

| Attrbute      | Translation | Type    | Chinese book | Foreign book |
| :------------ | :---------- | :------ | :----------: | :----------: |
| Id            | 排名        | int     |   &check;    |   &check;    |
| Name          | 书名        | varchar |   &check;    |   &check;    |
| Author        | 作者        | varchar |   &check;    |   &check;    |
| Country       | 国家        | varchar |   &check;    |   &check;    |
| Publisher     | 出版社      | varchar |   &check;    |   &check;    |
| Year          | 出版日期    | varchar |   &check;    |   &check;    |
| Page          | 页数        | int     |   &check;    |   &check;    |
| Price         | 定价        | float   |   &check;    |   &check;    |
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