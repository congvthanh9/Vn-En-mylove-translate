#input các thư viện cần thiết
from tkinter import*
from PIL import Image, ImageTk
from googletrans import Translator

#tạo giao diện đầu tiên
root = Tk()
root.title("Mylove Translator")
root.geometry("450x650")
root.iconbitmap(r'C:\Users\congv\Documents\python\Mylove translator\mylove.ico')

#tạo background
load = Image.open(r'C:\Users\congv\Documents\python\Mylove translator\background2.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0,y=0)

#Tạo tên app
name = Label(root, text="Mylove Translator", fg="#CBADED", bd=0, bg="#E2FAFE")
name.config(font=('Tranformer Movie', 25))
name.pack(pady=10)

#Tạo khung dịch đầu vào
box_input = Text(root, width=29,bd=0.1,bg="#D3D9FD",height=8, font=("Tranformers Movie",16))
box_input.pack(pady=20)

#tạo frame button 
button_frame = Frame(root).pack(side=BOTTOM)

#tạo chức năng cho công cụ clear
def clear():
    box_input.delete(1.0,END)
    box_output.delete(1.0,END)

#tạo chức năng cho công cụ trans
def translator(): 
    INPUT=box_input.get(1.0, END)
    t=Translator()
    s=t.translate(INPUT,src="vi", dest="en")
    a=s.text
    box_output.insert(END, a)
    print(INPUT)


#tạo button clear 
clear_button = Button(button_frame, text="Clear",bd=0, font=(("Arial"), 10, "bold"), bg="#CBADED", fg='#FFFFFF', command=clear)
clear_button.place(x=105, y=295)

#tạo button translator
trans_button = Button(button_frame, text="Translate",bd=0, font=(("Arial"), 10, "bold"), bg="#CBADED", fg='#FFFFFF',command=translator)
trans_button.place(x=290, y=295)


#Tạo khung dịch đầu ra 
box_output = Text(root,bd=0.1, bg="#D3D9FD", width=29, height=8, font=('Tranformer Movie',16))
box_output.pack(pady=45)



#tạo vòng lặp để chạy giao diện trên màn hình
root.mainloop()