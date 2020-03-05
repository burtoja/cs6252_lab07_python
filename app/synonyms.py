'''
Created on Mar 3, 2020

@author: Allen Burton
'''
def updateDictionary(thesaurus, key, word):
    if key != "" and word != "":            
        if key in thesaurus:  
            thesaurus[key].append(word)
        else:
            thesaurus[key] = [word]
        return True;
    else:
        return False

def get_synonyms_from_file():
    thesaurus = {}  
    try:
        with open("synonyms.txt", "r") as synonym_file:          
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
        print("Error: File not found")
    except:
        print("Error: Error reading file")
    finally:
        return thesaurus
