import sqlite3 as sql
import pandas as pd
import datetime as dt
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty,ListProperty
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider
from bookwriter_backend import *


class Homepage(Screen):
    pass

class Login(Screen):
    pass

class Register(Screen):
    pass

class CreateBook(Screen):
    pass

class Manager(ScreenManager):
    pass

class BookWriterApp(App):
    books = ListProperty()
    chapters = ['Create Chapter','Edit Chapter']
    paragraphs = ListProperty()
    notes = ListProperty()
    book_objects = ListProperty(['Edit Note','Edit Paragraph','Create Note','Create Paragraph'])
    user = StringProperty('')
    book = StringProperty('')
    chapter = StringProperty('')

    def pickpage(self):
        self.root.current = 'hp'

    def reg(self,fname,lname,uname,email,pword):
        create_user(fname,lname,uname,email,pword)

    def verified(self,email,pword):
        conn = sqlite3.connect('book_users6.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Users')
        rows = cur.fetchall()
        conn.close()
        df = pd.DataFrame(rows)
        df.columns = ['fname','lname','uname','email','pword']
        ver_key = [df['email'].to_list(),df['pword'].to_list()]
        for (e,f) in zip(ver_key[0],ver_key[1]):
            x = e + f
            user_input = (email + pword)
            if x == user_input:
                self.user = email
                self.root.current = 'hp'
                self.books = choose_book(email)
                self.chapters = choose_chapter(self.user,self.book)

    def add_book(self,book_title):
        create_book(self.user,book_title)

    def add_chapter(self,book_title,chapter_title):
        if chapter_title == 'Create Chapter':
            create_book(self.user,self.book)
            create_chapter(self.user,book_title,chapter_title)
        else:
            pass

    def add(self,content):
        if content == 'Create Note':
            create_note(self.user,self.book,self.chapter)
            self.root.ec.text = ''
        elif content == "Create Paragraph":
            create_paragraph(self.user,self.book,self.root.ec.text,self.chapter)
            self.root.ec.text = ''
        else:
            pass

    def sel_book(self,book_title):
        self.book = book_title.text
        try:
            self.chapters = choose_chapter(self.user,self.book)
        except Exception as e:
            self.root.current = 'cb'

    def sel_chapter(self,chapter_title):
        try:
            self.chapters = choose_chapter(self.user,self.book)
        except Exception as e:
            if self.chapters == 'Create Chapter':
                pass
            else:
                self.chapters = chapter_title.text


    def select(self,content):
        if content == 'Edit Note':
            self.root.sd.text = str(select_note(self.user,self.book,self.chapter))
        elif content == "Edit Paragraph":
            self.root.sd.text = str(select_paragraph(self.user,self.book,self.chapter))
        else:
            pass

    def update(self,book,paragraph,chapter_link):
        select_paragraph(self.user,book,paragraph,chapter_link)

    def del_book(self,book_title):
        delete_book(self.user,book_title)

    def del_chapter(self,book_title,chapter_title):
        delete_chapter(self.user,book_title,chapter_title)

    def delete(self,book,chapter_link,content):
        if content == 'Edit Note':
            delete_note(self.user,self.book,self.chapter)
        elif content == "Edit Paragraph":
            delete_paragraph(self.user,self.book,self.chapter)
        else:
            pass
        self.root.ec.text = ''



    def build(self):
        kv = Builder.load_file("bookwriter.kv")
        self.title = 'BookWriter'
        return kv

if __name__ == '__main__':
    BookWriterApp().run()
