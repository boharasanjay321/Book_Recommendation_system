from flask import Flask, render_template,request,jsonify
#import mysql.connector as conn
import pickle
import numpy as np

popular_df=pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
similarity_score=pickle.load(open('similarity_score.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
#mydb=conn.connect(host="localhost",user="root",password="Ratlam@123")
app=Flask(__name__)

@app.route('/')
def index():

    return render_template('home.html',
                           book_name=list(popular_df['Book-Title'].values),
                           Author=list(popular_df['Book-Author'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values),
                           image= list(popular_df['Image-URL-S'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_book',methods=['POST'])
def recommend():
    user_input=request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_item = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]
    # return distance
    data = []
    for i in similar_item:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)


    print(data)
    return render_template('recommend.html',data=data)

@app.route('/contact')
def con():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')



if __name__== '__main__' :
   app.run(debug=True)

