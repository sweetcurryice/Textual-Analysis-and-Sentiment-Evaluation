import os
import shutil
import pyphen
import re
import nltk
import chardet
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import pandas as pd
import subprocess
from textblob import TextBlob
nltk.download('punkt')


crawler_dir = os.path.join("Web_Crawler", "crawler_main.py")
subprocess.run(["python", crawler_dir])

df = pd.read_excel("Data Preprocessing\Input Data\Input.xlsx")

cleaned_articles_directory = os.path.join("Data Preprocessing", "Output Data", "Cleaned articles")
default_articles_directory = os.path.join("Data Preprocessing", "Output Data", "Extracted articles")


################################################################################
# STOPWORDS FILE MERGER ########################################################
################################################################################

def remove_directory(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)

input_directory = os.path.join("Data Preprocessing","Input Data", "StopWords")
folder_path = os.path.join(input_directory,"concatination")
output_directory = os.path.join(folder_path, "final_stop_words.txt")

remove_directory(folder_path)

# Initialize an empty string to store the concatenated text
concatenated_text = ''

# Iterate through text files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_directory, filename)
        
        # Read the content of each text file and append it to the concatenated_text
        with open(file_path, 'r') as file:
            file_text = file.read()
            concatenated_text += file_text

# Write the concatenated text to the output file
with open(output_directory, 'w') as output:
    output.write(concatenated_text)
    
print("Concatination of all the Stop-Word files completed.")

################################################################################
################################################################################
################################################################################
 




################################################################################
# STOP WORDS AND PUNCTUATION REMOVER FOR EXTRACTED ARTICLES ####################
################################################################################

def charset_detect(stop_words_file):
    with open(stop_words_file, 'rb') as file:
        result = chardet.detect(file.read())  # This is to Detect the encoding as the stop word files were not loading until the encoding was specified
    return result['encoding']


def read_stop_words(stop_words_file):
    
    with open(stop_words_file, 'r', encoding=charset_detect(stop_words_file)) as file:
        stop_words = set(file.read().split())
    return stop_words
    

# Function to remove stop words from a list of words
def remove_stop_words(text, stop_words):
    #new_words = "".join([word for word in text if word in string.punctuation])
    new_words = re.sub(r'[^a-zA-Z0-9+-]', ' ', text)
    words = new_words.split()
    cleaned_words = [word.lower() for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

remove_directory(cleaned_articles_directory)

# Contains the all the stop words from the multiple stop words files
stop_words_file = os.path.join("Data Preprocessing","Input Data", "StopWords","concatination","final_stop_words.txt")

stop_words = read_stop_words(stop_words_file)

# To Iterate through text files in the input directory
for filename in os.listdir(default_articles_directory):
    if filename.endswith('.txt'):
        input_path = os.path.join(default_articles_directory, filename)
        output_path = os.path.join(cleaned_articles_directory, filename)
        
        # Read the content of the text file
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Remove stop words from the content
        cleaned_text = remove_stop_words(text, stop_words)
        
        # Writing the cleaned data into a text file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

print("Stop words removed from all text files.")

################################################################################
################################################################################
################################################################################




################################################################################
# REMOVE STOPWORDS FROM POSITIVE AND NEGATIVE FILES ############################
################################################################################

    

# Function to remove stop words from a list of words
def remove_stop_words2(text, stop_words):
    #new_words = "".join([word for word in text if word in string.punctuation])
    new_words = re.sub(r'[^a-zA-Z0-9+-]', ' ', text)
    words = new_words.split()
    cleaned_words = [word.lower() for word in words if word not in stop_words]
    return '\n'.join(cleaned_words)

# Directory containing text files
input_directory2 = os.path.join("Positive Negative Words")
output_directory2 = os.path.join("Positive Negative Words", "StopWords Removed")

remove_directory(output_directory2)



# Iterate through text files in the input directory
for filename in os.listdir(input_directory2):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_directory2, filename)
        output_path = os.path.join(output_directory2, filename)
        
        # Read the content of the text file
        with open(input_path, 'r', encoding=charset_detect(input_path)) as file:
            text = file.read()
        
        # Remove stop words from the content
        cleaned_text = remove_stop_words2(text, stop_words)
        
        # Write the cleaned content back to the text file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

print("Stop words removed from the positive and negative words file files.")






################################################################################
# SENTIMENTAL ANALYSIS #########################################################
################################################################################

# function to read file using directory
def read_file(file_directory, filename):
    input_path = os.path.join(file_directory, filename)
    # Read the content of the text file
    with open(input_path, 'r', encoding='utf-8') as file:
        words = file.read()
    
    return words

positive_negative_dict = os.path.join("Positive Negative words", "StopWords Removed")
positive_dict = nltk.tokenize.word_tokenize(read_file(positive_negative_dict, "positive-words.txt"))
negative_dict = nltk.tokenize.word_tokenize(read_file(positive_negative_dict, "negative-words.txt"))

