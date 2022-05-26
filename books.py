import json
import pandas as pd

booksFile = 'books.json'

paragraphs = []
notes = []
chapters = []
books = []
book = ''

#Chapters = [{'ChapterTitle':['DataFrame1','DataFrame2','DataFrame3']}]

#Create
def new_book(bookName,chapterTitle,p,n):
    try:
        paragraphs.append(p)
        notes.append(n)
    except:
        pass
    file = f'{bookName}.json'
    chapter = {chapterTitle:(paragraphs,notes)}
    data = []
    with open(file, 'w') as f:
        data.append(chapter)
        json.dump(data, f)
        try:
            with open(booksFile, 'r') as f:
                books = json.load(f)
        except:
            pass
        books.append(bookName)
    with open(booksFile, 'w') as f2:
        json.dump(books, f2)

def new_chapter(bookName,chapterTitle,p,n):
    file = f'{bookName}.json'
    chapter = {chapterTitle:(paragraphs,notes)}
    with open(file, 'w') as f:
        data = json.load(f)
        data.append(chapter)
        json.dump(data, f)

#Read/Select
def load_books():
    with open(booksFile, 'r') as f:
        books = json.load(f)
        return books

def load_book(bookName):
    file = f'{bookName}.json'
    with open(file, 'r') as f:
        try:
            data = json.load(f)
        except:
            pass

def load_chapter(bookName,chapTitle):
    file = f'{bookName}.json'
    with open(file, 'r') as f:
        try:
            data = json.load(f)
        except:
            pass
    chapter = data[chapTitle]

def load_chapter_content(bookName,chapTitle):
    pass

#Update/Edit
def add_entry(bookName,chap,entry_type,entry):
    file = f'{bookName}.json'
    with open(file, 'r'):
        data = json.load(f)
        chapter = data[chap]
        paragraphs = chapters[0]
        notes = chapters[1]
        if entry_type == True:
            paragraphs.append(entry)
        else:
            notes.append(entry)
        x = {chap:[paragraphs,notes]}
        chapters.append(x)
    with open(file, 'w') as f:
        json.dump(data, f)

def edit_entry(bookName,chapTitle,entryType,entryNum,entry):
    pass

#Delete
def delete_book(bookName):
    pass

def delete_chapter(bookName,chapTitle):
    pass

def delete_entry(bookName,chapTitle,entryType,entryNum,entry):
    pass
