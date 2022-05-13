import sqlite3
import pandas as pd
import datetime as dt

now = dt.datetime.now()
today = dt.date(now.year,now.month,now.day)

pages = 0
book_chapters = []
chapter_paragraphs = []
chapter_notes = []
chapter_sources = []

def create_user(fname,lname,uname,email,pword):
    fname,lname,uname,email,pword = fname,lname,uname,email,pword
    conn = sqlite3.connect('book_users6.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Users(Fname TEXT,Lname TEXT,Username TEXT,Email TEXT, Pword TEXT)''')
    cur.execute("INSERT INTO Users(Fname,Lname,Username,Email,Pword) VALUES(?,?,?,?,?)",(fname,lname,uname,email,pword))
    conn.commit()
    conn.close()

def create_book(uname,title):
    date_created = today
    conn = sqlite3.connect(f'{uname}-{title}.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Bookcontentz(BookTitle TEXT,Date TEXT)''')
    cur.execute("INSERT INTO Bookcontentz(BookTitle,Date) VALUES(?,?)",(title,date_created))
    conn.commit()
    conn.close()

def create_chapter(uname,book,title):
    date_created = today
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Chapter_content(Chapter TEXT,Chapter_title TEXT,Date TEXT)''')
    cur.execute("SELECT * FROM Chapter_content")
    row = cur.fetchall()
    try:
        chap_num = len(rows) + 1
        cur.execute("INSERT INTO Chapter_content(Chapter,Chapter_title,Date) VALUES(?,?,?)",(chap_num,title,date_created))
        conn.commit()
        conn.close()
    except Exception as e:
        chap_num = 1
        cur.execute("INSERT INTO Chapter_content(Chapter,Chapter_title,Date) VALUES(?,?,?)",(chap_num,title,date_created))
        conn.commit()
        conn.close()

def create_paragraph(uname,book,paragraph,chapter_link):
    date_created = today
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Parag_content(Par_num INT,Paragraph TEXT,Date TEXT)''')
    cur.execute("SELECT * FROM Parag_content")
    rows = cur.fetchall()
    try:
        par_num = len(rows) + 1
    except Exception as e:
        par_num = 1
    cur.execute("INSERT INTO Parag_content(Par_num,Paragraph,Date) VALUES(?,?,?)",(par_num,paragraph,date_created))
    conn.commit()
    conn.close()

def create_note(uname,book,note,chapter_link):
    date_created = today
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Note_content(Note_num INT PRIMARY KEY,Note TEXT,Date TEXT)''')
    cur.execute("SELECT * FROM Note_content")
    rows = cur.fetchall()
    try:
        note_num = len(rows) + 1
    except Exception as e:
        note_num = 1
    cur.execute("INSERT INTO Note_content(Note_num,Note,Date) VALUES(?,?)",(note_num,paragraph,date_created))
    conn.commit()
    conn.close()

def choose_book(uname):
    f = ['book1']
    conn = sqlite3.connect(f'{uname}-books.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Bookcontentz")
        rows = cur.fetchall()
        conn.close()
        books = pd.DataFrame(rows)
        books.columns = ['title','date']
        book_title = books['title'].tolist()
        return book_title
    except Exception as e:
        return f


def choose_chapter(uname,book):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Chapter_content")
        rows = cur.fetchall()
        conn.close()
        chapter = pd.DataFrame(rows)
        chapter.columns = ['num','title','date']
        chapter_title = chapter['title'].tolist()
        return chapter_title
    except Exception as e:
        chapter_title = 'Create Chapter'
        return chapter_title


def select_paragraph(uname,book,chapter_link):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Parag_content")
    paragraph = cur.fetchall()
    conn.close()
    par = pd.DataFrame(paragraph)
    par.columns = ['num','content','date']
    par = par['content'].tolist()
    for e in par:
        return e

def select_note(uname,book,chapter_link):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Note_content")
    note = cur.fetchall()
    conn.close()
    return note

def edit_paragraph(uname,book,chapter_link,id,new_content):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute("UPDATE Parag_content SET Paragraph=? where Par_num=?",(id,new_content))
    conn.commit()
    conn.close()

def edit_note(uname,book,chapter_link,id,new_content):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute("UPDATE Note_content SET Note=? where Note_num=?",(id,new_content))
    conn.commit()
    conn.close()

def delete_paragraph(uname,book,chapter_link,id):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Parag_content where Par_num=?",(id))
    conn.commit()
    conn.close()

def delete_note(uname,book,chapter_link):
    conn = sqlite3.connect(f'{uname}-{book}.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Note_content where Note_num=?",(id))
    conn.commit()
    conn.close()
