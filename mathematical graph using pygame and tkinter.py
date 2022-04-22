import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
from tkinter import *
from tkinter import messagebox

def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw(lst):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    # x-y axis lines
    x = np.linspace(-10,10,100000)
    y = np.multiply(x,0)
    glColor3f(1.0, 0.0, 0.0)
    for i,j in zip(x,y):
        glVertex2f(i,j)
        glVertex2f(j,i)
    # The six graphs in one
    x = np.linspace(-10,10,100000)
    # sx is for log. since in log(x) x cannot be negative.
    sx = np.linspace(0.000001,10,100000)
    y = np.power(x,2)
    z = np.multiply(x,2)
    a = np.sin(x)
    b = np.cos(x)
    c = np.tan(x)
    d = np.log(sx)
    for i,j,k,l,m,n,o,so in zip(x,y,z,a,b,c,d,sx):
        if 1 in lst:
            glColor3f(0.3,0.2,0.7)
            glVertex2f(i,j)
        if 2 in lst:
            glColor3f(1.0,0.0,1.0)
            glVertex2f(i,k)
        if 3 in lst:
            glColor3f(1.0,1.0,1.0)
            glVertex2f(i,l)
        if 4 in lst:
            glColor3f(0.0,1.0,1.0)
            glVertex2f(i,m)
        if 5 in lst:
            glColor3f(0.5,0.5,0.5)
            glVertex2f(i,n)
        if 6 in lst:
            glColor3f(0.5,0.9,0.5)
            glVertex2f(so,o)
    glEnd()
    glFlush()

def main():
    # Tkinter code for accepting types of graphs to be drawen
    root = Tk()
    root.title("Graph type chooser")
    enter = Entry(root,width=17, borderwidth=5, font=('Arial 18'))
    enter.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
    lst = []
    def clickButton(choice):
        enter.delete(0,END)
        if len(lst)>=2:
            messagebox.showerror('Error message', 'Error: you chose more than two graphs!\nplease just draw the two graphs')
            enter.insert(0,"sorry! only 2 graphs.")
        else:
            lst.append(choice)
            enter.insert(0,"you chose: ")
            if choice == 1:
                chosen = "x square"
            elif choice == 2:
                chosen = "linear"
            elif choice == 3:
                chosen = "sin"
            elif choice == 4:
                chosen = "cos"
            elif choice == 5:
                chosen = "tan"
            elif choice == 6:
                chosen = "log"
            else:
                chosen = "sorry, you chose wrong!"
            enter.insert(11,chosen)
    Button1 = Button (root, text="x square", padx=7, pady=20, borderwidth=3, command=lambda: clickButton(1))
    Button2 = Button (root, text="linear", padx=14, pady=20, borderwidth=3, command=lambda: clickButton(2))
    Button3 = Button (root, text="sin", padx=20, pady=20, borderwidth=3, command=lambda: clickButton(3))
    Button4 = Button (root, text="cos", padx=20, pady=20, borderwidth=3, command=lambda: clickButton(4))
    Button5 = Button (root, text="tan", padx=20, pady=20, borderwidth=3, command=lambda: clickButton(5))
    Button6 = Button (root, text="log", padx=20, pady=20, borderwidth=3, command=lambda: clickButton(6))
    Button1.grid(row=1,column=0,padx=5,pady=5)
    Button2.grid(row=1,column=1,padx=5,pady=5)
    Button3.grid(row=1,column=2,padx=5,pady=5)
    Button4.grid(row=2,column=0,padx=5,pady=5)
    Button5.grid(row=2,column=1,padx=5,pady=5)
    Button6.grid(row=2,column=2,padx=5,pady=5)
    draw_graph = Button(root, text="draw selected graphs", padx=20, pady=10, width=20, borderwidth=7, bg="coral", command=root.destroy)
    draw_graph.grid(row=3,column=0, columnspan=3, padx=5, pady=5)
    root.mainloop()

    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw(lst)
        pygame.display.flip()
        pygame.time.wait(10)

main()