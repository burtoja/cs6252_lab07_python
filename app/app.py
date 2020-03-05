'''
Created on Jan 20, 2020

@author: CS6252
'''
'''from flask import Flask
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
'''

def updateDictionary(dictionary, key, word):
    if key != "" and word != "":            
        if key in thesaurus:  
            thesaurus[key].append(word)
            '''print("UPDATED: (" + key + ", " + word + ") is a key already" )'''
        else:
            thesaurus[key] = [word]
            '''print("ADDED: (" + key.strip() + ", " + word + ") is NOT a key already" )'''
        return True;
    else:
        '''print("ERROR: Missing either key or word")'''
        return False
 
try:
    with open("../synonyms55.txt", "r") as synonym_file: 
        thesaurus = {}  
        for line_number, line in enumerate(synonym_file.readlines()):
            words = line.split(",")
            try:
                if not updateDictionary(thesaurus, words[0].strip(), words[1].strip()) and not updateDictionary(thesaurus, words[1].strip(), words[0].strip()):
                    line_number += 1
                    print ("Error in line {}: Missing word ({}, {})".format(line_number, words[0].strip(), words[1].strip()) )            
            except IndexError:
                line_number += 1
                print("Error in line {}: No comma ({})".format(line_number, words[0].strip()))         
        print (thesaurus)
except FileNotFoundError:
    thesaurus = {} 
    print("Error: File not found")
except:
    print("Error: Error reading file")
        
