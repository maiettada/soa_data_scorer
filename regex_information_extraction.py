# -*- coding: utf-8 -*-
"""Annotation Tool Compatto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eUvWOXEDHszpaA3OqE05SHBWz8wqxJPS
"""

from contextlib import contextmanager
import sys, os
from __future__ import print_function
import pandas as pd
import os
pd.__version__ 
 
from google.colab import drive

def read_df_limited(filepath, section):
  with suppress_stdout():
    drive.mount('/content/drive')
    dataframe = pd.read_csv(filepath, sep=',', nrows=limit)
    return dataframe[section]

def read_df(filepath, section):
  with suppress_stdout():
    drive.mount('/content/drive')
    dataframe = pd.read_csv(filepath, sep=',')
    return dataframe[section]

def write_df(filepath, df):    
  """
  This function writes data df to a file
  """
  with suppress_stdout():
    drive.mount('/content/drive')
    df.to_csv(filepath)

delimiter = '----------------------------------------------'

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import io
from contextlib import redirect_stdout

def redirection(functor):
  with io.StringIO() as buf, redirect_stdout(buf):
      print('redirected data')
      output = buf.getvalue()
  functor(output)

def fill_columns(col_text,col_retr,col_relev,col_prec,col_recall):
  """
  This function creates a Pandas DataFrame and returns it to the caller
  :param col_x: colon of data x to be filled 
  :return: DataFrame df
  """
  df= pd.DataFrame({'Text window': col_text,
                  'Retrieved instances': col_retr,
                  'Soa presenti': col_relev,
                  'Soa individuati': col_prec,
                  'Classif. individuate': col_recall})
  return df

#Here I will test the fill_columns routine
#the resulting df will be passed to the write_df for writing to file
col_text = ['OG1 blablabla', 'OG-99 bim bum bam']
col_retr = ['OG-1', '']
col_relev = ['OG-1', '']
col_prec = ['','']
col_recall = ['','']
df = fill_columns(col_text,col_retr,col_relev,col_prec,col_recall)

write_df('/content/drive/My Drive/Dataset/windowings.csv',df)
print(delimiter + color.BOLD + 'Hello World !' + color.END + delimiter)
with suppress_stdout():
  print(delimiter + color.BOLD + 'Hello World !' + color.END + delimiter)
redirection(print)

import re

#most complex regex
soa_cat_regex_iii = r'O(S|G|s|g)\n?[-\s]?\n?(\d\d?\w?).*'
soa_cat_regex_iii = r'(IV\s?\-?bis|IV|III\s?\-?bis|III|II|IX|VIII|VII|VI|X|V|I)[^\w]'

#medium-complexity regex
soa_cat_regex_ii = r'O(S|G|s|g)(\d\d?\w?).*'
ordinals_regex_ii = r'(IV|IV|III|II|IX|VIII|VII|VI|X|V|I)[^\w]'

#basic regex
soa_cat_regex_i = r'O(S|G)(\d\d?).*'
ordinals_regex_i = r'(IV|IV|III|II|IX|VIII|VII|VI|X|V|I)[^\w]'

soa_cat_regex_version = soa_cat_regex_i
ordinals_regex_version = ordinals_regex_i


def message(a1,a2):
  print(a1,'[',a2,']')

