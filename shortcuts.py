#importações
import time
from tkinter import *
from tkinter import messagebox

#setagem padrão para não dar erro
pontos = 0
jogadas = 0
jog = 1
global start 
start = True

#=============================================================================================================================

#print de resultados
def next( jogadas):
 if (jogadas != 0):
  time.sleep(0.5)
  messagebox.showinfo("Prepare-se!!!!", "Próxima jogada")
  time.sleep(0.25) 

#função de checagem para tratamento de dados
def check(a=0):
 while True:
  try:
   a = int(a)
   return a
  except ValueError:
   messagebox.showinfo("Erro!!!", "Há presença de \n formatos Inválidos!!!!")
   a = 0
#essa aqui eu tenho orgulho de mostrar que eu sei fazer agora kakakakakakak


