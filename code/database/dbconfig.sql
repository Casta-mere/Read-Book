
insert into mysql.user(host,user,authentication_string,ssl_cipher,x509_issuer,x509_subject) values('%', 'castamere','123456', '','','');

insert into mysql.user(host,user,authentication_string,ssl_cipher,x509_issuer,x509_subject) values('%', 'juki', password('juki233'), '','','');

update user set host = '%' where user = 'root';