def filtered(argument):
    """
    Here a filtering of strings is provided.
    The following switcher will output the name of the SOA category if right,
    otherwise it will ouput "Invalid"
    :param argument: string that is supposed to be a SOA category
    :return: verified SOA string, or Invalid
    """
    message("start filtering : ", argument)
    switcher = {      
      'OG-1' :  lambda:   'OG-1',      'OG-2' :  lambda:   'OG-2',
      'OG-3' :  lambda:   'OG-3',      'OG-4' :  lambda:   'OG-4',
      'OG-5' :  lambda:   'OG-5',      'OG-6' :  lambda:   'OG-6',
      'OG-7' :  lambda:   'OG-7',      'OG-8' :  lambda:   'OG-8',
      'OG-9' :  lambda:   'OG-9',      'OG-10' :  lambda:   'OG-10',
      'OG-11' :  lambda:   'OG-11',      'OG-12' :  lambda:   'OG-12',
      'OG-13' :  lambda:   'OG-13',      'OS-1' :  lambda:   'OS-1',
      'OS-2' :  lambda:   'OS-2A', 
      'OS-2A' :  lambda:   'OS-2A',      'OS-2B' :  lambda:   'OS-2B',
      'OS-3' :  lambda:   'OS-3',      'OS-4' :  lambda:   'OS-4',
      'OS-5' :  lambda:   'OS-5',      'OS-6' :  lambda:   'OS-6',
      'OS-7' :  lambda:   'OS-7',      'OS-8' :  lambda:   'OS-8',
      'OS-9' :  lambda:   'OS-9',      'OS-10' :  lambda:   'OS-10',
      'OS-11' :  lambda:   'OS-11',
      'OS-12' :  lambda:   'OS-12A',      'OS-12A' :  lambda:   'OS-12A',
      'OS-12B' :  lambda:   'OS-12B',      'OS-13' :  lambda:   'OS-13',
      'OS-14' :  lambda:   'OS-14',      'OS-15' :  lambda:   'OS-15',
      'OS-16' :  lambda:   'OS-16',      'OS-17' :  lambda:   'OS-17',
      'OS-18' :  lambda:   'OS-18A',
      'OS-18A' :  lambda:   'OS-18A',      'OS-18B' :  lambda:   'OS-18B',
      'OS-19' :  lambda:   'OS-19',
      'OS-20' :  lambda:   'OS-20A',      'OS-20A' :  lambda:   'OS-20A',
      'OS-20B' :  lambda:   'OS-20B',      'OS-21' :  lambda:   'OS-21',
      'OS-22' :  lambda:   'OS-22',      'OS-23' :  lambda:   'OS-23',
      'OS-24' :  lambda:   'OS-24',      'OS-25' :  lambda:   'OS-25',
      'OS-26' :  lambda:   'OS-26',      'OS-27' :  lambda:   'OS-27',
      'OS-28' :  lambda:   'OS-28',      'OS-29' :  lambda:   'OS-29',
      'OS-30' :  lambda:   'OS-30',      'OS-31' :  lambda:   'OS-31',
      'OS-32' :  lambda:   'OS-32',      'OS-33' :  lambda:   'OS-33',
      'OS-34' :  lambda:   'OS-34',      'OS-35' :  lambda:   'OS-35'
    }
    func = switcher.get(
        argument, lambda: 'Invalid' #invalid category
        )
    return func()

def normalised_category(stringa):
  """
  Normalisation of category string ( not verifying if the string 
  really belongs to the SOA dictionary)
  :param stringa: example "OS. 87a"
  :return: example OS-87A
  """
  message("start normalised_category : ", stringa)
  a = re.sub(r'O(S|G|s|g)\n?[-\s]?\n?(\d\d?\w?).*',r'O\1-\2', stringa)
  message("substituted with ", a)
  return a.upper()

def classif(stringa):
  """
  Extraction of classifications out of string
  :param stringa: ex. "OS-123 classifica IV.BIS"
  :return: ex"IV-bis"
  """
  message("start classif ", stringa)
  stringa = re.sub(r'(BIS|Bis)',r'bis',stringa)
  roman_regex = re.compile(ordinals_regex_version)
  match = roman_regex.search(stringa, pos=0)
  if match:
    start = match.start() 
    end = match.end()
    to_be_returned= stringa[start:end]
  else:
    to_be_returned='?'
    start = 0
    end = 0
  message("      classif before sostitution with :", to_be_returned)
  substitutd = re.sub(r'(IV\s?\-?bis|IV|III\s?\-?bis|III|II|IX|VIII|VII|VI|X|V|I).*',r'\1', to_be_returned)
  message("      classif after sostitution :", substitutd)
  #, flags=re.DEBUG+re.VERBOSE)
  return substitutd, start, end

