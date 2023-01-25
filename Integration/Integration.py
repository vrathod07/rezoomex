from concept_extraction_module import concept_extraction
from association_mining import search
from wsd_module import wsd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from ner2 import *
import nltk
import re
# from external_knowledge_linking_1 import coursera_scrapping
# from external_knowledge_linking_1 import *


def identify_dates(entity):
    months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if(entity.lower() in months):
        return "Month"
    if(entity.isdigit() and 1880 < int(entity) < 2030):
        return "Year"
    return None
    
def identify_pincode(entity):
    if(len(entity) == 6 and entity.isdigit()):
        if(int(entity[0]) != 0):
            return "PinCode"
    else:
        return None
        

def main(entity):
    gazateer = identify_pincode(entity)
    if(gazateer == None):
        gazateer = identify_dates(entity)
    if(gazateer == None):
        gazateer = wsd(entity)[2]
        # if(res is tuple):
        #     gazateer = res[3]
        # else:
        #     gazateer = None
    if(gazateer == None):
        gazateer = search(entity)
    if(len(gazateer) == 0):
        try:
            gazateer = concept_extraction(entity)[1]
        except:
            gazateer = None
    if(gazateer == None):
        try:
            gazateer = ner([entity])
        except:
            gazateer = None

    return gazateer
        
words = ["Elon","Blair","Vaishnavi", "IIT","Indian Institute of Technology","Developer","AWS","January 2015","Computer Engg","BSCs","electrical engineer","Caltech","NYU","UNICEF","jQuery","Tester","RB Electronics"," A.K.Mahavidyalya","Accenture","Deloitte"]  
correct_result = ["Name",'Name','Name','Institutes','Institutes','Designation', "Skill","Date","Branch IT", 'Designation','Institutes','Institutes','Company',"Skill","Designatioon","Company","Institutes","Company","Company"]  
result = {}    
for word in words:
    res = main(word)
    result.update({word:res})
print(result)
conf_matrix = confusion_matrix(y_true=correct_result, y_pred=list(result.values()))
print(accuracy_score(correct_result , list(result.values()))*100)
print(recall_score(correct_result, list(result.values())))
print(precision_score(correct_result, list(result.values()))*100)
print(f1_score(correct_result, list(result.values())))
# {'Elon': 'Name', 'Blair': 'Name', 'Vaishnavi': 'Name', 'IIT': 'Institutes', 'Indian Institute of Technology': 'Institutes', 'Developer': 'Designation', 'AWS': ['Microsoft Azure', 'Google Cloud', 'IBM Cloud', 
# 'VMWare Cloud'], 'January 2015': 'Name', 'Computer Engg': 'Branch IT', 'BSCs': 'Branch IT', 'electrical engineer': 'Designation', 'Caltech': 'Institutes', 'NYU': 'Institutes', 'UNICEF': 'Company', 'India': 'Duration', 'America': [('America', 'NNP')]}

