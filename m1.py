from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QVBoxLayout , QHBoxLayout , QPushButton , QButtonGroup , QMessageBox
from PyQt5.QtGui import QIcon
from os import system

system("cls") 

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dunyo Davlatlari")
        self.setWindowIcon(QIcon("download.png"))
        self.setFixedSize(1000, 850)


        self.answer={
            1 : "Ottava",
            2 : "Berlin",
            3 : "Seul",
            4 : "Tokio",
            5 : "Dehli",
            6 : "Anqara",
            7 : "Bog'dod",
            8 : "Sano",
            9 : "Vashington",
            10:"Tbilisi"

        }

        # 1111 
        self.test1_box = QVBoxLayout()

        
        self.test1_label = QLabel("1.Kanada Poytaxti :")
        self.test1_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Ottava", self)
        self.answer_B = QRadioButton("Toronto", self)
        self.answer_C = QRadioButton("Ontario", self)
        self.test1_group.addButton(self.answer_A)
        self.test1_group.addButton(self.answer_B)
        self.test1_group.addButton(self.answer_C)


    
        self.test1_box.addWidget(self.test1_label)
        self.test1_box.addWidget(self.answer_A)
        self.test1_box.addWidget(self.answer_B)
        self.test1_box.addWidget(self.answer_C)

        

         # 2222 
        self.test2_box = QVBoxLayout()

    
        self.test2_label = QLabel("2.Germaniya Poytaxti :")
        self.test2_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Hamburg", self)
        self.answer_B = QRadioButton("Frankfurt", self)
        self.answer_C = QRadioButton("Berlin", self)
        self.test2_group.addButton(self.answer_A)
        self.test2_group.addButton(self.answer_B)
        self.test2_group.addButton(self.answer_C)

        
        self.test2_box.addWidget(self.test2_label)
        self.test2_box.addWidget(self.answer_A)
        self.test2_box.addWidget(self.answer_B)
        self.test2_box.addWidget(self.answer_C)


         #  3333 
        self.test3_box = QVBoxLayout()

        
        self.test3_label = QLabel("3.Janubiy Koreyaning poytaxti ")
        self.test3_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Seul", self)
        self.answer_B = QRadioButton("Busan", self)
        self.answer_C = QRadioButton("Kvanju", self)
        self.test3_group.addButton(self.answer_A)
        self.test3_group.addButton(self.answer_B)
        self.test3_group.addButton(self.answer_C)


    
        self.test3_box.addWidget(self.test3_label)
        self.test3_box.addWidget(self.answer_A)
        self.test3_box.addWidget(self.answer_B)
        self.test3_box.addWidget(self.answer_C)




         # 4444 
        self.test4_box = QVBoxLayout()

        
        self.test4_label = QLabel("4.Yaponiya poytaxti ")
        self.test4_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Osaka", self)
        self.answer_B = QRadioButton("Tokio", self)
        self.answer_C = QRadioButton("Fukushima", self)
        self.test4_group.addButton(self.answer_A)
        self.test4_group.addButton(self.answer_B)
        self.test4_group.addButton(self.answer_C)

        
        self.test4_box.addWidget(self.test4_label)
        self.test4_box.addWidget(self.answer_A)
        self.test4_box.addWidget(self.answer_B)
        self.test4_box.addWidget(self.answer_C)




         # 5555 
        self.test5_box = QVBoxLayout()

        
        self.test5_label = QLabel("5.Hindiston poytaxti  ")
        self.test5_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Chandanhosur", self)
        self.answer_B = QRadioButton("Dehli", self)
        self.answer_C = QRadioButton("Bangalor", self)
        self.test5_group.addButton(self.answer_A)
        self.test5_group.addButton(self.answer_B)
        self.test5_group.addButton(self.answer_C)


    
        self.test5_box.addWidget(self.test5_label)
        self.test5_box.addWidget(self.answer_A)
        self.test5_box.addWidget(self.answer_B)
        self.test5_box.addWidget(self.answer_C)


        self.left_box=QVBoxLayout()

        self.left_box.addLayout(self.test1_box)
        self.left_box.addLayout(self.test2_box)
        self.left_box.addLayout(self.test3_box)
        self.left_box.addLayout(self.test4_box)
        self.left_box.addLayout(self.test5_box)




        self.test6_box = QVBoxLayout()

        # 6666 
        self.test6_label = QLabel("6.Turkiya poytaxti ")
        self.test6_group=QButtonGroup(self)
        
        self.answer_A = QRadioButton("Istanbul", self)
        self.answer_B = QRadioButton("Izmir", self)
        self.answer_C = QRadioButton("Anqara", self)
        self.test6_group.addButton(self.answer_A)
        self.test6_group.addButton(self.answer_B)
        self.test6_group.addButton(self.answer_C)

        
        self.test6_box.addWidget(self.test6_label)
        self.test6_box.addWidget(self.answer_A)
        self.test6_box.addWidget(self.answer_B)
        self.test6_box.addWidget(self.answer_C)

    

         # 7777 
        self.test7_box = QVBoxLayout()

    
        self.test7_label = QLabel("7.Iroq poytaxti ")
        self.test7_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Bog'dod", self)
        self.answer_B = QRadioButton("Mosul", self)
        self.answer_C = QRadioButton("Nosiriya", self)
        self.test7_group.addButton(self.answer_A)
        self.test7_group.addButton(self.answer_B)
        self.test7_group.addButton(self.answer_C)


        
        self.test7_box.addWidget(self.test7_label)
        self.test7_box.addWidget(self.answer_A)
        self.test7_box.addWidget(self.answer_B)
        self.test7_box.addWidget(self.answer_C)


         #  8888
        self.test8_box = QVBoxLayout()


        self.test8_label = QLabel("8.Yaman poytaxti ")
        self.test8_group=QButtonGroup(self)

        self.answer_A = QRadioButton("Adan", self)
        self.answer_B = QRadioButton("Sano", self)
        self.answer_C = QRadioButton("Taiz", self)
        self.test8_group.addButton(self.answer_A)
        self.test8_group.addButton(self.answer_B)
        self.test8_group.addButton(self.answer_C)


    
        self.test8_box.addWidget(self.test8_label)
        self.test8_box.addWidget(self.answer_A)
        self.test8_box.addWidget(self.answer_B)
        self.test8_box.addWidget(self.answer_C)




         # 9999
        self.test9_box = QVBoxLayout()

    
        self.test9_label = QLabel("9.Amerika Qo'shman Shtatlari poytaxti ")
        self.test9_group=QButtonGroup(self)
        self.answer_A = QRadioButton("Vashington", self)
        self.answer_B = QRadioButton("Filadelfiya", self)
        self.answer_C = QRadioButton("Arizona", self)
        self.test9_group.addButton(self.answer_A)
        self.test9_group.addButton(self.answer_B)
        self.test9_group.addButton(self.answer_C)


    
        self.test9_box.addWidget(self.test9_label)
        self.test9_box.addWidget(self.answer_A)
        self.test9_box.addWidget(self.answer_B)
        self.test9_box.addWidget(self.answer_C)




         # 10 10 10 10  
        self.test10_box = QVBoxLayout()

        
        self.test10_label = QLabel("10. Gruziya poytaxti ")
        self.test10_group=QButtonGroup(self)

        self.answer_A = QRadioButton("Batumi", self)
        self.answer_B = QRadioButton("Suxumi", self)
        self.answer_C = QRadioButton("Tbilisi", self)
        self.test10_group.addButton(self.answer_A)
        self.test10_group.addButton(self.answer_B)
        self.test10_group.addButton(self.answer_C)
        self.submit_button=QPushButton("Submit " , self)
        self.submit_button.setStyleSheet("""
          color : blue ;
""")  
        

        self.submit_button.setFixedSize(200 , 50)

        

        self.test10_box.addWidget(self.test10_label)
        self.test10_box.addWidget(self.answer_A)
        self.test10_box.addWidget(self.answer_B)
        self.test10_box.addWidget(self.answer_C)
        self.test10_box.addWidget(self.submit_button)
        


        self.right_box=QVBoxLayout()

        self.right_box.addLayout(self.test6_box)
        self.right_box.addLayout(self.test7_box)
        self.right_box.addLayout(self.test8_box)
        self.right_box.addLayout(self.test9_box)
        self.right_box.addLayout(self.test10_box)
        
        

                                      



        self.master_layaut=QHBoxLayout()
        self.master_layaut.addLayout(self.left_box)
        self.master_layaut.addLayout(self.right_box)
        self.setLayout(self.master_layaut)

        self.submit_button.clicked.connect(self.clicked_btn)
        self.setStyleSheet("""
          QWidget {
          font-size : 22px 
                           }
    
                           
""") 
        

    def clicked_btn(self):
        t1 = self.test1_group.checkedButton()
        t2 = self.test2_group.checkedButton()
        t3 = self.test3_group.checkedButton()
        t4 = self.test4_group.checkedButton()
        t5 = self.test5_group.checkedButton()
        t6 = self.test6_group.checkedButton()
        t7 = self.test7_group.checkedButton()
        t8 = self.test8_group.checkedButton()
        t9 = self.test9_group.checkedButton()
        t10 = self.test10_group.checkedButton()

        score = 0

        if t1:
            clicked_answer = t1.text()
            if clicked_answer == self.answer[1]:
                score += 1

        if t2:
            clicked_answer = t2.text()
            if clicked_answer == self.answer[2]:
               score += 1

        if t3:
            clicked_answer = t3.text()
            if clicked_answer == self.answer[3]:
             score += 1

        if t4:
            clicked_answer = t4.text()
            if clicked_answer == self.answer[4]:
                score += 1

        if t5:
            clicked_answer = t5.text()
            if clicked_answer == self.answer[5]:
                score += 1

        if t6:
            clicked_answer = t6.text()
            if clicked_answer == self.answer[6]:
                score += 1

        if t7:
             clicked_answer = t7.text()
             if clicked_answer == self.answer[7]:
                score += 1

        if t8:
            clicked_answer = t8.text()
            if clicked_answer == self.answer[8]:
                 score += 1

        if t9:
            clicked_answer = t9.text()
            if clicked_answer == self.answer[9]:
                score += 1

        if t10:
            clicked_answer = t10.text()
            if clicked_answer == self.answer[10]:
                score += 1

        msbox = QMessageBox(self)
    
        if t1 and t2 and t3 and t4 and t5 and t6 and t7 and t8 and t9 and t10:
            msbox.setText(f"Test yakunlandi! Siz {score} / 10 savolga to'g'ri javob berdingiz")
            msbox.setIcon(QMessageBox.Information)
        else:
            msbox.setText("Testni yakunlamadingiz! Iltimos, barcha savollarga javob bering.")
            msbox.setIcon(QMessageBox.Warning)

        msbox.exec_()
    
    

app = QApplication([])
main_window = Window()
main_window.show()
app.exec_()
        
   