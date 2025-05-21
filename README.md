# **Chat Insights — AI Conversation Analyzer**

## **Project Overview**  
Chat Insights is a Python tool built to analyze chat logs between a user and an AI assistant. It reads `.txt` files of conversations, processes the content, and generates detailed summaries including message counts and key topic highlights. By leveraging natural language processing (NLP) techniques, it extracts meaningful keywords and tracks the flow of dialogue to deliver clear, informative insights.

---

## **Key Features**  
- **Conversation Parsing:** Efficiently separates messages by speaker (User vs AI) from `.txt` logs.  
- **Message Metrics:** Counts total messages, as well as breakdowns by User and AI.  
- **Keyword Extraction:** Identifies top 5 keywords excluding common stopwords and filler words.  
- **Summarization:** Produces a readable summary with total exchanges, main topics discussed, and frequent keywords.  
- **Batch Processing:** Supports analyzing multiple chat files in a folder for consolidated reports.  
- **Interactive UI:** Built with Streamlit for an easy-to-use web interface showcasing results dynamically.

---

## **How It Works**  

### 1. **Parsing Chat Logs**  
Reads each chat `.txt` file line by line, categorizing text into separate User and AI message lists to maintain context.

### 2. **Cleaning Text Data**  
Extracts only alphabetic words, converts to lowercase, and removes common stopwords (e.g., “the”, “is”) and conversational fillers (e.g., “hi”, “thanks”).

### 3. **Extracting Keywords**  
Uses frequency analysis to determine the top 5 most meaningful keywords that best represent the conversation topics.

### 4. **Generating Summary**  
Combines message counts and keywords into a concise natural language summary that highlights the core discussion points.

### 5. **Processing Multiple Files**  
Scans entire folders of chat logs, generating individual and combined summaries for comprehensive analysis.

---

## **Technologies Used**  
- **nltk:** Natural Language Toolkit for stopword filtering and tokenization.  
- **re:** Regular expressions for text extraction and cleaning.  
- **collections.Counter:** Counting word frequencies for keyword extraction.  
- **os:** File and directory management.  
- **streamlit:** Frontend framework for an interactive web app interface.

---

## **Design Philosophy**  
- **Simple & Effective:** Minimal dependencies and clear logic for easy understanding and maintenance.  
- **Modular:** Each component (parsing, cleaning, keyword extraction) is standalone and reusable.  
- **User Friendly:** Provides clear output with interactive UI for seamless user experience.

---

## **Requirements**  
- Python 3.6+  
- Libraries:  
  - `nltk`  
  - `scikit-learn` (optional, for TF-IDF)  
  - `streamlit`

---

## **User Interface**

###  Initial UI Output (After Running in Browser)
![Image Alt](https://github.com/Ariful129/Qtec/blob/48dbc241b8d9fcb7face3fa9919bab51f64c4914/images/Initial_UI.png)

### Final UI Output (After Running in Browser)
![Image Alt](https://github.com/Ariful129/Qtec/blob/e4d3121b37cd9af13ec66ff7ad35ecdb173f31b4/images/Final_UI.png)

## **Installation & Setup** 🔧  

### Clone the repo:  
```bash
git clone https://github.com/Ariful129/Qtec.git
cd Qtec



