from tkinter import *
from tkinter import messagebox

L=[1,2,3,4,5,6,7,8,9]
CCS = 0
computerchoice = []
humanchoice =[]
computerchoiceT =[]
humanchoiceT =[]

def Exit():
    msg = messagebox.askyesno("Exit","are you sure you want exit?")
    if msg is True:
        exit()
def Rest():
    defultdata()
    defultAppearance()

def defultdata():
    global computerchoice
    global humanchoice
    global computerchoiceT
    global humanchoiceT
    global CCS
    CCS = 0
    computerchoice = []
    humanchoice =[]
    computerchoiceT =[]
    humanchoiceT =[]
    
def Winner(the_winner):
    msg = messagebox.askyesno(the_winner,"Play Again?!")
    if msg is True:
        Rest()
    else:
        Exit()

def test(listofthetested1,listofthetested2,sentence):
    global computerchoice
    global humanchoice
    global computerchoiceT
    global humanchoiceT
    winList=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    
    if len(listofthetested1) == 3:
        if sorted(listofthetested2) in winList:
            Winner(sentence)
        else:
            pass
        
    if len(listofthetested1)== 4:
        for listLen in range(4):
            listofthetested2.pop(listLen)
            if sorted(listofthetested2) in winList:
                Winner(sentence)
                break
            else:
                listofthetested2.clear()
                listofthetested2.extend(listofthetested1)
                continue
                
    elif len(listofthetested1)== 5:
        breakloop =0
        for listLen1 in range(5):
            if breakloop ==1:
                break
            listofthetested2.clear()
            listofthetested2.extend(listofthetested1)
            listofthetested2.pop(listLen1)
            for listLen2 in range(len(listofthetested2)):
                listofthetested2.pop(listLen2)
                if sorted(listofthetested2) in winList:
                    Winner(sentence)
                    breakloop = 1
                    break
                else:
                    listofthetested2.clear()
                    listofthetested2.extend(listofthetested1)
                    listofthetested2.pop(listLen1)
                    if listLen1 == 4:
                        Winner('Draw!')
                        breakloop = 1
                        break
                    else:
                        continue
            

                
def random():
    import random
    global L
    global CCS
    global computerchoice
    global humanchoice
    while len(humanchoice)<=4:
        CCS = random.sample(L,1)[0]
        if not CCS in computerchoice and not CCS in humanchoice:
            computerchoice.append(CCS)
            computerchoiceT.append(CCS)
            break
     
    
class square:
    
    def __init__(self,master,r,c,squareNo,color):
        self =Frame(master,width = 100,height=100, bg=color)
        self.grid(row =r, column=c,padx=2, pady=2)    
        self.bind("<1>",lambda e: human_choice(self))
        self.number = squareNo



def human_choice(self):
    global humanchoice
    global computerchoice
    if self.cget('bg')=='white' and not self.number in computerchoice:
        self.configure(bg='steel blue')
        humanchoice.append(self.number)
        humanchoiceT.append(self.number)
        test(humanchoice,humanchoiceT,'You Won!')
        random()
        computerTurn()
    else:
        messagebox.showinfo('MSG','this block is already used!')



def computerTurn():
    global CCS
    if CCS == 1:
        f1 = square(mainF,0,0,1,'firebrick1')
    if CCS == 2:
        f2 = square(mainF,0,1,2,'firebrick1')
    if CCS == 3:
        f3 = square(mainF,0,2,3,'firebrick1')
    if CCS == 4:
        f4 = square(mainF,1,0,4,'firebrick1')
    if CCS == 5:
        f5 = square(mainF,1,1,5,'firebrick1')
    if CCS == 6:
        f6 = square(mainF,1,2,6,'firebrick1')
    if CCS == 7:
        f7 = square(mainF,2,0,7,'firebrick1')
    if CCS == 8:
        f8 = square(mainF,2,1,8,'firebrick1')
    if CCS == 9:
        f9 = square(mainF,2,2,9,'firebrick1')
    test(computerchoice,computerchoiceT,'Computer Win!')
root = Tk()
root.title('tic tac toe')
mainF = Frame(root,bg='gray25')
mainF.grid(padx=4,pady=4)


def defultAppearance():
    f1 = square(mainF,0,0,1,'white')
    f2 = square(mainF,0,1,2,'white')
    f3 = square(mainF,0,2,3,'white')
    f4 = square(mainF,1,0,4,'white')
    f5 = square(mainF,1,1,5,'white')
    f6 = square(mainF,1,2,6,'white')
    f7 = square(mainF,2,0,7,'white')
    f8 = square(mainF,2,1,8,'white')
    f9 = square(mainF,2,2,9,'white')
    
defultAppearance()

buttonRest = Button(root,bg='bisque',text='Rest',command = Rest)
buttonExit = Button(root,bg='mistyrose2',text='Exit',command = Exit)

buttonRest.grid(row=0 , column=3)
buttonExit.grid(row=0 , column=4)

root.mainloop()
