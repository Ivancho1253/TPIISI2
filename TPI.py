import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Designing window for registration

def register():
    global register_screen
    register_screen = tk.Toplevel(main_screen)
    register_screen.title("Registro")
    register_screen.geometry("300x300")

    global username
    global password
    global username_entry
    global password_entry
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(register_screen, text="Por favor, ingrese los datos", bg="brown").pack()
    tk.Label(register_screen, text="").pack()
    username_label = tk.Label(register_screen, text="Usuario")
    username_label.pack()
    username_entry = tk.Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = tk.Label(register_screen, text="Contraseña")
    password_label.pack()
    password_entry = tk.Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    tk.Label(register_screen, text="").pack()
    tk.Button(register_screen, text="Registro", width=10, height=2, bg="brown", command=register_user).pack()

# Designing window for login

def login():
    global login_screen
    login_screen = tk.Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    tk.Label(login_screen, text="Por favor, ingrese los datos",bg="brown").pack()
    tk.Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    global username_login_entry
    global password_login_entry

    tk.Label(login_screen, text="Usuario * ").pack()
    username_login_entry = tk.Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    tk.Label(login_screen, text="").pack()
    tk.Label(login_screen, text="Contraseña * ").pack()
    password_login_entry = tk.Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    tk.Label(login_screen, text="").pack()
    tk.Button(login_screen, text="Login", width=10, height=2, bg="brown",command=login_verify).pack()

# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    tk.Label(register_screen, text="Registro Exitoso", fg="green", font=("calibri", 15)).pack()

# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_success():
    global login_success_screen
    login_success_screen = tk.Toplevel(login_screen)
    login_success_screen.title("Exitoso")
    login_success_screen.geometry("150x100")
    tk.Label(login_success_screen, text="Login Exitoso", fg= "green", font=("calibri", 15)).pack()
    tk.Button(login_success_screen, text="Volver", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = tk.Toplevel(login_screen)
    password_not_recog_screen.title("Exitoso")
    password_not_recog_screen.geometry("150x100")
    tk.Label(password_not_recog_screen, text="Contraseña Incorrecta ", fg= "red").pack()
    tk.Button(password_not_recog_screen, text="Volver", command=delete_password_not_recognised).pack()

# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = tk.Toplevel(login_screen)
    user_not_found_screen.title("Exitoso")
    user_not_found_screen.geometry("150x100")
    tk.Label(user_not_found_screen, text="Usuario no encontrado", fg= "red").pack()
    tk.Button(user_not_found_screen, text="Volver", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    main_screen.geometry("500x500")
    main_screen.title("Login TroncoSoft")

    # Load and display the image
    image_path = "/Users/Acer/Downloads/LogoTPI.jpg"
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()

    tk.Label(text="Bienvenido a TroncoSoft", bg="brown", width="20", height="2", font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(text="").pack()
    tk.Button(text="Login", height="2",bg="brown", width="30", font=("Copperplate Gothic Bold", 15), command=login).pack()
    tk.Label(text="").pack()
    tk.Button(text="Registrarse", height="2",bg="brown", width="30", font=("Copperplate Gothic Bold", 15), command=register).pack()

    main_screen.mainloop()

main_account_screen()