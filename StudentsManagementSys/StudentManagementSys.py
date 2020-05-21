'''
时间：2020-4-22 23:13:49
作者：LF
邮箱：jksj27250#gmail.com
主题：
    学生信息管理系统
内容：
    1.学生信息维护
        1.1.录入学生信息
        1.2.删除学生信息
        1.3.修改学生信息
    2.查询/统计
        2.1.按学生姓名查找
        2.2.按学生ID查找
        2.3.查询并显示所有学生信息
        2.4.统计学生总人数
    3.排序
        3.1升序排序
        3.2降序排序
'''
# -*- coding: UTF-8 -*-
import os, re, sys


# 显示菜单函数
def menu():
    # 输出菜单
    print(""
          "$###################学生信息管理系统#####################$\n"
          "|                                                     |\n"
          "|                      功能菜单                        |\n"
          "|                   1.录入学生信息                      |\n"
          "|                   2.查找学生信息                      |\n"
          "|                   3.删除学生信息                      |\n"
          "|                   4.修改学生信息                      |\n"
          "|                   5.排序学生信息                      |\n" 
          "|                   6.统计学生人数                      |\n"
          "|                   7.显示学生信息                      |\n"
          "|                   0.退出管理系统                      |\n"
          "|                                                     |\n"
          "$#####################################################$"
          "")


# 保存学生信息到文件
def save(student):
    try:
        student_txt = open("student_information.txt", 'a')  # 以追加的方式打开
    except Exception as e:
        student_txt = open("student_information.txt", 'W')  # 文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info) + '\n')  # 按行存储，添加换行符
    student_txt.close()  # 关闭文件


