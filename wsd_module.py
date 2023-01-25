import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import wordnet as wn
import wikipedia
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nltk.download('wordnet')
nltk.download('omw-1.4') 


def read_all_files():
  company_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Company.txt",header=None,names=["Company"],on_bad_lines='skip')
  desg_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Designation.txt",header=None,names=["Designation"],on_bad_lines='skip')
  insti_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\InstituteGrade-I.txt",header=None,names=["Institutes"],on_bad_lines='skip')
  address_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Address_Keywords.txt",header=None,names=["Address"],on_bad_lines='skip')
  awards_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\AwardAndRecognitionAnchor (copy).txt",header=None,names=["Awards"],on_bad_lines='skip')
  branchIT_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Branch-IT.txt",header=None,names=["BranchIT"],on_bad_lines='skip')
  branchNonIT_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Branch-NonIT.txt",header=None,names=["BranchNonIT"],on_bad_lines='skip')
  certificates_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Certification.txt",header=None,names=["Certificates"],on_bad_lines='skip')
  diplomat_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Diploma.txt",header=None,names=["Diploma"],on_bad_lines='skip')
  domain_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Domain.txt",header=None,names=["Domain"],on_bad_lines='skip')
  duration_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\DurationAnchor.txt",header=None,names=["DurationAnchor"],on_bad_lines='skip')
  hardware_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\DeviceAndHardWare.txt",header=None,names=["DeviceAndHardWare"],on_bad_lines='skip')
  education_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\EducationAnchor.txt",header=None,names=["EducationAnchor"],on_bad_lines='skip')
  experience_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\ExperienceAnchor.txt",header=None,names=["ExperienceAnchor"],on_bad_lines='skip')
  functionality_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Functionality.txt",header=None,names=["Functionality"],on_bad_lines='skip')
  graduate_df = pd.read_csv("orphan-entity-allocation\WSD\data\gazetteers\All\Graduate.txt",header=None,names=["Graduate"],on_bad_lines='skip')
  desgabbr_df = pd.read_csv("orphan-entity-allocation\WSD\data\desg_abbr.txt",sep=":",header=None,names=["source","target"],on_bad_lines='skip')
  instiabbr_df = pd.read_csv("orphan-entity-allocation\WSD\data\insti_abbr.txt",sep=":",header=None,names=["source","target"],on_bad_lines='skip')
  compabbr_df = pd.read_csv("orphan-entity-allocation\WSD\data\comp_abbr.txt",sep=":",header=None,names=["source","target"],on_bad_lines='skip')
  graduate_abbr = pd.read_csv("orphan-entity-allocation\WSD\data\graduate_abbr.txt",header=None,names=["source","target"],on_bad_lines='skip')
  diploma_abbr = pd.read_csv("orphan-entity-allocation\WSD\data\diploma_abbr.txt",header=None,names=["source","target"],on_bad_lines='skip')
  return company_df,desg_df,insti_df,address_df,awards_df,branchIT_df,branchNonIT_df,certificates_df,diplomat_df,domain_df,duration_df,hardware_df,education_df,experience_df,functionality_df,graduate_df,desgabbr_df,instiabbr_df,compabbr_df,graduate_abbr,diploma_abbr

company_df,desg_df,insti_df,address_df,awards_df,branchIT_df,branchNonIT_df,certificates_df,diplomat_df,domain_df,duration_df,hardware_df,education_df,experience_df,functionality_df,graduate_df,desgabbr_df,instiabbr_df,compabbr_df,graduate_abbr,diploma_abbr = read_all_files()
def synonymsCreator(word):
	synonyms = []

	for syn in wn.synsets(word):
		for i in syn.lemmas():
			synonyms.append(i.name())

	return synonyms


