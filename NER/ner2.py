# Step One: Import nltk and download necessary packages
 
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
 
# Step Two: Load Data
#sentence = "WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E. Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcement."
# Step Three: Tokenise, find parts of speech and chunk words 


def ner(sentence):
   tuple_list =[]

   for sent in nltk.sent_tokenize(sentence):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
       if hasattr(chunk, 'label'):
            
         label= chunk.label()
         word= ' '.join(c[0] for c in chunk)
         print("word =",word)
         tuple= (word,label)
         tuple_list.append(tuple)

         print(chunk.label(), ' '.join(c[0] for c in chunk))

   ner_dict = dict(tuple_list)
   return ner_dict
  # print(ner_dict)

def ner_driver():
       #sentence given by resume text paragraphs
       # sample sentence given now
       sentence = "WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E. Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcemen"
       ner_output= ner(sentence)
       #print(ner_output)
