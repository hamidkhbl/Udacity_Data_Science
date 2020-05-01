from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


# 1- normalize -> converting to lower case and remove punctuation
# 2- Tokenize  -> split up the sentence to words
# 3- Remove stop words
# 4- Stem/Lemmatzie