# 录入学生信息函数
def insert():
    print("开始录入学生信息......\n")
    studentList = []  # 保存学生信息列表
    mark = True
    while mark:
        id = input("请输入学生学号ID（如1001）：")
        if not id:
            break
        name = input("请输入学生姓名：（如赵海棠):")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩：(如100）"))
            python = int(input("请输入python成绩：（如100）"))
            C = int(input("请输入C语言成绩：（如100)"))
        except:
            print("输入无效，不是整数数值......重新录入信息\n")
            continue
        # 将学生成绩保存到字典
        stdent = {"ID": id, "name": name, "english": english, "python": python, "C": C}
        studentList.append(stdent)  # 将学生字典添加到列表
        inputMark = input("是否继续添加？（Y/N):")
        if inputMark == 'Y':
            mark = True
        elif inputMark == "Y":
            mark = True
        else:
            mark = False
    save(studentList)
    print("学生信息录入完毕！！！\n")


# 将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:  # 如果没有要显示的数据
        print("(^@_@^) 无数据信息 （^@_@^)\n")
        return
    # 定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^18}\t{:^4}\t{:^10}\t{:^12}"
    print(format_title.format("ID", "姓名", "英语成绩", "Python成绩",
                              "C语言成绩", "总成绩"))
    # 定义具体内容显示格式
    format_data = "{:^6}{:^14}\t{:^12}\t{:^12}\t{:^12}\t{:^14}"
    for info in studentList:  # 通过for循环将列表中的数据全部显示出来
        English = int(info.get("english"))
        Python = int(info.get("python"))
        C = int(info.get("C"))
        Sum = English+Python+C
        #print(info.get("ID"),info.get("name"),English,Python,C,Sum)
        print(format_data.format(info.get("ID"), info.get("name"), English,Python,C,Sum))

# 查找学生信息函数
def search():
    print("开始查找学生信息......\n")
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists("student_information.txt"):
            mode = input("按ID查找输入1；按姓名查找输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("输入有误，重新输入\n")
                search()
            with open("student_information.txt", "r") as file:
                student = file.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id != "":
                        if d['ID'] == id:
                            student_query.append(d)
                    elif name != "":
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            inputMark = input("是否继续查询？（y/Y/N/n）:")
            if inputMark == "y":
                mark = True
            elif inputMark == "Y":
                mark =True
            else:
                mark = False
        else:
            print("暂未保存数据信息……")
            return



# 删除学生信息函数
def delete():
    print("开始删除学生信息......\n")
    show()
    mark = True
    while mark:
        studentId = input("请输入需删除学生ID：")
        if studentId != "":  # 判断输入要删除的学生是否存在
            if os.path.exists("student_information.txt"):  # 判断文件是否存在
                with open("student_information.txt", 'r') as rfile:  # 打开文件
                    student_old = rfile.readlines()  # 读取全部内容
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open("student_information.txt", "w") as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['ID'] != studentId:
                            wfile.write(str(d) + "\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID 为 %s 的学生信息已经删除......" % studentId)
                    else:
                        print("没有找到ID为%s 的学生信息......" % studentId)
            else:
                print("无学生信息......")
                break
            show()
            inputMark = input("是否继续删除？(Y/N):")
            if inputMark == 'Y':
                mark = True
            elif inputMark == 'y':
                mark = True
            else:
                mark = False
    print("删除学生信息结束！！！")


# 修改学生信息函数
def modify():
    print("开始修改学生信息\n")
    show()  # 显示全部学生信息
    if os.path.exists("student_information.txt"):  # 判断文件是否存在
        with open("student_information.txt", "r") as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
            #print(student_old)    #测试
    else:
        return
    student_id = input("请输入要修改的学生ID：(如1001）")
    with open("student_information.txt", "w") as w_file:
        for student in student_old:
            d = dict(eval(student))
            if d["ID"] == student_id:
                print("已经找到该学生，可以修改其信息！")
                while True:  # 输入要修改的信息
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入python成绩："))
                        d["C"] = int(input("请输入C语言成绩："))
                    except:
                        print("输入有误，重写输入！！！\n")
                    else:
                        break  # 跳出循环
                student = str(d)  # 将字典转化为字符串
                w_file.write(student + '\n')  # 将修改信息写入文件
                print("修改成功！！！")
            else:
                w_file.write(student)  # 将未修改信息写入文件
    mark = input("是否继续修改其他学生信息？（Y/N)\n")
    if mark == 'Y':
        modify()
    elif mark == 'y':
        modify()  # 重新执行修改操作
    else:
        show()  # 显示修改后所有学生信息


# 排序
def sort():
    print("排序\n")
    show()
    new = []
    if os.path.exists("student_information.txt"):
        with open("student_information.txt", "r") as r_file:
            student_old = r_file.readlines()
        for lisr in student_old:
            d = dict(eval(lisr))
            new.append(d)
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":
        ascORdescBool = False
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("您的输入有误，请重新输入：")
        sort()
    mode = input("请选择排序方式：1：按英语成绩排序 2：按python成绩排序 3：按C语言成绩排序0：按总成绩排序")
    if mode == "1":
        new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":  # 按Python成绩排序
        new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":  # 按C语言成绩排序
        new.sort(key=lambda x: x["C"], reverse=ascORdescBool)
    elif mode == "0":  # 按总成绩排序
        new.sort(key=lambda x: x["english"] + x["python"] + x["C"],reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(new)  # 显示排序结果



# 统计学生总数
def total():
    print("统计学生总数\n")
    if os.path.exists("student_information.txt"):
        with open("student_information.txt", "r") as r_file:
            student_old = r_file.readlines()
            if student_old :
                print("一共有%d名学生！"%len(student_old))
            else :
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息")



# 显示所有学生信息
def show():
    print("开始显示所有学生信息\n")
    student_new = []
    if os.path.exists("student_information.txt"):
        with open("student_information.txt", 'r') as rfile:
            student_old = rfile.readlines()  # 读取全部内容
        for list in student_old:
            student_new.append(eval(list))  # 将找到的学生信息保存到列表中
        if student_new:
            show_student(student_new)
    else:
        print("占未保存学生信息\n")
    print("已录入学生信息答应完成！！！")


# 主函数
def main():
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()  # 显示菜单
        option = input("请选择：")  # 选择菜单项
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:  # 退出系统
                print("您已经退出学生信息系统！\n")
                ctrl = False
            elif option_int == 1:  # 录入学生信息
                insert()
            elif option_int == 2:  # 查找学生成绩信息
                search()
            elif option_int == 3:  # 删除学生成绩信息
                delete()
            elif option_int == 4:  # 修改学生成绩信息
                modify()
            elif option_int == 5:  # 排序
                sort()
            elif option_int == 6:  # 统计学生总数
                total()
            elif option_int == 7:  # 显示所有学生信息
                show()


if __name__ == '__main__':
    main()
