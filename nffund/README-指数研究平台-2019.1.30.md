# 指数研究平台

项目链接：

个人百度云网盘链接:

## Requirements

```
Python 3.5.2
```
(理论上，只要是Python3，应该都可以)

使用pip3安装的第三方库
```
pandas==0.23.4
Django==2.1.5
pyecharts==0.5.11
```

如果启动django时，仍然报错某些第三方库没装，手动安装即可。

直接使用pip3安装，（理论上，pip3自动选择相应的版本安装，不需要制定版本安装）

```
pip3 install pandas
pip3 install Django
pip3 install pyecharts
```



## Usage

1. cd进入nffund

2. 执行命令，采用Django框架自带的开发服务器。外部浏览器访问服务器的8001端口即可

   ```
   python3 manage.py runserver 8001
   # 本地浏览器访问服务器的8001端口即可
   ```

   默认在本地127.0.0.1:8000端口启动，可以手动改为8001端口

   ```python
   python3 manage.py runserver 0.0.0.0:8001
   # 外网浏览器访问服务器的8001端口即可
   ```

**下面的步骤暂时可以不做：**

3. pip3安装uwsgi，配置uwsgi.ini（重点是端口），用起启动django框架。
4. 安装Nginx服务器，修改nginx.conf文件。配置端口和static静态文件目录（注意nginx.conf中的端口和uwsgi.ini端口一致）

