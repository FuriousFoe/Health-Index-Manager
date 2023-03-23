import tkinter
import tkinter.messagebox
from tkinter import *
import os
import matplotlib.pyplot as plt
names = []
row = 0
#file handling

def click_reg():
    global username
    username = registerUsername.get()
    age = registerAge.get()
    height = registerHeight.get()
    weight = registerWeight.get()
    bp = registerbp.get()
    pr = registerPr.get()
    result, bmi = Result()
    #account = os.listdir()

    if username == '' or age == '' or height == '' or weight == '' or bp == '' or pr == '' or result == '':
        a.config(fg='red', text='*All fields required*')
        return
    else :
        registerResult.insert(0, result)
        file = open(username, 'w')
        file.write(username + '\n')
        file.write(age + '\n')
        file.write(height + '\n')
        file.write(weight + '\n')
        file.write(bp + '\n')
        file.write(pr + '\n')
        file.write(result + '\n')
        file.write('0.0')
        file.close()
        a.config(text='File created successfully :)', fg='green')

def Result():
    bmi = 0
    try:
        height = int(registerHeight.get())
        weight = int(registerWeight.get())
        bmi = weight*10000/(height*height)

    except:
        print('Enter Valid Height and Weight')

    try:
        bp = int(registerbp.get())
        pulse = int(registerPr.get())
    except:
        print("Enter valid BP and Pulserate")

    global res1
    res1 = ""
    if bmi != 0:
        if bmi <= 18.5:
            res1 = 'Underweight'
        elif bmi <= 25:
            res1 = "Healthy"
        elif bmi <= 30:
            res1 = "Obese"
        else: 
            res1 = "Morbidly obese"
        
    global res2
    res2 =" "
    global res3
    res3 =" "
    if pulse != 0 and bp != 0:
        if bp <= 120:
            res2 = ", Low BP"
        elif bp <= 130:
            res2 = ", Normal BP"
        elif bp <= 140:
            res2 = ", High BP"
        else:
            res2 = ", Extreme HyperTension"

        if pulse <= 60:
            res3 = ", Low Pulse"
        elif pulse <= 100:
            res3 = ", Normal Pulse"
        else:
            res3 = ", High Pulse"

        global res
        res = res1 + res2 + res3
        return res, bmi

def details():
    file = open(username, "r")
    data = file.read()
    accDetails = data.split('\n')
    accDetails_username = accDetails[0]
    accDetails_age = accDetails[1]
    accDetails_heigth = accDetails[2]
    accDetails_weigth = accDetails[3]
    accDetails_bp = accDetails[4]
    accDetails_pr = accDetails[5]
    accDetails_result = accDetails[6]

    personalDetailsWindow = Toplevel(root)
    personalDetailsWindow.title('Personal Details')
    Label(personalDetailsWindow, text='Personal Details', font=("Helvetica",18, "bold")).grid(padx=15)
    Label(personalDetailsWindow, text="Username :\t" + accDetails_username).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Age :\t\t" + accDetails_age).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Height :\t\t" + accDetails_heigth).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Weight :\t\t" + accDetails_weigth).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="bp :\t\t" + accDetails_bp).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="pr :\t\t" + accDetails_pr).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Result :\t\t" + accDetails_result).grid(sticky=W, padx=10)

#The Framework
root = tkinter.Tk()
root.title("HEALTH INDEX")
root.geometry("400x300")
root.grid()

panel1 = tkinter.PanedWindow(bd =4 , relief="raised",bg="Grey" )
panel1.pack(fill=BOTH , expan =1 )

panel2 = tkinter.PanedWindow(panel1 , orient=VERTICAL ,bd=4 , bg = "grey" , relief= "raised")
panel1.add(panel2)

files = tkinter.Label(panel1 , text = "Files")
panel1.add(files)

data = tkinter.Label(panel2 , text = "Data")
panel2.add(data)

frame = tkinter.Frame(data)
frame.pack()

frame2 = tkinter.Frame(files)
frame2.pack()

label = tkinter.Label(frame , text = "Name : ")
label.grid(row = 0 , column = 0)

registerUsername = tkinter.Entry(frame)
registerUsername.grid(row = 0 , column = 1)

label = tkinter.Label(frame , text = "Age : ")
label.grid(row = 1 , column = 0)

registerAge = tkinter.Entry(frame)
registerAge.grid(row = 1 , column = 1)

label = tkinter.Label(frame, text = "Height : ")
label.grid(row = 2 , column = 0)

registerHeight = tkinter.Entry(frame)
registerHeight.grid(row = 2 , column = 1)

label = tkinter.Label(frame , text = "Weight : ")
label.grid(row = 3 , column = 0)

registerWeight = tkinter.Entry(frame)
registerWeight.grid(row = 3 , column = 1)

