dic ={'Harry Potter':{
        'author':'J.K.Rowling',
        'publisher':'Bloomsbury',
        'price':600,
        'published':2000,
        'ISBN Code':446310785,
              },
    'To Kill a Mockingbird':{
        'author':'Harper Lee Read',
        'publisher':'J. B. Lippincott & Co.',
        'price':500,
        'published':1960,
        'ISBN Code':446310786},

    'A Fire Upon the Deep': {
        'author': 'Vernor Vinge',
        'publisher': 'J. B. Lippincott & Co.',
        'price': 500,
        'published': 1992,
        'ISBN Code':446310788},
    'Ancillary Justice':{
        'author': 'Ann Leckie',
        'publisher': 'Dzanc Books (Detroit, MI)',
        'price': 800,
        'published': 2014,
        'ISBN Code':446310710
    },
  'Redshirts':{
    'author': 'John Scalzi',
    'publisher': 'Penguin Books (London, UK)',
    'price': 900,
    "published": 2013,
    "ISBN Code": 446310711
  },

   'Among Others':{
    'author': 'Jo Walton',
    'publisher': 'Phaidon (London and New York City)',
    'price': 400,
    'published': 2012,
    'ISBN Code': 446310712
  },
  'Blackout, All Clear (Vol. 2 - Blackout)':{
    'author': "Connie Willis",
    'publisher': "McSweeney's (San Francisco, CA)",
    'price': 600,
    'published': 2011,
    'ISBN Code': 446310713
  },
  'The Windup Girl':{
    'author': 'Paolo Bacigalupi',
    'publisher':'Graywolf Press (Minneapolis, MN)',
    'price': 500,
    'published': 2010,
    'ISBN Code': 446310714
  },
  'The City & The City':{
    'author': 'China Mieville',
    'publisher': 'Dzanc Books (Detroit, MI)',
    'price': 700,
    'published': 2010,
    'ISBN Code': 446310715
  },
  'The Graveyard Book':{
    'author':'Neil Gaiman',
    'publisher': 'Penguin Books (London, UK)',
    'price': 900,
    'published': 2009,
    'ISBN Code': 446310716
  },
  'The Yiddish Policemen Union':{
    'author': 'Michael Chabon',
    'publisher': 'Rare Bird Books (Los Angeles, CA)',
    'price': 300,
    'published': 2008,
    'ISBN Code': 446310717
  },
  'The Yiddish Policemen Union1':{
    'author': 'Michael Chabon',
    'publisher': 'Rare Bird Books (Los Angeles, CA)',
    'price': 300,
    'published': 2008,
    'ISBN Code': 446310717
  }

}
def iterateDic(dic):
    for k,info in dic.items():
        print("\nBookName:", k)
        for v in info:
            print(str(v) + ':', str(info[v]))





#with open('/home/srujanee/projects/api/book.csv') as csv_file:
with open('/home/srujanee/projects/api/book.csv', 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    column_names = csv_dict_reader.fieldnames
    print('Header ',column_names)
    for row in csv_dict_reader:
        if row['Author'] == 'Vernor Vinge':
            print(row)
        list_books.append(row)
print(list_books)

def searchbyISBN(my_list):
    expeclist_books = []
    isbn = int(input("Enter the ISBN No to be searched : "))
    #li_isbn = list(isbn.split(" "))
    print(type(isbn),isbn)
   # res = isbn in (isbn for sublist in my_list for isbn in sublist)
   #  res1 = any(isbn in sublist for sublist in my_list)
   #  print(res1)
    print(my_list)
    for i in my_list:
        if isbn not in i:
            expeclist_books=i
            break

    return expeclist_books





