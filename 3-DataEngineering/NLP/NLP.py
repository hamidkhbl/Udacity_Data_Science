from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re


corpus = ["The first time you see The Second Renaissance it may look boring.",
        "Look at it at least twice and definitely watch part 2.",
        "It will change your view of the matrix.",
        "Are the human people the ones who started the war?",
        "Is AI a bad thing ?"]

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()



# 3- Remove stop words
# 4- Stem/Lemmatzie

def tokenize(text):
    # 1- normalize -> converting to lower case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # 2- Tokenize  -> split up the sentence to words
    tokens = word_tokenize(text)
    
    # 3- Remove stop words
    # 4- Stem/Lemmatzie
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    return tokens


# Bag og words
from sklearn.feature_extraction.text import CountVectorizer
# initialize count vectorizer object
vect = CountVectorizer(tokenizer=tokenize)
# get counts of each token (word) in text data
X = vect.fit_transform(corpus)
# convert sparse matrix to numpy array to view
X.toarray()
# view token vocabulary and counts
vect.vocabulary_


# Tfidf Transformer
from sklearn.feature_extraction.text import TfidfTransformer

# initialize tf-idf transformer object
transformer = TfidfTransformer(smooth_idf=False)

# use counts from count vectorizer results to compute tf-idf values
tfidf = transformer.fit_transform(X)

# convert sparse matrix to numpy array to view
tfidf.toarray()

# TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# initialize tf-idf vectorizer object
vectorizer = TfidfVectorizer()

# compute bag of word counts and tf-idf values
X = vectorizer.fit_transform(corpus)

# convert sparse matrix to numpy array to view
X.toarray()
