class Library():
    def __init__(self):
        self.filename = open("books.txt",mode='a+',encoding='utf-8') #dosyayı acıyorum yoksa olusturuyorum.


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
                print(f"Title: {book_info[0]}, Author: {book_info[0]}") 


    def add_books(self):
        title = input("Enter book title:")
        author = input("Enter book author:")
        release_year = input("Enter first release year:")
        pages = input("Enter number of pages:")
        book_info = f"{title},{author},{release_year},{pages}\n"  #\n alt satıra inmeyi saglıyor. # f"{varıable}" strınge cevırıyor
        self.filename.writelines(book_info)
        print("Kütüphaneye kitap eklenmiştir.")

lib = Library()

lib.add_books()