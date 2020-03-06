'''
Created on Jan 20, 2020

@author: CS6252
'''

from flask import Flask
from synonyms import get_synonyms_from_file
app = Flask(__name__)

@app.route('/synonyms')
def get_all_synonyms():
    all_synonyms = get_synonyms_from_file()
    return all_synonyms

@app.route('/synonym/<string:word>')
def get_synonym(word):
    all_synonyms = get_synonyms_from_file()
    if word in all_synonyms.keys():
        return {word: all_synonyms[word]}
    else: 
        return {"message": "No synonyms available for " + word} 
