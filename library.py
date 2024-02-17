class Library():
    def __init__(self):
        self.filename = open("books.txt",mode='a+',encoding='utf-8') #dosyayı acıyorum yoksa olusturuyorum.


    def __del__(self):
        self.filename.close()  #kutuphane nesnesi silinince dosyayı kapatıyorum.
        


    def list_books(self):
        self.filename.seek(0)  # dosyanın basına don
        books = self.file.readlines()
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

    def remove_books(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)  # sıfırlıyor
        books = self.file.readlines()
        found = False
        for i, book in enumerate(books):
            if title in book:
                del books[i]
                found = True
                break
        if found:
            self.file.seek(0)
            self.file.truncate()  #dosyanın icini siliyor
            self.file.writelines(books)  #güncellenmis kitap listesini dosyaya yazar
            print(f"The book '{title}' has been removed from the library.")
        else:
            print(f"The book '{title}' is not found in the library.")


#lib = Library()

#lib.add_books()
#lib.remove_books()

    def menu_göster(self):
        print("\nKütüphane Yönetim Sistemine Hoşgeldiniz!")
        print("1. Kitapları Listele")
        print("2. Kitap Ekle")
        print("3. Kitap Sil")
        print("Q Çıkış")

#Library = Library("books.txt")
#Library.add_books()
#Library.remove_books()
#Library.ana_menu_göster()
#Library.list_books()

while True:
    menu_göster()
    choise = input("Yapmak istediğiniz işlemi seçiniz: ")

    if choise == "1":
        list_books()
    elif choise == "2":
        add_books()
    elif choise == "3":
        remove_books()
    elif choise == "Q":
        break
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek giriniz.")