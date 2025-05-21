# AI Chat Log Analysis and Summary 📊

## Project Overview 📝
AI Chat Log Analysis and Summary is a Python-based tool designed to analyze chat logs between a user and an AI. It reads `.txt` files containing the conversation, processes the data, and generates detailed summaries with message statistics and key insights. This project leverages **natural language processing (NLP)** techniques to extract meaningful keywords, track conversation flow, and provide an informative summary.

---

## Features ⭐
- **Chat Log Parsing**: Reads `.txt` files and separates messages by speaker (User and AI).
- **Message Statistics**: Counts the total number of messages, user messages, and AI messages.
- **Keyword Extraction**: Identifies the top 5 most frequently used keywords excluding stopwords and conversational fillers.
- **Summary Generation**: Creates a readable summary including:
  - **Total number of exchanges** (User and AI messages).
  - **Main topics** discussed (based on keyword extraction).
  - **Most common keywords**.
- **Batch Processing**: Supports processing multiple chat logs at once from a folder.
- **User Interface**: Uses **Streamlit** to display results in an interactive web app.

---

## **Methodology** 🧠

### **1. Chat File Parsing** 📁
The tool reads `.txt` files line by line and separates the conversation into `User` and `AI` messages. These messages are stored in two separate lists to track the conversation flow.

### **2. Text Cleaning** 🧹
The tool processes the messages by:
- Extracting only alphabetic characters.
- Converting text to lowercase.
- Removing **stopwords** (e.g., "the", "and", "is") and **conversational fillers** (e.g., "hi", "thanks", "bye").

### **3. Keyword Extraction** 🔑
Once the text is cleaned, the tool analyzes the most frequently occurring words using Python's `collections.Counter`. The **top 5 most frequent keywords** are selected, providing a clear indication of the conversation's main topics.

### **4. Summary Generation** 🧾
A summary is generated that includes:
- **Total number of exchanges** (User + AI messages).
- **Main topics discussed**, based on the most common keywords.
- **List of the top 5 keywords**.

### **5. Batch Processing (Folder Support)** 📂
The tool can process multiple `.txt` chat log files at once. The function `parse_chat_folder(folder_path)` processes all `.txt` files in a specified folder, and the final output is a combined summary of all chat logs.

---

## **Libraries and Tools Used** 🛠️
- **nltk**: For text processing, including stopword removal and tokenization.
- **re**: For regular expressions used in text cleaning and pattern matching.
- **collections.Counter**: For frequency analysis of words.
- **os**: For file handling and navigation.
- **streamlit**: For building the frontend web application where users can interact with the tool and view the generated summaries.

---

## **Design Philosophy** 💡
- **Simplicity**: The project focuses on simple, efficient solutions without relying on complex machine learning models.
- **Modularity**: Each function is designed to be independent and reusable for easier testing and maintenance.
- **Clarity**: The logic and flow of the program are transparent and easy to understand.

---

## **Requirements** ⚙️
- **Python**: Version 3.6 or higher
- **Libraries**:
  - `nltk` (for text processing and stopword removal)
  - `scikit-learn` (for TF-IDF, optional feature)
  - `streamlit` (for creating the frontend web app)

---

## **Installation** 🔧

### **Step 1: Clone the Repository**
Clone the repository to your local machine: https://github.com/Ariful129/Qtec/tree/main

## **User Interface**
i). install streamlit in VS code
ii).use streamlit run app.py

# ** Output(Initial UI)
![Image Alt](https://github.com/Ariful129/Qtec/blob/48dbc241b8d9fcb7face3fa9919bab51f64c4914/images/Initial_UI.png)

# ** Output(Final UI)
![Image Alt](https://github.com/Ariful129/Qtec/blob/e4d3121b37cd9af13ec66ff7ad35ecdb173f31b4/images/Final_UI.png)



