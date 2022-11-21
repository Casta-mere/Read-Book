# Code

## 主页标签栏
- Home  
  滚动栏#1界面放intro，#2放test的intro和link
- Books  
  放top200书籍图片&简介，图片放上对应链接，可跳转至豆瓣(图片--豆瓣<a></a>标签href，点击详情--数据库，索引固定不滚动)
- Knowledge  
  陈列知识点？（可不要）
- Test  
  测试界面(禁止页面滚动，索引固定不滚动，#testid--0为开始界面，1~25对应题目，取的时候注意+1/-1的问题)
- Stasistics  
  数据界面
- profile  
  存放用户的信息
  
## 相关网页
- Flask+雷达图  https://blog.csdn.net/weixin_43836098/article/details/91347483
- https://blog.csdn.net/qq_36288559/article/details/112317273 
- 禁止html页面滚动  https://www.php.cn/div-tutorial-484001.html
- html内容固定不滚动  https://blog.csdn.net/qq_44034384/article/details/94180393


## 文件描述

| 文件名          | 文件描述                                 |
| :-------------- | :--------------------------------------- |
| database        | 数据库相关                               |
| question        | 问题相关                                 |
| static          | 样式(css)及图片                          |
| templates       | HTML相关                                 |
| webcrawer       | 爬虫相关                                 |
| control.py      | 控制类, 对前后端, 爬虫等进行封装后的使用 |
| main.py         | 本地运行                                 |
| reset_server.py | 重置服务器端数据                         |
| reset.py        | 重置本地端数据                           |
| server.py       | 服务器运行                               |
| testFlask.py    | 前端的接入口                             |