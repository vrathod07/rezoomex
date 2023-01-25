
import numpy
# import spacy
# import numpy 
# import nltk
# nlp = spacy.load('en_core_web_sm')
# def ner(sentence):
  
#   #  nltk.download('punkt')
#   #  nltk.download('averaged_perceptron_tagger')
#   #  nltk.download('maxent_ne_chunker')
#   #  nltk.download('words')
#    tuple_list =[]

#    for sent in nltk.sent_tokenize(sentence):
#     for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#        if hasattr(chunk, 'label'):
            
#          label= chunk.label()
#          word= ' '.join(c[0] for c in chunk)
#          print("word =",word)
#          tuple= (word,label)
#          tuple_list.append(tuple)

#          print(chunk.label(), ' '.join(c[0] for c in chunk))

#    ner_dict = dict(tuple_list)
#    return ner_dict
#   # print(ner_dict)

# def ner_driver(sentence):
#        #sentence given by resume text paragraphs
#        # sample sentence given now
#        ner_output= ner(sentence)
#        #print(ner_output)

# def ner_spacy(word):
#   print(nlp(word))

import nltk
from nltk.tag import pos_tag

def ner(sent):
    sent = nltk.pos_tag(sent)
    if(sent[0][1] == "NN"):
      return "Name"
    if(sent[0][1] == "JJ"):
      return "Location"
    return sent
import spacy  

from spacy import displacy  
  
nlp = spacy.load('en_core_web_sm')  
# Process whole documents  
text = ("When Sebastian Thrun started working on self-driving cars at "  
        "Google in 2007, few people outside of the company took him "  
        "seriously. “I can tell you very senior CEOs of major American "  
        "car companies would shake my hand and turn away because I wasn’t "  
        "worth talking to,” said Thrun, in an interview with Recode earlier "  
        "this week.")  
doc = nlp(text)  