def get_synonymDataFrame(df,column):
  source = []
  target = []
  for i in df[column]:
    try:
      result = synonymsCreator(i)
      for x in result:
        source.append(i)
        target.append(x)
    except:
      source.append(i)
      target.append("None")
  df_synonym = pd.DataFrame(list(zip(source,target)),columns=["source","target"])
  df_synonym.to_csv(f"orphan-entity-allocation\WSD\data_new\{column}__synonym.csv")

def get_HypernymsDataFrame(df,column):
  source = []
  target = []
  for i in df[column]:
    try:
      syn = wn.synsets(i)[0]
      result = syn.hypernyms()
      for x in result:
        source.append(i)
        target.append(x.name().split('.')[0])
    except:
      source.append(i)
      target.append("None")
  df_hypernym = pd.DataFrame(list(zip(source,target)),columns=["source","target"])
  df_hypernym.to_csv(f"orphan-entity-allocation\WSD\data_new\{column}_hypernym.csv")

def get_HyponymsDataFrame(df,column):
  source = []
  target = []
  for i in df[column]:
    try:
      syn = wn.synsets(i)[0]
      result = syn.hyponyms()
      for x in result:
        source.append(i)
        target.append(x.name().split('.')[0])
    except:
      source.append(i)
      target.append("None")
  df_hyponym = pd.DataFrame(list(zip(source,target)),columns=["source","target"])
  df_hyponym.to_csv(f"orphan-entity-allocation\WSD\data_new\{column}_hyponym.csv")


def edit_distance(word1, word2):
  W1_LEN = len(word1)
  W2_LEN = len(word2)
  dp = [[0] * (W1_LEN + 1) for _ in range(W2_LEN + 1)]
  for i in range(W1_LEN):
      dp[W2_LEN][i] = W1_LEN - i
  for i in range(W2_LEN):
      dp[i][W1_LEN] = W2_LEN - i
  for i in range(W2_LEN - 1, -1, -1):
      for j in range(W1_LEN - 1, -1, -1):
          if word2[i] == word1[j]:
              dp[i][j] = dp[i + 1][j + 1]
          else:
              dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1]) + 1
  return dp[0][0]

def getDataFrame():
    get_HyponymsDataFrame(desg_df,"Designation")
    get_HypernymsDataFrame(desg_df,"Designation")
    get_synonymDataFrame(address_df,"Address")
    get_HyponymsDataFrame(address_df,"Address")
    get_HypernymsDataFrame(address_df,"Address")
    get_synonymDataFrame(branchIT_df,"BranchIT")
    get_HyponymsDataFrame(branchIT_df,"BranchIT")
    get_HypernymsDataFrame(branchIT_df,"BranchIT")
    get_synonymDataFrame(branchNonIT_df,"BranchNonIT")
    get_HyponymsDataFrame(branchNonIT_df,"BranchNonIT")
    get_HypernymsDataFrame(branchNonIT_df,"BranchNonIT")
    get_synonymDataFrame(branchNonIT_df,"BranchNonIT")
    get_HyponymsDataFrame(duration_df,"DurationAnchor")
    get_HypernymsDataFrame(duration_df,"DurationAnchor")
    get_synonymDataFrame(duration_df,"DurationAnchor")
    get_HyponymsDataFrame(hardware_df ,"DeviceAndHardWare")
    get_HypernymsDataFrame(hardware_df ,"DeviceAndHardWare")
    get_synonymDataFrame(hardware_df ,"DeviceAndHardWare")
    get_HyponymsDataFrame(experience_df,"ExperienceAnchor")
    get_HypernymsDataFrame(experience_df,"ExperienceAnchor")
    get_synonymDataFrame(experience_df,"ExperienceAnchor")
    get_HyponymsDataFrame(education_df,"EducationAnchor")
    get_HypernymsDataFrame(education_df,"EducationAnchor")
    get_synonymDataFrame(education_df,"EducationAnchor")
    #df_desg_synonym.to_csv("Designation_synonym.csv")
    # return df_desg_hyponym,df_desg_hypernym,df_desg_synonym


