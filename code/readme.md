# Code

## 主页标签栏
- Home  
  滚动栏#1界面放intro，#2放test的intro和link
- Books  
  放top200书籍图片&简介，图片放上对应链接，可跳转至豆瓣(图片--豆瓣<a>标签href，点击详情--数据库，索引固定不滚动)
- Knowledge  
  陈列知识点？（可不要）
- Test  
  测试界面(禁止页面滚动，索引固定不滚动，#testid--0为开始界面，1~25对应题目，取的时候注意+1/-1的问题)
- Stasistics  
  数据界面
- profile  
  存放用户的信息

## templates
- index.html  主页
- books.html  书籍简介
- bookDetail.html  书籍详情
- test.html  测试页
- statistics.html 数据页
- profile.html 个人信息页（也是登录/注册界面）
- validation.html 认证html
- model.html 用于debug的html（现存test li选择更改class的内容）

## 相关网页
- Flask+雷达图  https://blog.csdn.net/weixin_43836098/article/details/91347483
- 禁止html页面滚动  https://www.php.cn/div-tutorial-484001.html
- html内容固定不滚动  https://blog.csdn.net/qq_44034384/article/details/94180393
- html 内容根据屏幕大小变 https://blog.csdn.net/qq_38004125/article/details/108060396


## 文件描述

| 文件名    | 文件描述        |
| :-------- | :-------------- |
| database  | 数据库相关      |
| static    | 样式(css)及图片 |
| templates | HTML相关        |
| webcrawer | 爬虫相关        |
