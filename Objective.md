# <ins> Project Objective</ins>

## Table of Contents:
1. [Objective](#1-objective)
2. [Data Extraction](#2-data-extraction)
3. [Textual Analysis](#3-textual-analysis)
   1. [Sentimental Analysis](#31-sentimental-analysis)
      1. [Cleaning using Stop Words Lists](#311-cleaning-using-stop-words-lists)
      2. [Creating dictionary of Positive and Negative words](#312-creating-dictionary-of-positive-and-negative-words)
      3. [Extracting Derived variables](#313-extracting-derived-variables)
   2. [Analysis of Readability](#32-analysis-of-readability)
   3. [Average Number of Words Per Sentence](#33-average-number-of-words-per-sentence)
   4. [Complex Word Count](#34-complex-word-count)
   5. [Word Count](#35-word-count)
   6. [Syllable Count Per Word](#36-syllable-count-per-word)
   7. [Personal Pronouns](#37-personal-pronouns)
   8. [Average Word Length](#38-average-word-length)

## 1. Objective
The objective of this assignment is to extract textual data articles from the given URLs and perform text analysis to compute variables explained below.

-------------------------
## 2. Data Extraction
- Extract text data from each website listed in the "Urls" column of the "input.xlsx" file.
- Save the extracted text as individual text files.
- Use the corresponding "url id" as the filename for each text file ([url id].txt).
- Extract only the article title and text, excluding headers, footers, or other non-article content.

-------------------------

## 3. Textual Analysis
For each text file, conduct textual analysis to compute various variables, such as sentiment scores, readability metrics, and linguistic features. Save the output in a copy of the input.xlsx file, placing the results in the same row as their corresponding URL IDs to facilitate easy reference and analysis.

These are the following variables and metrics to be computed:-

### 3.1 Sentimental Analysis
Sentimental analysis determines whether a piece of writing is positive, negative, or neutral. The algorithm designed for financial texts includes the following steps:

#### 3.1.1 Cleaning using Stop Words Lists
Use Stop Words Lists to clean the text, excluding words found in the list.

#### 3.1.2 Creating a dictionary of Positive and Negative words
Use the positive and negative files to create a dictionary of Positive and Negative words, excluding those in the Stop Words Lists.

#### 3.1.3 Extracting Derived variables
Convert the text into tokens using the NLTK tokenize module to calculate the following variables:
- Positive Score: Sum of +1 for each word in the Positive Dictionary.
- Negative Score: Sum of -1 for each word in the Negative Dictionary (multiplied by -1 for positive score).
- Polarity Score: (Positive Score – Negative Score) / (Positive Score + Negative Score + 0.000001) (range from -1 to +1).
- Subjectivity Score: Use the package textblob .

### 3.2 Analysis of Readability
Calculate readability using the Gunning Fox index formula:

- Average Sentence Length: Number of words / number of sentences.
- Percentage of Complex words: Number of complex words / number of words.
- Fog Index: 0.4 * (Average Sentence Length + Percentage of Complex words).

### 3.3 Average Number of Words Per Sentence
Calculate: Average Number of Words Per Sentence = Total number of words / Total number of sentences.

### 3.4 Complex Word Count
Count complex words (words with more than two syllables).

### 3.5 Word Count
Count total cleaned words in the text by removing stop words and punctuations.

### 3.6 Syllable Count Per Word
Count syllables in each word, handling exceptions.

### 3.7 Personal Pronouns
Calculate counts of personal pronouns ("I," "we," "my," "ours," and "us"), excluding the country name "US."

### 3.8 Average Word Length
Calculate: Sum of total number of characters in each word / Total number of words.

------------------------------------------------