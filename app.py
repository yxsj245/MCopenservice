#-------------------------导入运行库--------------------------
import urllib.request
import easygui
import shutil
import subprocess
import os
import urllib.request
import requests
from flask import Flask
from tqdm import tqdm
#--------------------------资源下载链接集合----------------------
#解压软件
decompressionapp = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/app/winrar-x64-611.exe'
#java17
java17down = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/Java/openjdk-17%2B35_windows-x64_bin.zip'
#java16
java16down = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/Java/openjdk-16%2B36_windows-x64_bin.zip'
#java8
java8down = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/Java/openjdk-8u43-windows-i586.zip'
#forge1.19.4
forge1194 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/forge-1.19.4-45.0.66-installer.jar'
#bukkit1.19.4
bukkit1194 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/craftbukkit-1.19.4.jar'
#paper1.20.1
paper1201 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/paper/paper-1.20.1-55.jar'
#paper1.19.4
paper1194 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/paper/paper-1.19.4-545.jar'
#spigot1.19.4
spigot1194 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/spigot-1.19.4.jar'
#LLBDS1.20.01
llbds12001='http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/LLBDS/LLBDS2.14.1-1.20.1.zip'
#LLBDS1.19.83
llbds11983 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/LLBDS/LLBDS2.13.1-1.19.83.zip'
#BDS1.20.01
bds12001 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/BDS/bedrock-server-1.20.1.02.zip'
#BDS1.19.83
bds11983 = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/server/BDS/bedrock-server-1.19.83.01.zip'
#C++运行环境
cjiajia = 'http://mcjavaauto.oss-cn-beijing.aliyuncs.com/app/VisualCppRedist_AIO_x86_x64.exe'
#--------------------------方法库-------------------------------
#下载文件并重命名的方法
def dowm(url,name):
    url = url
    response = urllib.request.urlopen(url)
    file_size = int(response.headers["Content-Length"])
    progress_bar = tqdm(total=file_size, unit="B", unit_scale=True, ncols=80)

    with open(name, "wb") as file:
        downloaded_size = 0
        while True:
            buffer = response.read(1024)
            if not buffer:
                break
            file.write(buffer)
            downloaded_size += len(buffer)
            progress_bar.update(len(buffer))


    progress_bar.close()
    print('文件下载完毕')
#移动文件方法
def move(name,path):
    current_directory = os.getcwd()

    file_name = name

    target_directory = path

    current_file_path = os.path.join(current_directory, file_name)
    target_file_path = os.path.join(target_directory, file_name)

    shutil.move(current_file_path, target_file_path)

    print("文件移动完成，文件已保存在:", target_file_path)

# 解压文件方法
def rarzip(pathone,pathtwo):
    os.popen(r"start winrar -o x %s %s" % (pathone,pathtwo))
    print('文件解压完毕')

#写入文件
def writfile(content):

    current_directory = os.getcwd()

    file_name = "run.cmd"
    file_path = os.path.join(current_directory, file_name)

    file_content = content

    with open(file_path, "w") as file:
        file.write(file_content)
    print("文件已创建并写入成功:", file_path)

#运行程序
def run(name):
    current_directory = os.getcwd()

    program_path = os.path.join(current_directory, name)

    subprocess.run(program_path)
    print('程序执行完毕')

