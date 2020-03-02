### Import packages
from tkinter import *
from time import sleep

### Class Defs

"""
Puede definir tabla 1 o tabla 2
Puede definir títulos y estilos
Data es matriz 
"""
class Table:
    
    def __init__(self, pwindow, px=0, py=0, pwidth=800, pheight=220, pdata=[[""]], tableType = 1, titleColWidth = 270):

        #creacion atributos
        self.titleColWidth = titleColWidth
        self.secondTitleRatio = 0.6
        self.thirdTitleRatio = 0.5
        if tableType == 1:
            self.cell_width = (pwidth-titleColWidth)//len(pdata[0])
        elif tableType == 2:
            self.cell_width = (pwidth-(1+self.secondTitleRatio+self.thirdTitleRatio)*titleColWidth)//len(pdata[0])
        self.cell_height = pheight//len(pdata)
        self.window = pwindow
        self.x = px
        self.y = py
        self.height = pheight
        self.width = pwidth
        self.cols = len(pdata[0])
        self.rows = len(pdata)
        self.data = pdata
        self.text_refs = {}
        self.check_refs = {}
        self.frame_refs = {}
        self.rowNames = ["","Palabra de datos (sin paridad):","p1","p2","p3","p4","p5","Palabra de datos (con paridad):"]
        self.colNames = ["p1","p2","d1","p3","d2","d3","d4","p4","d5","d6","d7","d8","d9","d10","d11","p5","d12","Prueba de paridad","Bit de paridad"]

        #validacion datos
        try:
            cols = len(pdata[0])
            for i in range(len(pdata)):
                if cols != len(pdata[i]):
                    raise TypeError
        except:
            print("Tabla de datos invalida")
            return

        #creacion tabla

        for i in range(self.rows+1): #columna 1

            f = Frame(self.window,
                      highlightbackground="black",
                      highlightcolor="black",
                      highlightthickness=1)
            f.place(x=self.x,
                    y=self.y+self.cell_height*i,
                    width = titleColWidth,
                    height=self.cell_height)
            b = Text(f,
                     relief=FLAT,
                     wrap=WORD,
                     background="light grey")
            b.insert(END, self.rowNames[i])
            b.pack(expand=True)
            b.tag_add("Style","1.0",END)
            b.tag_configure("Style",justify="center",font="cambria 12 bold")
            b.tag_configure("Subscript", offset=-6,font="cambria 8 bold")
            if 1 < i and i < 7:
                b.tag_add("Subscript", "1.1",END)
            self.frame_refs[(i,0)] = f

        for j in range(self.cols): #fila 1

            f = Frame(self.window,
                      highlightbackground="black",
                      highlightcolor="black",
                      highlightthickness=1)
            f.place(x=self.x+titleColWidth+self.cell_width*j,
                    y=self.y,
                    width = self.cell_width,
                    height=self.cell_height)
            b = Text(f,
                     relief=FLAT,
                     wrap=WORD,
                     background="light grey")
            b.insert(END, self.colNames[j])
            b.pack(expand=True)
            b.tag_add("Style","1.0",END)
            b.tag_configure("Style",justify="center",font="cambria 12 bold")
            b.tag_configure("Subscript", offset=-6,font="cambria 8 bold")
            if j < 17:
                b.tag_add("Subscript", "1.1",END)
            self.frame_refs[(0,j+1)] = f
        
        for i in range(self.rows): #datos
            for j in range(self.cols):
                
                f = Frame(self.window,
                          highlightbackground="black",
                          highlightcolor="black",
                          highlightthickness=1)
                f.place(x=self.x+titleColWidth+self.cell_width*j,
                        y=self.y+self.cell_height*(i+1),
                        width = self.cell_width,
                        height=self.cell_height)
                b = Text(f,
                         relief=FLAT,
                         wrap=WORD,
                         font="cambria 12",
                         background="white")
                if i==6:
                    b = Text(f,
                             relief=FLAT,
                             wrap=WORD,
                             font="cambria 12",
                             background="grey",
                             foreground="white")
                b.insert(END, self.data[i][j])
                b.pack(expand=True)
                b.tag_add("Justify","1.0",END)
                b.tag_configure("Justify",justify="center")
                b.tag_configure("Bold",font="cambria 12 bold")
                if i==0 or j==0 or j==1 or j==3 or j==7 or j==15:
                    b.tag_add("Bold","1.0",END)
                self.text_refs[(i,j)] = b
                self.frame_refs[(i+1,j+1)] = f
                
        if tableType == 2:

            bitsParidad = []
            for fila in self.data:
                suma = 0
                for bit in fila:
                    suma += int(bit)
                if (-1)**suma == 1:
                    bitsParidad.append(0)
                else:
                    bitsParidad.append(1)
            print(bitsParidad)
            
            for i in range(self.rows+1): # Prueba de paridad

                f = Frame(self.window,
                          highlightbackground="black",
                          highlightcolor="black",
                          highlightthickness=1)
                f.place(x=self.x+titleColWidth+self.cell_width*self.cols,
                        y=self.y+self.cell_height*i,
                        width = self.secondTitleRatio*titleColWidth,
                        height=self.cell_height)
                b = Text(f,
                         relief=FLAT,
                         wrap=WORD,
                         background="light grey")
                if i==0:
                    b.insert(END, self.colNames[17])
                    b.tag_add("Style","1.0",END)
                elif i==1:
                    b.tag_add("Style","1.0",END)
                elif bitsParidad[i-1]==1:
                    b.insert(END, "Error")
                    b.tag_add("Style","1.0",END)
                else:
                    b.insert(END,"Correcto")
                    b.tag_add("Style2","1.0",END)
                b.pack(expand=True)
                b.tag_configure("Style",justify="center",font="cambria 12 bold")
                b.tag_configure("Style2",justify="center",font="cambria 12")
                if i>1:
                    self.check_refs[(i-1,0)] = b
                self.frame_refs[(i,self.cols+1)] = f

            for i in range(self.rows+1): # Bit de paridad

                f = Frame(self.window,
                          highlightbackground="black",
                          highlightcolor="black",
                          highlightthickness=1)
                f.place(x=self.x+(1+self.secondTitleRatio)*titleColWidth+self.cell_width*self.cols,
                        y=self.y+self.cell_height*i,
                        width = self.thirdTitleRatio*titleColWidth,
                        height=self.cell_height)
                b = Text(f,
                         relief=FLAT,
                         wrap=WORD,
                         background="light grey")
                if i==0:
                    b.insert(END, self.colNames[18])
                    b.tag_add("Style","1.0",END)
                elif i==1:
                    b.tag_add("Style","1.0",END)
                elif bitsParidad[i-1]==1:
                    b.insert(END, bitsParidad[i-1])
                    b.tag_add("Style","1.0",END)
                else:
                    b.insert(END, bitsParidad[i-1])
                    b.tag_add("Style2","1.0",END)
                b.pack(expand=True)
                b.tag_configure("Style",justify="center",font="cambria 12 bold")
                b.tag_configure("Style2",justify="center",font="cambria 12")
                if i>1:
                    self.check_refs[(i-1,1)] = b
                self.frame_refs[(i,self.cols+2)] = f
            
        #if len(self.text_refs) > 1:
            #print(self.text_refs[(0,1)].get("1.0",END))
            #self.refs[(0,0)].tag_add("Error","1.0",END)
            #self.refs[(0,0)].tag_configure("Error",background="Red",foreground="white",justify="center")

    def destroy(self):
        for i,j in self.frame_refs:
            self.frame_refs[(i,j)].destroy()

    def get(self):
        salida = self.data
        for i,j in self.text_refs:
            salida[i][j] = self.text_refs[(i,j)].get("1.0",END)[:-1]
        return salida

    def getCheck(self):
        salida = {}
        for i,j in self.check_refs:
            salida[(i,j)] = self.check_refs[(i,j)].get("1.0",END)[:-1]
        return salida

