class Library():
    def __init__(self):
        self.filename = open("books.txt",mode='a+',encoding='utf-8') #dosyayı acıyorum yoksa olusturuyorum.

    def __del__(self):
        self.filename.close()  #kutuphane nesnesi silinince dosyayı kapatıyorum.

    def list_books(self):
        self.filename.seek(0)  # dosyanın basına don
        self.books = self.filename.readlines()
        if not self.books:
             print("Kütüphane de kitap bulunmuyor.")
        else:
            print("Kütüphanede ki kitaplar:")
            for book in self.books:
                book_info = book.strip().split(",")
                print(f"{book_info[0]}, {book_info[1]}, {book_info[2]}, {book_info[3]}") 

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
        self.filename.seek(0)  # sıfırlıyor
        self.books = self.filename.readlines()
        found = False
        for i, book in enumerate(self.books):
            if str(title) in str(book):
                del self.books[i]
                found = True
                break
        if found:
            self.filename.seek(0)
            self.filename.truncate()  #dosyanın icini siliyor
            self.filename.writelines(self.books)  #güncellenmis kitap listesini dosyaya yazar
            print(f"The book '{title}' has been removed from the library.")
            # print(self.books)
        else:
            print(f"The book '{title}' is not found in the library.")


def main():
    lib = Library()

    print(
        """
        Kütüphane Yönetim Sistemine Hoşgeldiniz!
        1. Kitapları Listele
        2. Kitap Ekle
        3. Kitap Sil
        Q Çıkış
        """
          )
          

    choice = input("Yapmak istediğiniz işlemi seçiniz: ")
    print("----------------")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_books()
    elif choice == "3":
        lib.remove_books()
    elif choice == "Q":
        exit()
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek giriniz.")
        

if __name__ == "__main__":
    main()
   