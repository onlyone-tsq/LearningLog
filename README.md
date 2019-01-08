#LearningLog
#本代码使用了python3.4、django-2.14、bootstrap3、uwsgi-2.0.17、nginx-1.8，请自行下载相应版本
#下载代码后，请执行命令，在服务器上创建数据库 python manage.py migrate
#修改settings.py文件，将ALLOWED_HOSTS修改为你的IP或域名
#若有静态文件，请执行命令 python manage.py collectstatic
#根据你的项目要求，修改learning_log.ini文件
#若需与nginx配合使用，请在nginx.conf中添加server段
server {
        listen 80;                                                   #默认端口80，可根据实际要求更改
        server_name 192.168.0.253;                                   #域名地址，根据实际IP或者域名填写
        root /home/pi/django/LearningLog_Django;                     #项目的绝对路径
        index index.html;

        location /static { 
               alias /home/pi/django/LearningLog_Django/static;          #静态资源访问配置
            }
    
        location / {
            include /etc/nginx/uwsgi_params;                         #调用uwsgi模块
            uwsgi_pass 127.0.0.1:8000;                               #uwsgi模块指向的地址，这里和uwsgi.ini的socket配置一致
        }   
    }   

#配置好后，启动应用
#后台启动uwsgi
uwsgi learning_log.ini -d /home/pi/django/log/uwsgi.log
#启动nginx
/etc/init.d/nginx -s reload