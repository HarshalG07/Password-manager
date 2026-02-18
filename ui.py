from tkinter import *
from tkinter import ttk
from passGenrator import pass_gen
from tkinter import messagebox
import pyperclip

BG_COLOR = '#FFDAB3'
FONT = ('Albertus Medium',15,'normal')
FG_COLOR = '#574964'
BUTTON_FONT = ('Albertus Medium',12,'normal')
BUTTON_PRESS = "#F5C38F"

class Frontend():
    def __init__(self,window):
        self.window = window
        self.window.title('Password Manager')
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure(
            'Custom.TCombobox',
            fieldbackground=BG_COLOR,
            background=BG_COLOR,
            foreground=FG_COLOR
        )

        self.window.config(padx=20,pady=20,bg=BG_COLOR)
        self.setup_ui()

    def setup_ui(self):

        self.canvas = Canvas(
            width=400,
            height=260,
            bg=BG_COLOR,
            highlightthickness=0)
        self.image = PhotoImage(file='./images/pass_icon.png')
        self.canvas.create_image(200,130,image=self.image)
        self.canvas.grid(row=0,column=1)


        self.website_lbl = Label(text='Website:',font=FONT,fg=FG_COLOR,bg=BG_COLOR)
        self.website_lbl.grid(row=1,column=0,padx=5,pady=5)

        self.email_lbl = Label(text='Email/Username:',font=FONT,fg=FG_COLOR,bg=BG_COLOR)
        self.email_lbl.grid(row=2,column=0,padx=5,pady=5)

        self.pass_lbl = Label(text='Password:',font=FONT,fg=FG_COLOR,bg=BG_COLOR)
        self.pass_lbl.grid(row=3,column=0,padx=5,pady=5)

        self.website_entry = Entry(fg=FG_COLOR,bg=BG_COLOR,font=BUTTON_FONT)
        self.website_entry.grid(row=1,column=1,columnspan=3,sticky='ew',padx=5,pady=5)

        self.email_entry = ttk.Combobox(style='Custom.TCombobox',
                                        font=BUTTON_FONT,
                                        state='normal')
        self.email_entry.grid(row=2,column=1,columnspan=2,sticky='ew',padx=5,pady=5)

        self.pass_entry = Entry(fg=FG_COLOR,bg=BG_COLOR,font=BUTTON_FONT)
        self.email_entry['values'] = self.load_emails()
        self.pass_entry.grid(row=3,column=1,sticky='ew',padx=5,pady=5)

        self.gen_pass_button = Button(text='Generate Password',
               fg=FG_COLOR,
               bg=BG_COLOR,
               font=BUTTON_FONT,
               activebackground=BUTTON_PRESS,
               command=self.generate_pass).grid(row=3,column=2,sticky='ew',padx=5,pady=5)
        
        self.add_pass_button = Button(text='Add',
                fg=FG_COLOR,
                bg=BG_COLOR,
                font=BUTTON_FONT,
                activebackground=BUTTON_PRESS,
                command=self.add_pass).grid(row=4,column=1,columnspan=2,sticky='ew',padx=5,pady=5)
        
    def add_pass(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.pass_entry.get()

        if len(website)==0 or len(email)==0 or len(password)==0:
            messagebox.showerror(title='Missing Entry',
                                 message='One(or more) of the entries is(are) empty.\nFill them please.')
        else:
            is_ok = messagebox.askokcancel(title='Are You Sure?',
                                        message=f'Confirm the details:\nWebsite: {website}\nEmail: {email}\nPassword: {password}')
            if is_ok:
                with open(file='./pass/data.txt',mode='a') as f:
                    f.write(f'{website} | {email} | {password}\n')
                self.email_entry['values'] = self.load_emails()
                self.website_entry.delete(0,END)
                self.email_entry.delete(0,END)
    
                self.pass_entry.delete(0,END)

    def generate_pass(self):
        self.pass_entry.delete(0,END)
        password = pass_gen()
        pyperclip.copy(password)
        self.pass_entry.insert(0,password)

    def load_emails(self):
        emails = set()

        try:
            with open('./pass/data.txt','r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    email = parts[1].strip()
                    emails.add(email)
        except FileNotFoundError:
            pass

        return sorted(list(emails))