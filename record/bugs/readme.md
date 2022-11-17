# 问题记录

## 11.06

- [ ] 两台电脑数据库互访

    pymysql.connect(host=db_ip,user='root',password='',charset='utf8')  两台电脑连接同一个网络，将host更改为目标电脑的ip  

    但是报错：pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.38.148:3306' ([Errno 11001] getaddrinfo failed)")

        咩解决，去试了Azure的云服务器，时间不够，没心思整这么多，后面一定要搭建自己的服务器。

    cmd进入mysql:
    
        mysql -h localhost -u root -p





## 11.16 

- [x] 在11.06左右已经将书籍信息爬取完成，但在1106再爬取书籍封面图片时候，发现序号(书籍排名)在变，之前存储方式为按照排名为主键，现在不能通过排名页直接爬取了

        修改了爬虫，通过豆瓣id逐页爬取，虽然很慢就是了，200页也不至于开多线程
- [x] 由于是逐页爬取，爬取到后面ip被ban了.... 尝试过爬取之间sleep()，但也无法解决，好在数据量不大

        还能怎么办，换个网络....
- [x] 发现vscode git一直上传的时候都不是用github的账号.... 烦躁了很久.... 

        对线了四五个小时，发现是本地git配置的是qq邮箱，github是gmail，改了就没事了.... 前面那四五十次push就当吃一堑吧


## 11.17

- [x] 修改mysql密码

        set password for root@localhost = password('');

- [x] 查看所有端口进程，杀死进程

        netstat -ntlp
        kill -9 端口号

- [x] flask 部署到服务器

        if __name__ == "__main__":
	        app.run(host='0.0.0.0',port=80)

- [x] 服务器和本地上传时需要修改-后期可以改成双文件

        database 密码 wgAkYmSE
        main 中的相对路径
        上面那条 改host和port