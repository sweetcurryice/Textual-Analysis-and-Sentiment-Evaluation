# Textual Analysis and Sentiment Evaluation of Multiple Articles : A Data Science/ NLP project


Introducing the project 'Textual Analysis and Sentiment Evaluation of Multiple Articles.' This endeavor involves the extraction and normalization of diverse articles, culminating in a thorough analysis of polarity score, subjectivity score, and other 11 key metrics. The enriched dataset provides a comprehensive understanding of the textual landscape within the realm of multiple articles.

## Project Structure



📦Data Science Project
┣ 📦Data Preprocessing
┃ ┣ 📂Input Data
┃ ┃ ┣ 📂StopWords <span style="color: purple;">--------------------------------------------## The Stop words File ##</span>
┃ ┃ ┃ ┣ 📂concatination
┃ ┃ ┃ ┃ ┗ 📜final_stop_words.txt
┃ ┃ ┃ ┣ 📜StopWords_Auditor.txt
┃ ┃ ┃ ┣ 📜StopWords_Currencies.txt
┃ ┃ ┃ ┣ 📜StopWords_DatesandNumbers.txt
┃ ┃ ┃ ┣ 📜StopWords_Generic.txt
┃ ┃ ┃ ┣ 📜StopWords_GenericLong.txt
┃ ┃ ┃ ┣ 📜StopWords_Geographic.txt
┃ ┃ ┃ ┗ 📜StopWords_Names.txt
┃ ┃ ┗ 📜Input.xlsx <span style="color: purple;">----------------------------------------------## The Input File ##</span>
┃ ┗ 📂Output Data
┃ ┃ ┣ 📂Extracted articles <span style="color: purple;">-----------------------------------## Extracted Articles ##</span>
┃ ┃ ┣ 📂Cleaned articles
┃ ┃ ┗ 📂Tokenized articles
┣ 📦Positive Negative Words
┃  ┣ 📂StopWords Removed
┃  ┃ ┣ 📜negative-words.txt
┃  ┃ ┗ 📜positive-words.txt
┃  ┣ 📜negative-words.txt
┃  ┗ 📜positive-words.txt
┣ 📦Web_Crawler
┃  ┣ 📂Web_Crawler
┃  ┣ 📜crawler_main.py <span style="color: purple;">-----------------------------------------## The Web Crawler File ##</span>
┣ 📜data_analysis.py
┣ 📜requirements.txt
┣ 📜output.xlsx <span style="color: purple;">-----------------------------------------------------## The Output File ##</span>
┣ 📜Objective_.md <span style="color: purple;">-----------------------------------------------------## The Objective File ##</span>
┗ 📜READ_ME.md
 
 

<br><br>
- **Web_Crawler**: This directory contains the Python script `crawler_main.py`, which is responsible for extracting data from the given URL. It uses the Scrapy library for web crawling.

- **Data_Preprocessing**: This directory contains the `input.xlsx` file, which contains a list of articles with associated URLs. The extracted articles will be saved in the `Output_Data/extracted_articles` directory.

- **data_analysis.py**: This Python script is used for text analysis on the extracted articles and computes various variables as described in the project requirements.

- **Text Analysis.docx**: This document provides definitions and details about the variables to be computed during text analysis.

---------------

## Instructions to Run the Project

 **IMPORTANT -** 
 * Run the data_analysis.py file, as it does the entire job, from data extraction to cleaning, and then analysis, finally generating the output, But to review the entire process and to understand the code, you may follow the given instructions.


1. **Data Extraction**:

   - Navigate to the `Web_Crawler` directory.
   - You can review my code in `crawler_main.py` by opening it in a code editor.
   - I've made it easy to specify the URL(s) from which to extract articles within the script.
   - By running `crawler_main.py`, the script extracts article text. I ensured that only the article title and content were extracted, excluding headers, footers, or any other irrelevant information.
   - You'll find the extracted articles saved in the `Data_Preprocessing/Output_Data/extracted_articles` directory with filenames corresponding to their URL IDs.

2. **Data Analysis**:

   - If you navigate back to the project's main directory, you can explore my code in `data_analysis.py` by opening it in a code editor.
   - I implemented the text analysis as per the requirements outlined in `Text Analysis.docx`. I used Python for the data analysis.
   - I've saved the computed variables in the same order as specified in `Output Data Structure.xlsx`.

3. **Output Generation**:

   - The generated output excel file is save in the parent directory under the name of `output.xlsx`.


I hope this documentation helps you evaluate my work effectively. If you have any questions or need clarifications, please don't hesitate to reach out to me. Thank you for considering my submission!

---------------------------

## Possible Applications and Implications of Text Analysis Results

- The outputs of this project, which include sentiment analysis, readability metrics, and linguistic feature extraction, can have several practical applications across different domains, these are some potential uses of the project outputs:


1. **News Monitoring**:

    - Media monitoring tools can prioritize and categorize news articles based on their sentiment for quicker analysis.

2. **Content Tailoring for Different Audiences**:

    - Readability metrics can help financial analysts and communicators tailor their reports and documents for specific audiences.

3. **Risk Assessment**:

	- Linguistic feature extraction, such as personal pronoun analysis, can offer additional insights into the communication style and potential biases.

4. **Customer Feedback Analysis**:

	- Organizations can use sentiment analysis to understand customer sentiments expressed in feedback, reviews, or social media, helping them improve overall customer satisfaction.


5. **Education and Training**:

	- Readability metrics can be utilized in educational materials to ensure that financial concepts are presented in a comprehensible manner.
	- Linguistic features can be analyzed to identify areas for improvement in written communication skills.

6. **Market Research**:

	- Sentiment analysis can aid in understanding customer opinions and market trends, contributing to more effective market research.

In summary, the outputs of this project can be valuable in decision-making, communication improvement, risk assessment, compliance, and various other applications within the financial domain and beyond. The versatility of sentiment analysis and linguistic feature extraction makes these outputs applicable to a wide range of contexts where understanding and leveraging textual information is crucial.

--------------
## Acknowledgments

The data utilized in this project, including but not limited to the primary CSV with Urls, stop words, and positive and negative word lists, was graciously sourced from [BlackOffer](https://blackcoffer.com/). I extend my sincere gratitude to BlackOffer for providing access to these valuable resources, which significantly contributed to the comprehensive analysis and findings presented in this report. This collaboration has been instrumental in enriching the depth and breadth of insights derived from the project.



------------------



## Contact Information

Feel free to reach out to me via [Email](mailto:shivamsaikiran111@gmail.com) or on [LinkedIn](https://www.linkedin.com/in/shivam-sai-kiran-030745210/).

----------------------------



© 2023 Shivam Sai Kiran. This project is licensed under the [MIT License](License.txt).