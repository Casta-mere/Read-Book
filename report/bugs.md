# 问题记录

# 11.06

- [ ] 两台电脑数据库互访

    pymysql.connect(host=db_ip,user='root',password='',charset='utf8')  两台电脑连接同一个网络，将host更改为目标电脑的ip  

    但是报错：pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.38.148:3306' ([Errno 11001] getaddrinfo failed)")

    cmd进入mysql:
    
        mysql -h localhost -u root -p

- [ ] 