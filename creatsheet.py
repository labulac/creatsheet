from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QMessageBox
from PyQt5.QtCore import *
from Ui_creatsheet import Ui_MainWindow
import sys, requests, threading, time, openpyxl, shutil, os, configparser,subprocess


# 自定义信号源
class MySignals(QObject):
    update_object_text = pyqtSignal(QObject, str)


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)
        
        self.currentversion = "17"
        self.download_finish = '0'

        self.pushButton_3.clicked.connect(self.quit)
        self.pushButton.clicked.connect(self.create_new_sheet)
        self.pushButton_2.clicked.connect(self.write_date)

        # 灰度显示最大化与关闭按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)

        self.ms = MySignals()
        self.ms.update_object_text.connect(self.update_gui_text)

        yiyan_update_thread = threading.Thread(target=self.yiyan_update)
        yiyan_update_thread.start()

    def conf(self):
        # 检查配置是否存在
        if os.path.isfile("upgrade.bat"):
            os.remove("upgrade.bat")

        try:
            requests.get('https://sc.ftqq.com/SCU126653T812824e9c91dc2707f0f712c5cc598bd5faf9a749f235.send?text=creatsheet启动啦~')
            github_net = 'https://cdn.jsdelivr.net/gh/labulac/creatsheet@main/creatsheet_info.js'
            github_conf = requests.get(github_net).text

            if github_conf != "":
                with open('D:/labulac.conf', 'w') as f:
                    f.write(github_conf)
                print('更新最新配置完成！')
        except:
            print('检查最新配置失败，网络异常！')

            if os.path.exists('D:/labulac.conf'):
                print('配置存在，飘过~~')
            else:
                conf = open("D:/labulac.conf", 'w')
                TempList = "[dir]\n"
                TempList += "yuan=D:/muban.xlsx\n"
                TempList += "xian=D:/sheet/\n"
                TempList += "[update]\n"
                TempList += "newversion=17\n"
                TempList += "downloadurl=https://cdn.jsdelivr.net/gh/labulac/qd@master/18.zip\n"
                TempList += "[yiyan]\n"
                TempList += "yiyan=https://v1.jinrishici.com/rensheng.txt\n"
                conf.write(TempList)
                conf.close()
                print('默认配置已经生成！')

        cf = configparser.ConfigParser()
        cf.read("D:/labulac.conf", encoding="utf-8")

        self.yuan = cf.get("dir", "yuan")
        self.xian = cf.get("dir", "xian")
        self.newversion = cf.get("update", "newversion")
        self.downloadurl = cf.get("update", "downloadurl")
        self.yiyan_url = cf.get("yiyan", "yiyan")

    def update_gui_text(self, fb, text):
        fb.setText(str(text))

    def yiyan_update(self):
        
        # 获取配置文件
        self.conf()
        
        try:
            yiyan_text = requests.get(self.yiyan_url).text
            
            self.ms.update_object_text.emit(self.yiyan_label, str(yiyan_text))
            # 固定窗口大小
            self.setFixedSize(self.width(), self.height())
            
            self.check_update()
            
        except:
            print("网络错误")
            yiyan_text = ("开心每一天！")

            self.ms.update_object_text.emit(self.yiyan_label, str(yiyan_text))
            # 固定窗口大小
            self.setFixedSize(self.width(), self.height())
        


    def check_update(self):
        
        if self.currentversion < self.newversion:
            self.checkupdate = True
        else:
            self.checkupdate = False
            print("没有发现新的版本")
            
        if self.checkupdate == True:
            print("发现新的版本！！！")
            newfile = requests.get(self.downloadurl)
            try:
                with open('creatsheet1.exe', "wb") as code:
                    code.write(newfile.content)
                    
                self.download_finish = '1'
                self.ms.update_object_text.emit(self.pushButton_3, str('重启并更新'))
            except:
                self.download_finish = '0'
                requests.get(
                    'https://sc.ftqq.com/SCU126653T812824e9c91dc2707f0f712c5cc598bd5faf9a749f235.send?text=checksheet下载失败啦~'
                )
                
    def quit(self):
        if self.download_finish == '1':
            self.WriteRestartCmd("creatsheet.exe")
            
        sys.exit()
        
    def WriteRestartCmd(self,exe_name):
        b = open("upgrade.bat", 'w')
        TempList = "@echo off\n"
        TempList += "if not exist " + exe_name + " exit \n"
        TempList += "timeout /nobreak /t 3\n"
        TempList += "del " + os.path.realpath(sys.argv[0]) + "\n"
        TempList += "rename creatsheet1.exe creatsheet.exe\n"
        TempList += "start " + exe_name
        b.write(TempList)
        b.close()
        subprocess.Popen("upgrade.bat")

    def create_new_sheet(self):
        if self.lineEdit.text() != '':
            try:
                if os.path.exists(self.xian + self.lineEdit.text() +
                                  ".xlsx") is True:
                    self.ms.update_object_text.emit(self.pushButton,
                                                    str("账单名称已存在"))
                else:
                    shutil.copy(self.yuan,
                                self.xian + self.lineEdit.text() + ".xlsx")
                    self.pushButton.setEnabled(False)
                    self.ms.update_object_text.emit(self.pushButton,
                                                    str("已创建"))
                self.pushButton_2.setEnabled(True)
            except:
                print("路径不正确!")
                print(self.comboBox_4.currentText() + '年' +
                      self.comboBox_5.currentText() + '月' +
                      self.comboBox_6.currentText() + '日')
        else:
            print("账单名称为空！")

    def write_date(self):
        cal2 = self.comboBox_4.currentText(
        ) + '年' + self.comboBox_5.currentText(
        ) + '月' + self.comboBox_6.currentText() + '日'

        cal1 = self.comboBox_3.currentText(
        ) + '年' + self.comboBox_2.currentText(
        ) + '月' + self.comboBox_1.currentText() + '日'

        try:

            wb = openpyxl.load_workbook(self.xian + self.lineEdit.text() +
                                        ".xlsx")
            sheet = wb['Sheet1']

            sheet['A2'].value = cal1
            sheet['C2'].value = cal2
            wb.save(self.xian + self.lineEdit.text() + ".xlsx")
            self.pushButton_2.setEnabled(False)
            self.ms.update_object_text.emit(self.pushButton_2, str("已写入完成"))
        except:
            print("写入失败")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())