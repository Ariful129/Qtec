import os
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download the stopwords dataset 
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Common filler words to exclude from keyword extraction
CONVERSATIONAL_FILLERS = {'hi', 'hello', 'bye', 'thanks', 'thank', 'ok', 'okay'}

def clean_text(text):
    return re.findall(r'\b[a-z]+\b', text.lower())

def extract_keywords(messages, top_n=5):
    all_words = []
    for message in messages:
        all_words.extend(clean_text(message))

    # Filter out common stopwords 
    meaningful_words = [word for word in all_words if word not in stop_words and word not in CONVERSATIONAL_FILLERS]

    # Get the most common words 
    common_words = Counter(meaningful_words).most_common(top_n)

    # Return just the keywords
    return [word for word, _ in common_words]

def parse_chat_file(file_path):
    user_messages = []
    ai_messages = []

    # Read file 
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('User:'):
                user_messages.append(line[len('User:'):].strip())
            elif line.startswith('AI:'):
                ai_messages.append(line[len('AI:'):].strip())

    total_exchanges = len(user_messages) + len(ai_messages)
    all_messages = user_messages + ai_messages

    # Extract top keywords 
    keywords = extract_keywords(all_messages)
    conversation_nature = ', '.join(keywords) if keywords else "general"

    # Create the summary string 
    summary = (
        f"Summary for {os.path.basename(file_path)}:\n"
        f"- The conversation had {total_exchanges} exchanges.\n"
        f"- The user asked mainly about {conversation_nature}.\n"
        f"- Most common keywords: {', '.join(keywords)}."
    )

    return summary

def parse_chat_folder(folder_path):
    summaries = []
    total_exchanges = 0

    # Sort filenames to keep consistent order
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.txt'):
            full_path = os.path.join(folder_path, filename)
            summary = parse_chat_file(full_path)
            summaries.append(summary)

            # Extract total exchanges from the summary line
            for line in summary.split('\n'):
                if line.startswith("- The conversation had"):
                    numbers = re.findall(r'\d+', line)
                    if numbers:
                        total_exchanges += int(numbers[0])

    if summaries:
        combined = "\n\n".join(summaries)
        combined += f"\n\nTotal exchanges across all chats: {total_exchanges}"
        return combined
    else:
        return ""
