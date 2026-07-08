import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()


def transform_text(text):
  """
  Cleans an email by:
  - converting to lowercase
  - removing stopwords
  - removing punctuation
  - applying stemming
  """
  text= text.lower()
  text= nltk.word_tokenize(text)
  y=[]
  for i in text:
    if(i.isalnum()):
      y.append(i)
  text=y[:]
  y.clear()
  for i in text:
    if(i not in string.punctuation and i not in stopwords.words('english')):
      y.append(ps.stem(i))
  return " ".join(y)



if __name__=='__main__':
  print(transform_text("How are you singing anil?"))
