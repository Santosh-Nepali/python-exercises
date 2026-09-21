"""
Module 10 program 1


Implement the following class hierarchy using Python: 
A publication can be either a book or a magazine. 
Each publication has a name. 
Each book also has an author and a page count, 
whereas each magazine has a chief editor. 
Also write the required initializers to both classes. 
Create a print_information method to both subclasses for printing out all information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). 
Print out all information of both publications using the methods you implemented.


"""

class Publication:
    def __init__(self, publication_name):
        self.publication_name=publication_name
        
    def print_information(self):
        print(f"Publication : {self.publication_name}")
        
class Book(Publication):
    def __init__(self, publication_name, title, author, page_count):
        super().__init__(publication_name)
        self.title=title
        self.author=author
        self.page_count=page_count
    
    def print_information(self):
        super().print_information()
        print(f" - Title:  {self.title}")
        print(f" - Author: {self.author}")
        print(f" - Page Count : {self.page_count}")

class Magazine(Publication):
    def __init__(self, publication_name, chief_editor):
        super().__init__(publication_name)
        self.chief_editor=chief_editor
        
    def print_information(self):
        super().print_information()
        print(f" - Chief Editor:  {self.chief_editor}")
       
details=[]
details.append(Book('Donald Duck', 'CompartmentNo6', 'Rosa Liksom', '192'))
details.append(Magazine('Donald Duck', 'Aki Hyyppä'))
for d in details:
    print("-"*30)
    d.print_information()
