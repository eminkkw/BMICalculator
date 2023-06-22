from tkinter import *

#window
window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)

#label
label = Label(text="Enter Your Weight")
label.place(x=0,y=60)

#label_2
label_2 = Label(text="Enter Your Height")
label_2.place(x=0,y=100)


#entry
entry = Entry(width=20)
entry.place(x=110,y=60)

#entry_2
entry_2 = Entry(width=20)
entry_2.place(x=110,y=100)

#button
def click_button():
    hesaplama = BMIHesap()
    if int(hesaplama) < 18.5:
        print("Zayıfsın")
    elif 18.5 <= int(hesaplama) <= 24.9:
        print("Normal")
    elif 25 <= int(hesaplama) <= 29.9:
        print("Fazla Kilolu")
    elif 30 <= int(hesaplama) <= 34.9:
        print("1.derece Obezite")
    elif 35 <= int(hesaplama) <= 39.9:
        print("2.derece Obezite")
    elif int(hesaplama) > 40:
        print("3.derece Obezite")


button = Button(text="Calculate",command=click_button)
button.place(x=40,y=130)

#label_3
label_3_text = StringVar()  # Metin değişkeni
label_3 = Label(textvariable=label_3_text)# label_3_text değişkenine bağlanıyor
label_3.place(x=0,y=160) # Konum ayarı
label_3.pack()


#BMIHesap
def BMIHesap():
    value1 = entry.get()
    value2 = entry_2.get()
    hesaplama = int(value1) * int(value1) / int(value2)
    return hesaplama


window.mainloop()