def filtered_cl(argument):  
  """
  Dictionary filtering
  """
  message("start filtered_cl", argument)
  switcher = {      
      'I' :  lambda:   'I',
      'II' :  lambda:   'II',
      'III' :  lambda:   'III',
      'III bis' :  lambda:   'III-bis',
      'IIIbis' :  lambda:   'III-bis',
      'III-bis' :  lambda:   'III-bis',
      'IV' :  lambda:   'IV',
      'IV bis' :  lambda:   'IV-bis',
      'IVbis' :  lambda:   'IV-bis',
      'IV-bis' :  lambda:   'IV-bis',
      'V' :  lambda:   'V',
      'VI' :  lambda:   'VI',
      'VII' :  lambda:   'VII',
      'VIII' :  lambda:   'VIII'
  }
  func = switcher.get(
        argument, lambda: '?'
      )
  return func()

def test_once():
  """
  Bunch of calls to check the filtering-dictionary functionalities
  """
#with suppress_stdout():
  #TESTING 1)THE NORMALISATION
  print("standardisation trials")
  param = 'OG. 1     ncdsncjkdcnkjsdc'
  print(param, '-->', normalised_category(param))
  print(param, '-->', normalised_category(param))
  param = 'OG11  dcnsjLNCJDSLnc cdnancd'
  print(param, '-->', normalised_category(param))
  print(param, '-->', normalised_category(param))
  param = 'OG 99A     ncdsncjkdcnkjsdc'
  print(param, '-->', normalised_category(param))
  print(param, '-->', normalised_category(param))
  print("-------------------------------")

  #TESTING DICTIONARY FILTERING
  print("dictionary filtering:")

  param = 'OG 1 with noise symbols bla Classifica III-Bis.'
  print(param,'-->', filtered(normalised_category(param)))
  classifica, inizio, fine = classif(param)
  print('-------->', filtered_cl(classifica))
  print()

  param = 'OG2 with noise symbols 7+07+c class. VII  c+09+'
  print(param,'-->', filtered(normalised_category(param)))
  classifica, inizio, fine = classif(param)
  print('-------->', filtered_cl(classifica))
  print()


  param = 'OG-18A with noise symbols 7+07+ cl.II cc+09+'
  print(param,'-->', filtered(normalised_category(param)))
  classifica, inizio, fine = classif(param)
  print('-------->', filtered_cl(classifica))
  print()


  param = 'OG-3 with noise symbols 7+07+ cl.IV bis cc+09+'
  print(param,'-->', filtered(normalised_category(param)))
  classifica, inizio, fine = classif(param)
  print('-------->', filtered_cl(classifica))
  print()


  param = 'OG-3 with noise symbols 7+07+ cl.IV cc+09+'
  print(param,'-->', filtered(normalised_category(param)))
  classifica, inizio, fine = classif(param)
  print('-------->', filtered_cl(classifica))
  print()



  param = 'meaningless info'
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()

  param = 'OS-99 (inexistent)'
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()


  param= 'OG-1 ” Edifici civili ed industriali”; Classifica VI o superiore; \n3.4.'
  print(normalised_category(param))
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()


  param='OS21 nella classe I '
  print(normalised_category(param))
  print(classif(param))
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()

  param='OS21 Importo '
  print(normalised_category(param))
  print(classif(param))
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()

  param='OG 11 di cui'
  print(normalised_category(param))
  print(classif(param))
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()

  param='e della OS21 nella classe I'
  print(normalised_category(param))
  print(classif(param))
  print(param,'-->', filtered(normalised_category(param)))
  print('-------->', filtered_cl(classif(param)[0]))
  print()

test_once()

# Commented out IPython magic to ensure Python compatibility.
# structured output
## capture some variations of the OS/OG mentioned
### apply this on the given online csv (by incremental number of results)
import json
import re
limit=1000
col_text = []
col_retr = []
col_relev = []
col_prec = []
col_recall = []

# soa_cat_regex = r'O(S|G|s|g)\n?[-\s]?\n?(\d\d?\w?)'
#soa_cat_regex = r'O(S|G|s|g)\n?[-\s]?\n?(\d\d?\w?).*'
from_os_to_period = r'O(S|G|s|g)([^\.]+\d+\.\d+[^\.]*\.|cl\.[^\.]+\.|[^\.]+\.)'
from_os_n_char = r'O(S|G|s|g).{1,100}'

