from functools import total_ordering
import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import date
import database

app = customtkinter.CTk()
app.title('Fruits and Veggies Billing System')
app.geometry('900x350')
app.config(bg='#0A0B0C')
app.resizable(False,False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 24, 'bold')

def receipt():
    fruits_entries = [Apple_entry, Orange_entry, Mango_entry]
    vegetables_entries = [Carrots_entry, Potato_entry, Cabbage_entry]
    fruits_prices, vegetables_prices = database.get_product_prices()
    
    try:
        fruits_quantities = []
        for entry in fruits_entries:
            text = entry.get()
            if text:
                fruits_quantities.append(int(text))
            else:
                fruits_quantities.append(0)
                
        vegetables_quantities = []
        for entry in vegetables_entries:
            text = entry.get()
            if text:
                vegetables_quantities.append(int(text))
            else:
                vegetables_quantities.append(0)
                
        fruits_total = sum(quantity * price for quantity, price in zip(fruits_quantities, fruits_prices))
        vegetables_total = sum(quantity * price for quantity, price in zip(vegetables_quantities, vegetables_prices))
        total = fruits_total + vegetables_total
        todays_date = date.today().strftime('%d %m %Y')
        if total == 0:
            messagebox.showerror('Error','Choose at least 1 product.')
        else:
            fruits_total_label.configure(text=f'Fruits Total: ₱{fruits_total}')
            vegetablels_total_label.configure(text=f'Vegetables Total: ₱{vegetables_total}')
            total_label.configure(text=f'Total Price: ₱{total}')
            date_label.configure(text=f'Date: {todays_date}')
            return fruits_total, vegetables_total, total, todays_date
    except ValueError:
        messagebox.showerror('Error', 'Entered values should be integers.')

def new():
    Apple_entry.delete(0,END)
    Orange_entry.delete(0,END)
    Mango_entry.delete(0,END)
    Carrots_entry.delete(0,END)
    Potato_entry.delete(0,END)
    Cabbage_entry.delete(0,END)
    fruits_total_label.configure(text='')
    vegetablels_total_label.configure(text='')
    total_label.configure(text='')
    date_label.configure(text='')

def save():
    totals = receipt()
    if totals: [fruits_total, vegetables_total, None]
    fruits_total, vegetables_total, todays_date = totals
    with open('Receipt.txt', 'a') as file:
            file.write(f'Fruits Total: {fruits_total}₱\n')
            file.write(f'Vegetables Total: {vegetables_total}₱\n')
            file.write(f'Total Price: {fruits_total}₱\n')
            file.writer(f'Date: {todays_date}\n================\n')
    messagebox.showinfo('Succes', 'Receipt has been saved.')


fruits_frame = customtkinter.CTkFrame(app,bg_color='#131314', fg_color='#1B1A1D', corner_radius=10,border_width=1,border_color='#fff',width=280,height=250)
fruits_frame.place(x=15,y=15)

image1 = PhotoImage(file='fruit.png')
image1_label = Label(fruits_frame, image=image1,bg='#1B1A1D')
image1_label.place(x=5,y=5)

title1_label = customtkinter.CTkLabel(fruits_frame,font=font2,text='Fruits',text_color='#000000', bg_color='#FFFFFF')
title1_label.place(x=90,y=40)

Apple_label = customtkinter.CTkLabel(fruits_frame,font=font1,text='Apple:',text_color='#000000', bg_color='#FFFFFF')
Apple_label.place(x=20,y=100)

Apple_label = customtkinter.CTkLabel(fruits_frame,font= ('Trebuchet MS', 10, 'bold'), text='Quantity:',text_color='#000000', bg_color='#FFFFFF')
Apple_label.place(x=190,y=70,)

Apple_entry = customtkinter.CTkEntry(fruits_frame,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=80)
Apple_entry.place(x=170,y=100)

Orange_label = customtkinter.CTkLabel(fruits_frame,font=font1,text='Orange:',text_color='#000000', bg_color='#FFFFFF')
Orange_label.place(x=20,y=140)

Orange_entry = customtkinter.CTkEntry(fruits_frame,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=80)
Orange_entry.place(x=170,y=140)

