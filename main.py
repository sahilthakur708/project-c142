from flask import Flask,jsonify,request
import pandas as pd

all_articles=[]

data=pd.read_csv("articles.csv")
all_articles=data[1:]

liked_articles=[]
not_liked_articles=[]

app=Flask(__name__)

@app.route('/get_articles')
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route('/liked_articles', methods=["POST"])
def liked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route('/not_liked_articles', methods=["POST"])
def not_liked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()