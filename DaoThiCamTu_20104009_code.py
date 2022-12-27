from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from keras.models import load_model
from keras.utils import load_img, img_to_array
import numpy as np
  

# Tạo cửa sổ menu
root = Tk()
root.title("NHẬN DẠNG SÂU BỆNH TRÊN LÚA")
root.geometry("1080x600+200+80")
root.resizable(0,0)


img1=Image.open(r"rice_leaf_diseases\trangtrilogin\bg5.png")
photoimgae1=ImageTk.PhotoImage(img1)
lblimg1=Label(root,image=photoimgae1,cursor="hand2",bd=0)
lblimg1.place(x=0,y=0)

Main_Frame = Canvas(root,bg='white')
Main_Frame.place(x=350,y=0,width=800,height=600)

nen=Label(Main_Frame,text='NHẬN DẠNG SÂU BỆNH TRÊN LÚA',font=('Times New Roman',20,'bold'),fg='black',bg='white')
nen.place(x=150,y=100)

nen1=Label(Main_Frame,text='Tải ảnh lên',font=('arial',16,'bold'),fg='black',bg='white')
nen1.place(x=330,y=200)

Image_Frame = Canvas(root,bg='white')
Image_Frame.place(x=50,y=50,width=250,height=250)
img2=Image.open(r"nnnn.jpg")
photoimgae2=ImageTk.PhotoImage(img2)
lblimg2=Label(Image_Frame,image=photoimgae2,cursor="hand2",bd=0)
lblimg2.place(x=0,y=0)

model = load_model('saubenh.h5')
my_str = StringVar()
my_str.set('Loading...')
ketqua=Label(Main_Frame,textvariable=my_str,font=('arial',16,'bold'),fg='black',bg='white')
ketqua.place(x=320,y=400)
def openfn():
    filename = filedialog.askopenfilename(title='open')
    
    img = load_img(filename,target_size=(60,60))
    #plt.imshow(img)
    img = img_to_array(img)
    img = img[:,:,0]
    img = img.astype('float32')
    img = img.reshape(1,60,60,1)
    img = img/255
    class_number=['Bệnh bạc lá','Bệnh đạo ôn','Bệnh đốm nâu', 'Bệnh vàng lùn']
    a= int(np.argmax(model.predict(img),axis=1))
    print("Đây là bệnh",class_number[a])
    if (filename):
        my_str.set(class_number[a])
    return filename

def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(Image_Frame, image=img)
    panel.place (x=0,y=0)
    panel.image = img
    panel.pack()
lg_button1 = Button(Main_Frame,fg='white',bg='#DA70D6',border=0 ,text='UPLOAD FILE',width ='15',height='2',
    font =('time new roman',11,'bold'), cursor= "hand2",activeforeground='#924b45',command=open_img).place(x=320,y=250)
root.mainloop()