label = tkinter.Label(frame , text = "Blood Pressure : ")
label.grid(row = 4 , column = 0)

registerbp = tkinter.Entry(frame)
registerbp.grid(row = 4 , column = 1)

a = tkinter.Label(frame , text ="Pulse Rate : ")
a.grid(row = 5 , column = 0)

registerPr = tkinter.Entry(frame)
registerPr.grid(row = 5 , column = 1)

f = tkinter.Label(frame, text = "Result : ")
f.grid(row = 6 , column = 0)

registerResult = tkinter.Entry(frame )
registerResult.grid(row = 6, column= 1)

text = tkinter.Text(frame , height = 2 , width = 10)
text.grid(row=7 , column=1 )

sub = tkinter.Button(frame , text ="Submit " , command= lambda : Submit(text) )
sub.grid(row=7 , column=0)

a = Label(frame)
a.grid(row=8 , column=0)
#files


def Submit(text):
    img = plt.imread("bmi(2).jpg")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[40, 130, 140, 200])

    try:
        height = int(registerHeight.get())
        weight = int(registerWeight.get())
    except:
        print('no')

    plt.xlim([40, 130])
    plt.ylim([140, 200])

    plt.plot(weight, height, marker='o')
    plt.show()
    #text.insert(tkinter.INSERT, "*")
    click_reg()
    app = App()
    app.new_row()

class App(object):
    def new_row(self):
        # Create widgets
        global names
        global row
        if username in names:
            details()
        else:
            tkinter.Button(frame2, width= 20 , text=f"{username}" , command= lambda : details()).grid(column = 0, row = row)
            names.append(username)
            row += 1

def exit():
    exit = tkinter.messagebox.askyesno(" Health Index ", " Do you want to exit ?")
    if exit > 0:
        root.destroy()
        return

def project():
    root.resizable(height=False , width=False)

text = tkinter.Text(frame , height = 2 , width = 10)
text.grid(row=7 , column=1 )

sub = tkinter.Button(frame , text ="Submit and Plot" , command= lambda : Submit(text) )
sub.grid(row=7 , column=0)

def analysis():
    file = open(res,"w")
    file.write(res1 + '\n')
    file.write(res2 + '\n')
    file.write(res3 + '\n')
    file.write('0.0')
    file.close()

    file = open(res,"r")
    info = file.read()
    infodetails = info.split("\n")
    infodetails_status = infodetails[0]
    infodetails_bp = infodetails[1]
    infodetails_pluse = infodetails[2]

    window = tkinter.Tk()
    window.title("Your analysis :- ")
    Label(window, text="Status :\t\t" + infodetails_status).grid(sticky=W, padx=10)
    if infodetails_status == 'Healthy':
        Label(window, text="Just stay the way you are !!! \n Do regular exercise !!!").grid(sticky=W, padx=10)
    elif infodetails_status == "Underweight" :
        Label(window, text="You need to gain Weight \n Try Adding following in your meal \n"
                           " Rice ,Nuts and nut butters. \nRed meats , Potatoes and starches \n"
                           " Salmon and oily fish").grid(sticky=W, padx=10)
    else :
        Label(window, text=" Do regular exercise !!! \n For losing weight try following :-\n"
                           " Lean Protein. Lean protein sources \n like chicken, "
                           "turkey and grass-fed lean \nbeef help keep you full ,"
                           "decrease cravings \n and stabilize blood sugar, Eggs ").grid(sticky=W, padx=10)
    Label(window, text="bp :\t\t" + infodetails_bp).grid(sticky=W, padx=10)
    if infodetails_bp == ', Normal BP':
        Label(window, text="pulse :\t\t" + infodetails_pluse).grid(sticky=W, padx=10)
    else :
        Label(window, text=" 1) Lose extra pounds and \n"
                               "watch your waistline. \n "
                               " 2) Exercise regularly \n "
                               " 3) Eat a healthy diet \n "
                               " 4) Meditate Everyday for 1/2 hr").grid(sticky=W, padx=10)
        Label(window, text="pulse :\t\t" + infodetails_pluse).grid(sticky=W, padx=10)
    if infodetails_pluse == ", Normal Pulse":
        Label(window, text=" ").grid(sticky=W , padx=10)
    else:
        Label(window, text=" To attain a normal pulse you should \n" 
                           "Practicing stretching and relaxation \n exercises, such as yoga").grid(sticky=W , padx=10)


    window.geometry("250x80")
    window.mainloop()

rec = tkinter.Button(frame , text ="Recommendations" , command= lambda : analysis() )
rec.grid(row= 8 , column=0)


menubar = Menu(frame)
filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="INDEX ", command=project)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
root.config(menu=menubar)

root.mainloop()