def to_csv(df_desg_hyponym,df_desg_hypernym):
  desgabbr_df.to_csv("Designation_abbrevation.csv")
  compabbr_df.to_csv("Company_abbrevation.csv")
  
  df_desg_hyponym.to_csv("Designation_Hyponym.csv")
  df_desg_hypernym.to_csv("Designation_Hypernym.csv")
  instiabbr_df.to_csv("Institute_abbrevation.csv")


def identity_orphan(entity):

    df_desg_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\Designation_synonym.csv")
    df_desg_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\Designation_Hyponym.csv")
    df_desg_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\Designation_Hypernym.csv")
    df_addr_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\Address_synonym.csv")
    df_addr_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\Address_hyponym.csv")
    df_addr_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\Address_hypernym.csv")
    df_branchIT_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\BranchIT_synonym.csv")
    df_branchIT_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\BranchIT_hyponym.csv")
    df_branchIT_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\BranchIT_hypernym.csv")
    df_branchNonIT_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\BranchNonIT_synonym.csv")
    df_branchNonIT_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\BranchNonIT_hyponym.csv")
    df_branchNonIT_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\BranchNonIT_hypernym.csv")
    df_hardware_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\DeviceAndHardWare_synonym.csv")
    df_hardware_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\DeviceAndHardWare_hyponym.csv")
    df_hardware_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\DeviceAndHardWare_hypernym.csv")
    df_duration_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\DurationAnchor_synonym.csv")
    df_duration_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\DurationAnchor_hyponym.csv")
    df_duration_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\DurationAnchor_hypernym.csv")
    df_experience_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\ExperienceAnchor_synonym.csv")
    df_experience_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\ExperienceAnchor_hyponym.csv")
    df_experience_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\ExperienceAnchor_hypernym.csv")
    df_education_synonym = pd.read_csv("orphan-entity-allocation\WSD\data\EducationAnchor_synonym.csv")
    df_education_hyponym = pd.read_csv("orphan-entity-allocation\WSD\data\EducationAnchor_hyponym.csv")
    df_education_hypernym = pd.read_csv("orphan-entity-allocation\WSD\data\EducationAnchor_hypernym.csv")
   
    
    
    min_c = pow(10,2)
    min_d = pow(10,2)
    min_i = pow(10,2)
    entity = str(entity)
    ## Search in the database 
    if entity in list(company_df["Company"]): 
        return "Company"
    elif entity in list(insti_df["Institutes"]): 
      return "Institutes"
    elif entity in list(address_df["Address"]): 
      return "Address"
    elif entity in list(desg_df["Designation"]): 
      return "Designation"
    elif entity in list(awards_df["Awards"]): 
      return "Awards"
    elif entity in list(branchIT_df["BranchIT"]): 
      return "Branch IT"
    elif entity in list(branchNonIT_df["BranchNonIT"]): 
      return "Branch Non IT"
    elif entity in list(duration_df["DurationAnchor"]): 
      return "Duration"
    elif entity in list(hardware_df["DeviceAndHardWare"]): 
      return "Device and Hardware"
    elif entity in list(experience_df["ExperienceAnchor"]): 
      return "Experience"
    elif entity in list(education_df["EducationAnchor"]): 
      return "Education"
    else:
      ##search for abbrevations
      if entity in list(desgabbr_df["source"]) or entity in list(desgabbr_df["target"]): 
        return  "Designation"
      elif entity in list(instiabbr_df["source"]) or entity in list(instiabbr_df["target"]):
        return "Institutes"
      elif entity in list(compabbr_df["source"]) or entity in list(compabbr_df["target"]):
        return "Company"
      elif entity in list(graduate_abbr["source"]) or entity  in list(graduate_abbr["target"]):
        return "Graduate_Proffesional"
      elif entity in list(diploma_abbr["source"]) or entity in list(diploma_abbr["target"]):
        return "Diploma"
      else:
        #search for synonym
        for i in list(df_desg_synonym["target"]) or i in list(df_desg_synonym["source"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "Designation synonym"
        for i in list(df_addr_synonym ["target"]) or i in list(df_addr_synonym ["source"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "Address synon"
        for i in list(df_branchIT_synonym ["target"]) or i in list(df_branchIT_synonym["source"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "BranchIT"
        for i in list(df_branchNonIT_synonym["target"]) or i in list(df_branchNonIT_synonym["source"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "BranchNonIT"
        for i in list(df_hardware_synonym["target"]) or i in list(df_hardware_synonym["target"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "Hardware"
        for i in list(df_duration_synonym ["target"]) or i in list(df_duration_synonym ["target"]):
          i = str(i) 
          if entity.lower() in i.lower():
            return "Duration"
        for i in list(df_experience_synonym["target"]) or i in list(df_experience_synonym["target"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "Experience"
        for i in list(df_education_synonym["target"]) or i in list(df_education_synonym["target"]): 
          i = str(i)
          if entity.lower() == i.lower():
            return "Education"
        ##search for hyponyms
        for i in list(df_desg_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "Designation"
        for i in list(df_addr_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "Address"
        for i in list(df_branchIT_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "BranchIT"
        for i in list(df_branchNonIT_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "BranchNonIT"
        for i in list(df_hardware_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "Hardware"
        for i in list(df_duration_hyponym["target"]): 
          if entity.lower() in i.lower():
            return "Duration"
        for i in list(df_experience_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "Experience"
        for i in list(df_education_hyponym["target"]): 
          if entity.lower() == i.lower():
            return "Education"
      ##search for hypernyms
      for i in list(df_desg_hypernym["target"]): 
          if entity == i:
            return "Designation"
      for i in list(df_addr_hypernym["target"]) or i in list(df_addr_hypernym["source"]): 
        if entity == i:
          return "Address"
      for i in list(df_branchIT_hypernym["target"]) or list(df_branchIT_hypernym["source"]): 
        if entity == i:
          return "BranchIT"
      for i in list(df_branchNonIT_hypernym["target"]) or i in list(df_branchNonIT_hypernym["source"]): 
        if entity == i:
          return "BranchNonIT"
      for i in list(df_hardware_hypernym["target"]) or i in list(df_hardware_hypernym["source"]): 
        if entity == i:
          return "Hardware hypernyms"
      for i in list(df_duration_hypernym["target"]): 
        if entity == i:
          return "Duration"
      for i in list(df_experience_hypernym["target"]): 
        if entity == i:
          return "Experience"
      for i in list(df_education_hypernym["target"]): 
        if entity == i:
          return "Education"
        #edit distance
        least = ""
        for i in list(desg_df["Designation"]):
          ed = edit_distance(entity,i)
          # print(i,ed)
          if(ed) < 5:
            if(min_d > ed):
              least = i
              min_d = ed
        for i in list(company_df["Company"]):
          ed = edit_distance(entity,i)
          if(ed) < 5:
            if(min_c > ed):
              least = i
              min_c = ed
        for i in list(insti_df["Institutes"]):
          ed = edit_distance(entity,i)
          if((ed) < 3):
            if(min_i > ed):
              least = i
              min_i = ed
        if(min_i < 20):
          if(min_i < min_c and min_i < min_d and entity[0] == i[0]):
            return "institutes"
          elif((min_d < min_c and min_d < min_i)and entity[0] == i[0]):
            return "designation"
          elif((min_c < min_d and min_c < min_i)and entity[0] == i[0]):
            return "Company edit"
          else:
            return None
        else:
          return None
    
company_df,desg_df,insti_df,address_df,awards_df,branchIT_df,branchNonIT_df,certificates_df,diploma_df,domain_df,duration_df,hardware_df,education_df,experience_df,functionality_df,graduate_df,desgabbr_df,instiabbr_df,compabbr_df,graduate_abbr,diploma_abbr = read_all_files()
getDataFrame()
def wsd(entity):
  res = identity_orphan(entity)
  return (entity,"is",res)
