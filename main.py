import sqlite3
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class UsaBanco:
  def __init__(self, name):
    self.name = name

  def listarRegistros(self):
    db = sqlite3.connect(self.name + ".db")
    lista = list(db.execute("SELECT * FROM perguntas"))
    db.close()
    return lista

class SuperQuiz(BoxLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.db = UsaBanco("QuizDB")
    self.sortearPergunta()

  def sortearPergunta(self):
    self.ids.resposta.text = ""
    lista = self.db.listarRegistros()
    index = random.randint(0, 9)
    self.id = lista[index][0]
    self.pergunta = lista[index][1]
    self.alternativaCorreta = lista[index][2]
    self.alternativaErrada01 = lista[index][3]
    self.alternativaErrada02 = lista[index][4]
    self.alternativaErrada03 = lista[index][5]
    self.exibirAlternativas()

  def exibirAlternativas(self):
    lista = ['', '', '', '']
    index = random.randint(0, 3)
    while (lista[index] != ''):
      index = random.randint(0, 3)
    lista[index] = self.alternativaCorreta
    index = random.randint(0, 3)
    while (lista[index] != ''):
      index = random.randint(0, 3)
    lista[index] = self.alternativaErrada01
    index = random.randint(0, 3)
    while (lista[index] != ''):
      index = random.randint(0, 3)
    lista[index] = self.alternativaErrada02
    index = random.randint(0, 3)
    while (lista[index] != ''):
      index = random.randint(0, 3)
    lista[index] = self.alternativaErrada03

    self.ids.pergunta.text = self.pergunta
    self.lista = lista
    self.ids.alternativa1.text = lista[0]
    self.ids.alternativa2.text = lista[1]
    self.ids.alternativa3.text = lista[2]
    self.ids.alternativa4.text = lista[3]

  def exibirResultado(self, alternativa):
    if (self.lista[alternativa] == self.alternativaCorreta):
      self.ids.resposta.text = "Resposta correta"
    else:
      self.ids.resposta.text = "Resposta incorreta"

class MainApp(App):
  def build(self):
    self.title = "Super Quiz 1.0"
    return SuperQuiz()

if __name__ == '__main__':
  MainApp().run()