"""

### Global Vars
flags = [True,0]

### Function Defs
def click(flags):
    entered_text = textentry.get()
    rows = entered_text.split(",")
    data = []
    for i in range(len(rows)):
        data.append(rows[i].split(" "))
    if flags[0]:
        flags[0] = False
    else:
        flags[1].destroy()
    table = Table(window, 10, 140,1180,220,data,1)
    flags[1]=table
    
def click_2(flags):
    entered_text = flags[1].get()
    flags[1].destroy()
    flags[1] = Table(window, 10, 140,1180,220,entered_text,2)
    
def close_window():
    window.destroy()

### Main layout:
window = Tk()
window.geometry("1200x650+200+200")
window.title("Tablas")
window.configure(background="black")


Label (window,text="Indique la matriz:", bg="black", fg="white",font="none 12 bold").place(x=300,y=0,height=30,width=600)

textentry= Entry(window, width=20, bg="white")
textentry.place(x=300, y=30, width = 600, height=40)

#table_1 = Table(window, 10, 10, 10, 10,[[""]])

Button(window, text="SUBMIT", width=6, command=lambda:click(flags)).place(x=300,y=70,width=600,height=30)

Label (window, text="\nTabla 1:",bg="black",fg="white",font="none 12 bold").place(x=300,y=100,width=600,height=30)

Button(window, text="CHECK", width=6, command=lambda:click_2(flags)).place(x=300,y=560,width=600,height=30)

Button(window,text="Exit",width=14, command=close_window).place(x=300,y=600,width=600,height=30)

#### Run the main loop

window.mainloop()

"""