#-----------------------------程序方法----------------------------------------
#快速安装Java服务端
def expresssetup():
    # 下载解压缩软件
    print('开始下载压缩软件')
    dowm(decompressionapp, 'winrar-x64-611.exe')
    easygui.msgbox(
        '下载完成，接下来将自动运行安装程序，您只需按照要求进行安装，请不要改动安装目录，保持默认即可，一直点击下一步')
    run('winrar-x64-611.exe')

    # 创建Java目录
    os.mkdir('C:\Java')
    print('Java运行环境目录创建成功，位于C盘根目录')
    # 选择并下载对应的Java
    versions = easygui.buttonbox(
        '请输入开服Java环境版本(温馨提示：Java17可以兼容大部分1.19的核心版本，可以自己根据版本号往下推Java版本，1.18可以选择Java16；更老版本可以选择Java8)',
        choices=['Java17', 'Java16', 'Java8'])
    java_versions = versions
    server_ram = easygui.integerbox('请输入分配Java的运行内存')
    if versions == 'Java17':
        print('开始下载Java环境')
        dowm(java17down, 'Java17.zip')
        move('Java17.zip', "C:\\Java")
        print('开始解压Java环境包')
        rarzip('C:\Java\Java17.zip', "C:\\Java")

    elif versions == 'Java16':
        print('开始下载Java环境')
        dowm(java16down, 'Java16.zip')
        move('Java16.zip', "C:\\Java")
        print('开始解压Java环境包')
        rarzip('C:\Java\Java16.zip', "C:\\Java")
    else:
        print('开始下载Java环境')
        dowm(java8down, 'Java8.zip')
        move('Java8.zip', "C:\\Java")
        print('开始解压Java环境包')
        rarzip('C:\Java\Java8.zip', "C:\\Java")
    url = easygui.diropenbox(title="选择服务端存放的文件夹路径")
    print(url)
    select = easygui.buttonbox('请选择你要开服的核心', choices=['forge', 'bukkit', 'paper', 'spigot', '自定义核心下载'])
    if select == 'forge':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.19.4'])
        if select == '1.19.4':
            print('开始下载核心文件')
            dowm(forge1194,'forge1.19.4.jar')
            move('forge1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG forge1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    elif select == 'bukkit':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.19.4'])
        if select == '1.19.4':
            print('开始下载核心文件')
            dowm(bukkit1194, 'craftbukkit1.19.4.jar')
            move('craftbukkit1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG craftbukkit1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    elif select == 'paper':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.20.1', '1.19.4'])
        if select == '1.20.1':
            print('开始下载核心文件')
            dowm(paper1201, 'paper1.20.1.jar')
            move('paper1.20.1.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG paper1.20.1.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
        elif select == '1.19.4':
            print('开始下载核心文件')
            dowm(paper1194, 'paper1.19.4.jar')
            move('paper1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG paper1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    elif select == 'spigot':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.19.4'])
        if select == '1.19.4':
            print('开始下载核心文件')
            dowm(spigot1194, 'spigot1.19.4.jar')
            move('spigot1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG spigot1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    else:
        javadowndur = easygui.enterbox('第一步：请输入核心下载链接（必须是访问此链接直接弹出下载文件！）')
        print('正在准备开始下载')
        dowm(javadowndur, 'server.jar')
        move('server.jar', url)
        javadown_veriso = easygui.buttonbox('第二步：请选择Java运行环境版本', choices=['Java17', 'Java16', 'Java8'])
        if javadown_veriso == 'Java17':
            writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG server.jar' % (server_ram))
            move('run.cmd', url)
            easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
        elif javadown_veriso == 'Java16':
            writfile('C:/Java/jdk-16/bin/java.exe -jar -Xmx%sG server.jar' % (server_ram))
            move('run.cmd', url)
            easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
        else:
            writfile('C:/Java/jdk-8/bin/java.exe -jar -Xmx%sG server.jar' % (server_ram))
            move('run.cmd', url)
            easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')

def install():
    java_versions = easygui.buttonbox('请选择您刚才安装的Java环境版本',choices=['Java17', 'Java16', 'Java8'])
    url = easygui.diropenbox(title="选择服务端存放的文件夹路径")
    server_ram = easygui.integerbox('请输入分配Java的运行内存')
    print(url)
    select = easygui.buttonbox('请选择你要开服的核心', choices=['forge', 'bukkit', 'paper', 'spigot', '自定义核心下载'])
    if select == 'forge':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.19.4'])
        if select == '1.19.4':
            print('开始下载核心文件')
            dowm(forge1194,'forge1.19.4.jar')
            move('forge1.19.4', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG forge1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    elif select == 'bukkit':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.19.4'])
        if select == '1.19.4':
            print('开始下载核心文件')
            dowm(bukkit1194, 'craftbukkit1.19.4.jar')
            move('craftbukkit1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG craftbukkit1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    elif select == 'paper':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.20.1', '1.19.4'])
        if select == '1.20.1':
            print('开始下载核心文件')
            dowm(paper1201, 'paper1.20.1.jar')
            move('paper1.20.1.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG paper1.20.1.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
        elif select == '1.19.4':
            print('开始下载核心文件')
            dowm(paper1194, 'paper1.19.4.jar')
            move('paper1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG paper1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    elif select == 'spigot':
        select = easygui.buttonbox('选择你要下载的版本', choices=['1.19.4'])
        if select == '1.19.4':
            print('开始下载核心文件')
            dowm(spigot1194, 'spigot1.19.4.jar')
            move('spigot1.19.4.jar', url)
            if java_versions == 'Java17':
                writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG spigot1.19.4.jar' % (server_ram))
                move('run.cmd', url)
                easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
            else:
                easygui.msgbox('请选择Java17运行环境')
    else:
        javadowndur = easygui.enterbox('第一步：请输入核心下载链接（必须是访问此链接直接弹出下载文件！）')
        print('正在准备开始下载')
        dowm(javadowndur, 'server.jar')
        move('server.jar', url)
        javadown_veriso = easygui.buttonbox('第二步：请选择Java运行环境版本', choices=['Java17', 'Java16', 'Java8'])
        if javadown_veriso == 'Java17':
            writfile('C:/Java/jdk-17/bin/java.exe -jar -Xmx%sG server.jar' % (server_ram))
            move('run.cmd', url)
            easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
        elif javadown_veriso == 'Java16':
            writfile('C:/Java/jdk-16/bin/java.exe -jar -Xmx%sG server.jar' % (server_ram))
            move('run.cmd', url)
            easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')
        else:
            writfile('C:/Java/jdk-8/bin/java.exe -jar -Xmx%sG server.jar' % (server_ram))
            move('run.cmd', url)
            easygui.msgbox('已成功分配完毕，现在您只需前往服务端路径双击运行run.cmd程序按照官方开服向导进行操作即可')

def MCBELLBDS():
    url = easygui.diropenbox(title="选择服务端存放的文件夹路径")
    select = easygui.buttonbox('请选择你要下载的版本',choices=['1.20.01','1.19.83','自定义版本'])
    if select =='1.20.01':
        print('开始下载文件')
        dowm(llbds12001, 'llbds1.20.01.zip')
        move('llbds1.20.01.zip', url)
        rarzip('%s/llbds1.20.01.zip'%(url), url)
        easygui.msgbox('已成功分配完毕，待解压完毕后您只需前往服务端路径双击后缀为exe即可运行')
    elif select =='1.19.83':
        print('开始下载文件')
        dowm(llbds11983, 'llbds1.19.83.zip')
        move('llbds1.19.83.zip', url)
        rarzip('%s/llbds1.19.83.zip'%(url), url)
        easygui.msgbox('已成功分配完毕，待解压完毕后您只需前往服务端路径双击后缀为exe即可运行')
    else:
        BEdowndur = easygui.enterbox('第一步：请输入服务端下载链接（必须是访问此链接直接弹出下载文件！）')
        print('开始下载文件')
        dowm(BEdowndur, 'llbdscustom.zip')
        move('llbdscustom.zip', url)
        rarzip('%s/llbdscustom.zip'%(url), url)
        easygui.msgbox('已成功分配完毕，待解压完毕后您只需前往服务端路径双击后缀为exe即可运行')
def MCBEBDS():
    url = easygui.diropenbox(title="选择服务端存放的文件夹路径")
    select = easygui.buttonbox('请选择你要下载的版本',choices=['1.20.01','1.19.83','自定义版本'])
    if select =='1.20.01':
        print('开始下载文件')
        dowm(bds12001, 'bds1.20.01.zip')
        move('bds1.20.01.zip', url)
        rarzip('%s/bds1.20.01.zip'%(url), url)
        easygui.msgbox('已成功分配完毕，待解压完毕后您只需前往服务端路径双击后缀为exe即可运行')
    elif select =='1.19.83':
        print('开始下载文件')
        dowm(bds11983, 'bds1.19.83.zip')
        move('bds1.19.83.zip', url)
        rarzip('%s/bds1.19.83.zip'%(url), url)
        easygui.msgbox('已成功分配完毕，待解压完毕后您只需前往服务端路径双击后缀为exe即可运行')
    else:
        BEdowndur = easygui.enterbox('第一步：请输入服务端下载链接（必须是访问此链接直接弹出下载文件！）')
        print('开始下载文件')
        dowm(BEdowndur, 'bdscustom.zip')
        move('bdscustom.zip', url)
        rarzip('%s/bdscustom.zip'%(url), url)
        easygui.msgbox('已成功分配完毕，待解压完毕后您只需前往服务端路径双击后缀为exe即可运行')
def environment():
    print('开始下载压缩软件')
    dowm(cjiajia, 'VisualCppRedist_AIO_x86_x64.exe')
    easygui.msgbox('下载完成，接下来将自动运行安装程序，一直点击下一步')
    run('VisualCppRedist_AIO_x86_x64.exe')
def zhix():
    print('执行测试')
#------------------------------主程序入口---------------------------------------
try:
    select = easygui.buttonbox('菜单',choices=['快速安装Java服务端(首次运行)','安装Java服务端(用于快速安装中途出现失败时点击)','基岩LLBDS服务端','基岩BDS服务端','安装C++运行库(基岩服务端开服报错或首次纯系统环境需运行)'])
    if select=='快速安装Java服务端(首次运行)':
        expresssetup()
    elif select == '安装Java服务端(用于快速安装中途出现失败时点击)':
        install()
    elif select == '基岩LLBDS服务端':
        MCBELLBDS()
    elif select =='基岩BDS服务端':
        MCBEBDS()
    elif select =='安装C++运行库(基岩服务端开服报错或首次纯系统环境需运行)':
        environment()
except FileExistsError:
    print('已捕获程序异常，请根据提示排查')
    print('检测到您在C盘根目录已存在名为 Java 的文件夹，请手动前往删除后继续执行')
    input('按任意键重新执行程序....')
    #进行回调函数
    expresssetup()
except Exception as e:
    print('未捕获的程序异常，请保存截图，联系开发者进行处理')
    print('错误输出',str(e))
    input('按任意键退出程序....')
