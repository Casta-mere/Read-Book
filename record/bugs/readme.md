# 问题记录

## 11.06

- [x] 两台电脑数据库互访

    pymysql.connect(host=db_ip,user='root',password='',charset='utf8')  两台电脑连接同一个网络，将host更改为目标电脑的ip  

    但是报错：pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.38.148:3306' ([Errno 11001] getaddrinfo failed)")

        咩解决，去试了Azure的云服务器，时间不够，没心思整这么多，后面一定要搭建自己的服务器。

    cmd进入mysql:
    
        mysql -h localhost -u root -p
        
        linux查看mysql初始化密码
        sudo cat /etc/mysql/debian.cnf


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
        main 中的相对路径(已解决)
        上面那条 改host和port(已解决)
        
- [x] ssh关闭时不结束进程

        screen -S 窗口名 :新建窗口
        screen -ls : 列出当前窗口
        screen -r 窗口号 : 回到指定窗口
        exit : 删除当前窗口
        Ctrl+a d : 退出当前窗口
        https://blog.csdn.net/m0_46159309/article/details/108355180


## 11.19

- [x] 测试题目限制为了10道题，可能有的书不够10道题

## 11.20
- [x] uml类图生成

        pyreverse -o dot -p Pyreverse 路径/
        ctrl+k v 开启预览
        http://www.webgraphviz.com/ 在线预览
        https://svgtopng.com/ svg to png

- [x] latex插入svg图片

        https://blog.csdn.net/dl962454/article/details/114479159

## 11.21
- [ ] 多用户登录问题
	
        尝试了的方法：
        多线程
        多进程
        修改全局变量

未能实现多用户登录。由于使用全局变量globals在函数间进行传参，多线程共享全局变量导致同时只能一个用户登录。期间尝试过多进程，把globals换为flask框架下的g对象，将全局变量改写为类对象等。但未成功，后期会继续改进。