for filename in os.listdir(cleaned_articles_directory):
    
    if filename.endswith('.txt'):
        
        words = read_file(cleaned_articles_directory, filename)
            
        tokenized_text = word_tokenize(words)
        
######################## Positive and Negative Score #######################
            
        positive_score = sum(1 if word in positive_dict else 0 for word in tokenized_text)
        negative_score = sum(-1 if word in negative_dict else 0 for word in tokenized_text)*-1
        
        
###################### Polarity Score #######################################

        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        
        
####################### subjectivity Score ##################################
       
        blob = TextBlob(words)

        subjectivity_score = blob.sentiment.subjectivity 
        
######### Loading the various sentimental scores into the dataframe ##########
        
        target_url_id = filename.replace(".txt", "")        
        matching_rows = df['URL_ID'].astype(str) == target_url_id
        df.loc[matching_rows, 'POSITIVE SCORE'] = positive_score  # Pawsitive Score
        df.loc[matching_rows, 'NEGATIVE SCORE'] = negative_score  # Negative score
        df.loc[matching_rows, 'POLARITY SCORE'] = round(polarity_score, 3)  # polarity score
        df.loc[matching_rows, 'SUBJECTIVITY SCORE'] = round(subjectivity_score, 3)  # subjectivity score using text blob


################################################################################
################################################################################



    
################################################################################
# Analysis of Readability ######################################################
################################################################################

for filename in os.listdir(default_articles_directory):
    if filename.endswith('.txt'):
        text = read_file(default_articles_directory, filename)
        cleaned_text = read_file(cleaned_articles_directory, filename)
        words = word_tokenize(text)
        cleaned_words = word_tokenize(cleaned_text)
        sentences = sent_tokenize(text)
        
        
################### Average Sentence Length ####################################

        average_sentence_length = len(words)/len(sentences) 
        
            
#################### Complex word count and The Percentage######################

        def count_syllables(word, dicts):
            hyphenated = dicts.inserted(word)
            return hyphenated.count('-') + 1

        dicts = pyphen.Pyphen(lang='en')

        # ckecking if the word has more than 2 syllabus and storing it into complex words
        complex_words = [word for word in words if count_syllables(word, dicts) > 2]
        
        percentage_complex_words = (len(complex_words)/len(words))*100
        
######################### Fog Index ########################################### 

        fog_index = (average_sentence_length + percentage_complex_words)*0.4 
        # using the gunning fog method
        
################## Syllable per Word ###########################################

        syllable_count = int()
        syllable_words = []
        for word in words :      
            if word.endswith('es'):
                word = word[:-2]
            elif word.endswith('ed'):
                word = word[:-2]
            vowels = 'aeiou'
            syllable_count_word = sum( 1 for letter in word if letter.lower() in vowels)
            if syllable_count_word >= 1:
                syllable_count += syllable_count_word
                syllable_words.append(word)
                
                syllable_avg_per_word = syllable_count / len(syllable_words)
       
      
 
####################### Personal Pronouns ######################################

        pronouns_pattern = r'\b(I|we|my|ours|us)\b'   #regex for the the pronouns     
        personal_pronouns = re.findall(pronouns_pattern, text, re.IGNORECASE)
        personal_pronouns = [pronoun for pronoun in personal_pronouns if pronoun!= "US"] # 'US' removed so that it won't cause trouble while counting the pronouns
        

################# Average word length ##########################################
        average_word_length = len(text)/len(words)
        
        
        target_url_id = filename.replace(".txt", "")        
        matching_rows = df['URL_ID'].astype(str) == target_url_id
        
        
    
######### saving the output values into thier respective columns ############
        
        df.loc[matching_rows, 'AVG SENTENCE LENGTH'] = average_sentence_length
        
        df.loc[matching_rows, 'PERCENTAGE OF COMPLEX WORDS'] = round(percentage_complex_words, 0)
        
        df.loc[matching_rows, 'FOG INDEX'] = round(fog_index, 0)
        
        df.loc[matching_rows, 'AVG NUMBER OF WORDS PER SENTENCE'] = round(average_sentence_length, 0)
        
        df.loc[matching_rows, 'COMPLEX WORD COUNT'] = len(complex_words)
        
        df.loc[matching_rows, 'WORD COUNT'] = len(cleaned_words)
        
        df.loc[matching_rows, 'SYLLABLE PER WORD'] = round(syllable_avg_per_word, 4)
        
        df.loc[matching_rows, 'PERSONAL PRONOUNS'] = len(personal_pronouns)
        
        df.loc[matching_rows, 'AVG WORD LENGTH'] = round(average_word_length, 0)
        
        
        
        
        

df.drop([4, 24, 37], axis = 0, inplace = True) # removed the duplicate and dead links

output_excel_file = 'output.xlsx' 

if os.path.exists(output_excel_file):
    os.remove(output_excel_file)
    
df.to_excel(output_excel_file, index=False)
print("The excel output file was successfully generated with all the correct values in its place")

          