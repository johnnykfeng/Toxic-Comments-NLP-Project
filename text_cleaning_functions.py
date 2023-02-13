from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re

del_punct = string.punctuation
del_punct = del_punct.replace("-", "")  # don't remove hyphens
rm_pattern = r"[{}]".format(del_punct)

def clean_text(text):
    text = text.lower()  # convert to all lower case
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    text = re.sub(rm_pattern, "", text)  # remove punctuations
    text = re.sub(r'[0-9]', ' ', text)  # remove digits 0-9
    text = re.sub('\W', ' ', text)   # removes non-word character
    text = re.sub('\s+', ' ', text)  # removes extra spaces
    text = text.strip(' ')
    return text


# Define stopwords to exclude
stop = set(stopwords.words('english'))
stop.update(("to","cc","subject","http","from","sent", "ect", "u", "fwd", "www", "com"))

# Define punctuations to exclude and lemmatizer
exclude = set(string.punctuation)

# df_processed_text = pd.read_csv('processed_text.csv', usecols = ['cleaned_text'])

wordnet_lemmatizer = WordNetLemmatizer()

def text_lemmatizer(text):     
    tokens = word_tokenize(text)
    lemmatized_text = []
    
    for token in tokens:
        # lemmatized = wordnet_lemmatizer.lemmatize(token, pos='v')
        lemmatized_text.append(wordnet_lemmatizer.lemmatize(token, pos='v'))
        lemmatized_text.append(' ')
        
    return ''.join(lemmatized_text)


# text_cleaner includes text_lemmatizer function
def text_cleaner(text):
    text = clean_text(text)
    stop_free = " ".join([i for i in text.lower().split() if((i not in stop) and (not i.isdigit()))])
    punc_free = ''.join(i for i in stop_free if i not in exclude)
    normalized = " ".join(wordnet_lemmatizer.lemmatize(i) for i in punc_free.split())  
    
    return normalized