def fill_col(text,retrieved,relevant,precision,recall):
  global col_text,col_retr,col_relev,col_prec,col_recall
  col_text = col_text.append(text)
  col_retr.append(retrieved)
  col_relev.append(relevant)
  col_prec.append(precision)
  col_recall.append(recall)

def set_col(col):
  col_text = col

def retrieve_col():
  global col_text
  return col_text

def find_matches_positions(mia_stringa, chosen_regex):
  """
  :return: mia_lista, list made of (start_offset, end_offset) elements
  """
  compiled_regex = re.compile(chosen_regex) 
  a = compiled_regex.search( mia_stringa, pos=0 )
  mia_lista=[]
  i = 0
  while a and i<limit :
    mia_lista.append((a.start(),a.end()))
    a = compiled_regex.search( mia_stringa, pos=a.end())
    i=i+1
  return mia_lista

def matches_list_print(matches_string, matches_list):
    for match in matches_list:
      print(match)
      begin_char = match[0]
      end_char = match[1]
      #input()
      print(matches_string[begin_char:end_char])
      #print(strings_to_num(matches_string[begin_char:end_char]))

def extract_soa_cat_class(mia_stringa,start_offset=0, end_offset=0):
  """
  Extraction of soa categories and classes
  """
  soa_pos_list = find_matches_positions(mia_stringa, soa_cat_regex_version) # per ogni el della lista, ritornare enum e posizioni relative
  matches_list_print(mia_stringa, soa_pos_list)
  categories_list = []
  for  i in range(len(soa_pos_list)):
      begin_char = soa_pos_list[i][0]
      end_char = soa_pos_list[i][1]
      ## solvo bug  : begin_char_next_match = -1
      begin_char_next_match = None
      if i+1<len(soa_pos_list):
        begin_char_next_match = soa_pos_list[i+1][0]
      output_cat = filtered(normalised_category(mia_stringa[begin_char:end_char]))
      if output_cat != 'Invalid':
        print("processing", mia_stringa[begin_char:begin_char_next_match], "lenght: ", len(mia_stringa[begin_char:begin_char_next_match]))
        string_classif, inizio_classif, fine_classif  = classif(mia_stringa[begin_char:begin_char_next_match])
        output_cl = filtered_cl(string_classif)
        print("added:", output_cat, output_cl)
        categories_list.append([start_offset+begin_char, start_offset+end_char, 
                                #'-'.join([output_cat,output_cl])])
                                output_cat])
        if output_cl != '?':
          categories_list.append([start_offset+begin_char,
                                start_offset+begin_char+fine_classif,
                                output_cl])
  return categories_list

