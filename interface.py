#importações
from gamecode import *
""""
#=====================================================================================================================

#core de decisão
def resultados(Entra, jogadas):
  num = Entra.get()
  num = check(num)
 if(num == 0):
    return vezes
 else:
 #código de decisão transferido e adaptado do código fonte do jogo
  game(num, pontos)
  if (jogadas <= 0):
     time.sleep(0.5)
     messagebox.showinfo("Fim", "Obrigado por jogar!!!")
     time.sleep(0.75)
     main.destroy()

#========================================================================================================================

def aposta(jogadas):
    main.geometry("400x350")
    caixa.grid_remove()
    iniciar.grid_remove()

    título = Label(main, text=" Digite o número que acha que será sorteado entre 1 e 10: ")
    título.grid(column=0, row=1, padx=40, pady=30)
      
    numam = Entry(main, width=10)
    numam.grid(column=0, row=2, padx=40, pady=30)
    
    enviar = Button(main, text="Enviar", command= lambda: resultados(numam, jogadas))
    enviar.grid(column=0, row=3, padx=40, pady=30)


#========================================================================================================================

#segunda página(número apostado)
def apostar(Entra):
    jogadas = Entra.get()
    jogadas = check(jogadas)
    #reseter
    main.geometry("400x350")
    caixa.grid_remove()
    iniciar.grid_remove()

    título = Label(main, text=" Agora vamos apostar em um número!!!!")
    título.grid(column=0, row=1, padx=40, pady=30)
      
    
    enviar = Button(main, text="Enviar", command= lambda: aposta(jogadas))
    enviar.grid(column=0, row=3, padx=40, pady=30)

    

#primeira página(número de vezes)
def vezes():
    #reseter
    iniciar.grid_remove()
    t2.grid_remove()
    #reposicionamento da página
    main.geometry("310x350")

    título = Label(main, text="Digite o número de vezes que gostaria de jogar: ")
    título.grid(column=0, row=1, padx=20, pady=30)

    caixa = Entry(main, width=10)
    caixa.grid(column=0, row=2, padx=20, pady=30)

    enviar = Button(main, text="Enviar", command= lambda: apostar(caixa))
    enviar.grid(column=0, row=3, padx=20, pady=30)

#========================================================================================================================

#janela principal / main do projeto
main = Tk()
main.title("Jogo da adivinhação")
main.geometry("310x350")

título = Label(main, text = "Jogo de adivinhação de NÚMEROS!!!")
título.grid(column=0, row=0, padx=50, pady=30)

t2 = Label(main, text = "Digite o seu nome abaixo: ")
t2.grid(column=0, row=1, padx=50, pady=30)
caixa = Entry(main, width=10)
caixa.grid(column=0, row=2, padx=50, pady=30)

iniciar = Button(main, text="JOGAR", command= vezes)
iniciar.grid(column=0, row=3, padx=50, pady=30)

main.mainloop()
"""