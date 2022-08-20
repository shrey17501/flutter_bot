
from flask import Flask, request, jsonify
import spacy
app = Flask(__name__)

head = [

    {"id":1,
    "title":"introduction to algorithm"},
    {"id":2,
    "title":"Java2"}
]
intent = [
    {"first":"take rest"},
    {"second":"take medicine"}
]

s = "i have fever"
nouns = []
nlp = spacy.load("en_core_web_sm")
def fun(s):
    doc = nlp(str(s))
    for token in doc:
        if (token.pos_ == "NOUN" and token.dep_ == "dobj") or (token.pos_ == "NOUN" and token.dep_ == "attr"):
            nouns.append(token)
    for token in doc:
        if token.pos_ == "VERB" and token.dep_ == "ROOT":
            nouns.append(token)
    for token in doc:
        if (token.pos_ == "ADJ" and token.dep_ == "acomp") or (token.pos_ == "ADJ" and token.dep_ == "amod"):
            nouns.append(token)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            nouns.append(ent)

fun(s)

@app.route('/book', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        for t in nouns:
            if str(t) == 'fever':
                intent[1]=intent[0]
                return intent[1]
        else:
            'add books'

    if request.method == 'POST':
        id = head[-1]['id']+1
        new_title = request.form['title']

        new_obj = {
            'id':id,
            'title':new_title
        }
        head.append(new_obj)
        return jsonify(head)

if __name__ == "__main__":
    app.run()