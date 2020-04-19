import csv
import string

import pandas as pd
#from intertools import chain
from _csv import reader


my_list = []
file = '/home/srujanee/projects/api/book.csv'

class Books:
    def __init__(self,bookName,author,publisher,price,dateOfPublication,ISBNCode):
       self.bookName = bookName
       self.author = author
       self.publisher = publisher
       self.price = price
       self.dateOfPublication = dateOfPublication
       self.ISBNCode = ISBNCode


#df = pd.read_csv('/home/srujanee/projects/api/book.csv')



with open(file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        #print(row['BookName'], row['Author'], row['Publisher'],row['Price'],row['Date of Publication'],row['ISBN Code'])
        my_list.append(Books(row['BookName'], row['Author'], row['Publisher'],row['Price'],row['Date of Publication'],row['ISBN Code']))

print(my_list)


def csv_fn(file):
    df = pd.read_csv(file)
    pd.options.display.max_columns = len(df.columns)
    print(df.head())
    #df.style.set_properties(**{'text-align': 'left'})
    #print(df)
    return df.T.to_dict()


# def nested(isbn,my_list):
#     return any(isbn in nested for nested in my_list)

def search(my_list,valueToSearch,keyTosearch):
    exp_List=[]
    for k,i in my_list.items():
       for key,value in i.items():
           if str(keyTosearch) in str(key):
               if str(valueToSearch) in str(value):
                 exp_List =exp_List+list(i.items())

    return exp_List

df=csv_fn(file)
#print(df)
key = input("Enter key to serach --options/--BookName/Author/Publisher/Price/Date of Publication/ISBN Code")
value = input("Enter the Value to be searched : ")

#print(nested(isbn,df),'List Books')
print('Matched Book List--',search(df,value,key))







