from flask import Flask, jsonify,render_template, request, redirect, url_for
import random, string

app = Flask(__name__,template_folder='templates_')



books = [
            {
            'id': '1',
            'title':'In Search of Lost Time',
            'author':'Marcel Proust',
            'publication':'1922',
            'imgurl':'https://images-na.ssl-images-amazon.com/images/I/815obLRWCrS.jpg'
            },
            {
             'id': '2',
             'title':'Ulysses',
             'author':'James Joyce',
             'publication':'1922',
             'imgurl':'https://images-eu.ssl-images-amazon.com/images/I/51luXMePwUL.jpg'
            }

]

def generate_id():
    randomId = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)]) 
    return randomId


@app.route('/books', methods=['GET', 'POST'])
def getbooks():
    if request.method =='POST':
        book = {'title': request.json['title']}
        books.append(book)
        return render_template("books.html", books= books)
    else:
         return render_template("books.html", books= books)



@app.route('/')
def root():
    return redirect('/books')


@app.route('/books/<string:title>', methods=['GET','PUT'])
def getbook(title):
    book = {}
    if request.method =='GET':
        for book in books:
            if book['title']==title:
                book_ = book
                print(book_)
        return render_template("book.html", book = book_ )

##editing items not possible 
   # elif request.method == 'PUT':
      #  book = [book for book in books if book['title']==title]
      #  print(book)
      #  book['title'] = request.form['title']
     #   book['author'] = request.form['author']
     #   book['publication']= request.form['publication']
     #   return 'hello from put'

@app.route("/addbook",methods=['POST','GET'])
def add_book():
    book = {}
    if request.method =='POST':
        book['title'] = request.form['title']
        book['imgurl'] = request.form['imgurl']
        book['id'] = generate_id()
        book['author'] = request.form['author']
        book['publication']= request.form['publication']
        books.append(book)
        return redirect(url_for("getbooks"))
    else:
        return render_template("addbook.html")
  

if __name__ == "__main__":
    app.run(debug=True,port=8080)