Mango_label = customtkinter.CTkLabel(fruits_frame,font=font1,text='Mango:',text_color='#000000', bg_color='#FFFFFF')
Mango_label.place(x=20,y=180)

Mango_entry = customtkinter.CTkEntry(fruits_frame,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=80)
Mango_entry.place(x=170,y=180)

vegetables_frame = customtkinter.CTkFrame(app,bg_color='#131314',fg_color='#1B1A1D',corner_radius=10, border_width=1,border_color='#fff',width=280,height=250)
vegetables_frame.place(x=310,y=15)

image2 = PhotoImage(file='vegies.png')
image2_label = Label(vegetables_frame, image=image2,bg='#1B1A1D')
image2_label.place(x=5,y=5,)

title2_label = customtkinter.CTkLabel(vegetables_frame,font=font1,text='Vegetables',text_color='#000000', bg_color='#FFFFFF')
title2_label.place(x=90,y=40)

Carrots_label = customtkinter.CTkLabel(vegetables_frame,font=font1,text='Carrots:',text_color='#000000', bg_color='#FFFFFF')
Carrots_label.place(x=20,y=100,)

Carrots_label = customtkinter.CTkLabel(vegetables_frame,font= ('Trebuchet MS', 10, 'bold'), text='Quantity:',text_color='#000000', bg_color='#FFFFFF')
Carrots_label.place(x=190,y=70,)

Carrots_entry = customtkinter.CTkEntry(vegetables_frame,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=80)
Carrots_entry.place(x=170,y=100)

Potato_label = customtkinter.CTkLabel(vegetables_frame,font=font1,text='Potato:',text_color='#000000', bg_color='#FFFFFF')
Potato_label.place(x=20,y=140)

Potato_entry = customtkinter.CTkEntry(vegetables_frame,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=80)
Potato_entry.place(x=170,y=140)

Cabbage_label = customtkinter.CTkLabel(vegetables_frame,font=font1,text='Cabbage:',text_color='#000000', bg_color='#FFFFFF')
Cabbage_label.place(x=20,y=180)

Cabbage_entry = customtkinter.CTkEntry(vegetables_frame,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=80)
Cabbage_entry.place(x=170,y=180)

receipt_frame = customtkinter.CTkFrame(app,bg_color='#131314',fg_color='#1B1A1D',border_width=1,border_color='#fff',width=250,height=250)
receipt_frame.place(x=620,y=15)

title3_label = customtkinter.CTkLabel(receipt_frame,font=font1,text='Receipt',text_color='#fff',bg_color='#1B1A1D')
title3_label.place(x=90,y=10)

fruits_total_label = customtkinter.CTkLabel(receipt_frame,font=font1,text='',text_color='#fff',bg_color='#1B1A1D')
fruits_total_label.place(x=10,y=50)

vegetablels_total_label = customtkinter.CTkLabel(receipt_frame,font=font1,text='',text_color='#fff',bg_color='#1B1A1D')
vegetablels_total_label.place(x=10,y=90)

total_label = customtkinter.CTkLabel(receipt_frame,font=font1,text='',text_color='#fff',bg_color='#1B1A1D')
total_label.place(x=10,y=130)

date_label = customtkinter.CTkLabel(receipt_frame,font=font1,text='',text_color='#fff',bg_color='#1B1A1D')
date_label.place(x=10,y=170)

receipt_button = customtkinter.CTkButton(app,command=receipt,font=font2,text_color='#fff',text='Receipt',fg_color='#047152',bg_color='#0A0B0C',cursor='hand2',corner_radius=25,width=150)
receipt_button.place(x=190,y=280)

save_button = customtkinter.CTkButton(app,command=save,font=font2,text_color='#fff',text='Save',fg_color='#078C01',bg_color='#0A0B0C',cursor='hand2',corner_radius=25,width=150)
save_button.place(x=360,y=280)

new_button = customtkinter.CTkButton(app,command=new,font=font2,text_color='#fff',text='New',fg_color='#E93E05',bg_color='#0A0B0C',cursor='hand2',corner_radius=25,width=150)
new_button.place(x=530,y=280)


app.mainloop()
