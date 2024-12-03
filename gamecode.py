#importações
import random
import time
from shortcuts import *

#==============================================================================================================

#setagem de jogadas totais
def first(jogadas):
 jogadas = check()
 return jogadas

#jogo em si
def game(num, pontos):
  num = check(num)
  numa = random.randrange(1, 10)
  
  acertonumero(num, numa, pontos, jogadas)
  
def acertonumero(num, numa, pontos, jogadas):  
  #show results1
  if (num == numa):
    time.sleep(0.75)
    pontos +=1
    messagebox.showinfo("Parabéns", "Você acertou! \n Calculando pontos....")
    time.sleep(0.5)
    messagebox.showinfo("Pontos:", pontos)
    next(jogadas)

  #show results 2
  else:
    time.sleep(0.5)
    pontos -=1
    messagebox.showinfo("Errou! O sorteado foi: ", numa)
    time.sleep(0.5)
    messagebox.showinfo("Pontos:", pontos) 
    next(jogadas)
  jogadas -=1