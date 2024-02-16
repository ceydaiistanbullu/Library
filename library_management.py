class Library():
    def __init__(self):
        self.filename = open("books.txt","a+") #dosyayı acıyorum yoksa olusturuyorum.


    def __del__(self):
        self.filename.close()  #kutuphane nesnesi silinince dosyayı kapatıyorum.
        


    def list_books(self):
        self.filename.seek(0)  # dosyanın basına don
        books = self.filename.readlines()
        if not books:
             print("Kütüphane de kitap bulunmuyor.")
        else:
            print("Kütüphanede ki kitaplar:")
            for book in books:
                book_info = book.strip().split(",")
                print(f"Title: {book_info[0]}, Author: {book_info[1]}") 