def extract_soa_data(text_index, csv_print=False):
    """
    Reads docs from soa.csv
    Finds a list of (possible) soa-strings by using find_matches_positions
    Inspects those possible soa-strings with extract_soa_cat_class
    Depending on csv_print, can output to file
    :param text_index: index of the text to be inspected
    :param csv_print: boolean requirement true/false for csv output
    :return: complete dataframe df, document, col_texts with text windows,
    col_retr with data findigs for each window
    """
    global col_text,col_retr,col_relev,col_prec,col_recall
    col_text = []
    col_retr = []
    col_relev = []
    col_prec = []
    col_recall = []
    #with suppress_stdout():
    testi = read_df('/content/drive/My Drive/Dataset/soa.csv', 'testo')
    document = testi[text_index]
    #document = re.sub(r'\_',r' ', document)
    chosen_regex = from_os_n_char 
    #from_os_to_period
    liste_di_matches = find_matches_positions(document , chosen_regex)
    lista_di_soa = []
    colmn = []
    for match in liste_di_matches:
      begin_char = match[0]
      end_char = match[1]
      print(color.BOLD)
      print('%s\n%d) Window of selection: from position %d to %d\n' 
#             % (delimiter, liste_di_matches.index(match), begin_char, end_char))
      print('- - -\n%s\n- - - \noutcome:' % (document[begin_char:end_char]))
      extracted = extract_soa_cat_class(document[begin_char:end_char], 
                                        start_offset=begin_char, 
                                        end_offset=end_char)
      print(extracted)
      lista_di_soa.extend(extracted)
      print(color.END)
      col_text.append(document[begin_char:end_char])
      col_retr.append(extracted)
      col_relev.append('')
      col_prec.append('')
      col_recall.append('')
      print(' %s ' % (delimiter))
    print(lista_di_soa)
    df = fill_columns(col_text,col_retr,col_relev,col_prec,col_recall)
    if csv_print:
      write_df('/content/drive/My Drive/Dataset/windowings.csv',df)
      #print("written to file windowings.csv")
      #print(col_text,col_retr,col_relev,col_prec,col_recall)
    return df, document, col_text, col_retr

def retrieve_data():
  retrieved_list = read_df('/content/drive/My Drive/Dataset/windowings.csv',
                           'Retrieved instances')
  return retrieved_list

def local_and_csv_printing(text_index):
 retrieved_list = retrieve_data()
 #print(retrieved_list)
 df, text, windows, retrievals = extract_soa_data(text_index)
 df
 return df, text, windows, retrievals

def retrieve_postprocessed_data():
  """
  Creating a string out of a string list
  Input example: "[a,b]","[()]"
  Output:        "[a,b],[()]"
  """
  retrieved_list = read_df('/content/drive/My Drive/Dataset/windowings.csv',
                           'Retrieved instances')
  return ','.join(retrieved_list)


def exclude_empty_sublist(mylist):
  print(mylist)
  return [l for l in mylist if l!=[]]

def json_with_postprocessed_data(retr):
  """
  data would be: [[[14306, 14372, 'OS-7-?']], [[14620, 14680, 'OS-7-?']]]
  but for json format we need to cut a bracket level, e.g.
  [[14306, 14372, 'OS-7-?'], [14620, 14680, 'OS-7-?']]
  """
  postprocessed_data = str(retr)
  substituted_enclosure = re.sub(r']\s?]',r']',postprocessed_data)
  substituted_init = re.sub(r'\[\s?\[',r'[',substituted_enclosure)
  dumpd = (json.dumps({"labels":  substituted_init }))  
  no_quotes = re.sub(r'\"',r'',dumpd)
  no_quotes = re.sub(r'\'',r'"',no_quotes)
  label_quotes = re.sub(r'labels',r'"labels"',no_quotes)
  #label_quotes is the string with the proper list format
  json_obj = json.loads(label_quotes)
  return json_obj['labels']


def dumps_jsonl(text, retr, array_index):
  """
  Puts data together to get a complete jsonl output data,
  with lines like the following format:
    {"text": "President Obama", "labels": [ [10, 15, "PERSON"] ]}
  """
  with suppress_stdout():
    empty_excluded = exclude_empty_sublist(retr)
  return json.dumps({"text": text, "meta": {"ord_id": array_index, "fr_id": 0}, 
                     "labels": json_with_postprocessed_data(empty_excluded)})

def dumps_labels_only(retr, array_index):
  with suppress_stdout():
    empty_excluded = exclude_empty_sublist(retr)
  return json.dumps({"meta": {"ord_id": array_index, "fr_id": 0}, 
                     "labels": json_with_postprocessed_data(empty_excluded)})

def dumps_data_frame(df):
  return df


from time import sleep

def single_doc_dump():
  """
  Single-doc extraction
  """
  notepad_index = 2
  array_index = notepad_index-1
  with suppress_stdout():
   df, text, windows, retr = extract_soa_data(array_index)
  print(dumps_jsonl(text, retr, array_index))

def interval_doc_dump():
  """
  Executing the regex soa-extraction on an interval of docs.
  """
  json_outputs = []
  start_index = 0
  end_index = 100
  for indice in range(start_index, end_index):
    with suppress_stdout():
      df, text, windows, retr = extract_soa_data(indice)
    #print(dumps_jsonl(text, retr, indice))
    print(dumps_labels_only(retr, indice))
    sleep(0.20)

#Calling the extraction and printing out the results.
#dumps_data_frame(retr)
interval_doc_dump()

"""
Helper procedures to print documents to console
"""

def printdoc(her):
 with suppress_stdout():
  testi = read_df('/content/drive/My Drive/Dataset/soa.csv', 'testo')
 print(testi[her])

#printdoc(0)

with suppress_stdout():
 testi = read_df('/content/drive/My Drive/Dataset/soa.csv', 'testo')
testi[99]
