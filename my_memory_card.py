from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import*
from random import shuffle
from random import *

class Question():
    def __init__(self, answer, rqBa, wqBa1, wqBa2, wqBa3):
        self.answer = answer
        self.rqBa = rqBa
        self.wqBa1 = wqBa1
        self.wqBa2 = wqBa2
        self.wqBa3 = wqBa3

def ask(q: Question):
    answer.setText(q.answer)
    ask1.setText(q.rqBa)
    ask2.setText(q.wqBa1)
    ask3.setText(q.wqBa2)
    ask4.setText(q.wqBa3)    

    gBa.hide()
    gB.show()
    b1.setText('Ответить')

    gBr.setExclusive(False)
    ask1.setChecked(False)
    ask2.setChecked(False)
    ask3.setChecked(False)
    ask4.setChecked(False)
    gBr.setExclusive(True)

    shuffle(answers)
    layV1M.addWidget(answers[0])
    layV1M.addWidget(answers[1])
    layV2.addWidget(answers[2])
    layV2.addWidget(answers[3])

def ca():
    if ask1.isChecked():
        sc(tru)
        ans2.setText(tru)
        mw.score += 1
        mw.total += 1
    elif ask2.isChecked or ask3.isChecked or ask4.isChecked :
        sc(fls)
        ans2.setText(fls)
        mw.total += 1
    else:
        sc(mss)
        ans2.setText(mss)   

def sc(ans2):
    gB.hide()
    gBa.show()
    b1.setText('Следующий вопрос')

def sq():
    gBa.hide()
    gB.show()
    b1.setText('Ответить')
    gBr.setExclusive(False)
    ask1.setChecked(False)
    ask2.setChecked(False)
    ask3.setChecked(False)
    ask4.setChecked(False)
    gBr.setExclusive(True)

def nc():
    mw.curq += 1
    if mw.curq >= len(quests):
        mw.curq = 0
    q = quests[mw.curq]
    ask(q)
    
def click_OK():
    if b1.text() == 'Ответить':
        ca()
    elif b1.text() == 'Следующий вопрос':
        nc()

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')
mw.resize(500,300)
mw.show()

gBr = QButtonGroup()
ask1 = QRadioButton('')
ask2 = QRadioButton('')
ask3 = QRadioButton('')
ask4 = QRadioButton('')
mw.curq = -1
gBr.addButton(ask1)
gBr.addButton(ask2)
gBr.addButton(ask3)
gBr.addButton(ask4)
answers = [ask1, ask2, ask3, ask4]
rqBa = ask1
wqBa1 = ask2
wqBa2 = ask3
wqBa3 = ask4
mw.score = 0
mw.total = 0


tru = 'Правильный ответ'
fls = 'Неправильный ответ'
mss = 'Вы не выбрали вариант ответа'

#1
answer = QLabel('Какой национальности не существует?')
gB = QGroupBox('Варианты ответов')
b1 = QPushButton('Ответить')

#2
gBa = QGroupBox('Результат ответа')
ans2 = QLabel('Правильно/неправильно')

gB.show()
gBa.hide()

#лэйауты для gB
layoutH_quest = QHBoxLayout()   
layV1M = QVBoxLayout()
layV2 = QVBoxLayout()

#прикрепление лэйаутов в gB
layoutH_quest.addLayout(layV1M)
layoutH_quest.addLayout(layV2)
gB.setLayout(layoutH_quest)

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutV = QVBoxLayout()

#прикрепление лэйаутов в mw
layoutH1.addWidget(answer, alignment = Qt.AlignCenter)
layoutH2.addWidget(gB, alignment = Qt.AlignVCenter)
layoutH2.addWidget(gBa, alignment = Qt.AlignVCenter)
layoutH3.addWidget(b1, alignment = Qt.AlignCenter)
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2) 
layoutV.addLayout(layoutH3)
mw.setLayout(layoutV)

layoutH3.addStretch(1)
layoutH3.addWidget(b1, stretch = 3)
layoutH3.addStretch(1)

line_questV = QVBoxLayout()

line_questV.addWidget(ans2, alignment = Qt.AlignLeft)
gBa.setLayout(line_questV)

#нажатие кнопки
quests = []
quests.append(Question('Какой национальности не существует?', 'Смурфы', 'Чулымцы', 'Энцы', 'Алеуты'))
quests.append(Question('вопрос2', 'ответ2-1', 'ответ2-2', 'ответ2-3', 'ответ2-4'))
quests.append(Question('вопрос3', 'ответ3-1', 'ответ3-2', 'ответ3-3 ', 'ответ3-4'))
quests.append(Question('вопрос4', 'ответ4-1', 'ответ4-2', 'ответ4-3', 'ответ4-4'))
shuffle(quests)
nc()
b1.clicked.connect(click_OK)
app.exec_()

#статистика
print('Статистика')
print('Правиьных ответов', mw.score , 'из' , mw.total)
print('Процент правильных ответов:', mw.score/mw.total*100)