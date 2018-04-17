from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
from collections import defaultdict
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
import pandas as pd

url=input()
webpage = urlopen(url)
soup = BeautifulSoup(webpage,'html.parser')
stop=set(stopwords.words('english'))
c=""
exclude=set(string.punctuation)
for i in soup.find_all('p'):
    c=c+" "+i.getText()
x=" ".join(i for i in c.lower().split() if i not in stop)
x=''.join(i for i in x if not i.isdigit())
x=''.join(i for i in x if i not in exclude)
freq=Counter()
for i in x.split():
    freq[i]+=1
df=pd.DataFrame([col1,col2] for col1,col2 in freq.items())
HEADER = '''
<html>
<head>
<style>
.df tbody tr:last-child { background-color: #FF0000; }
</style>
</head>
<body>
'''
FOOTER = '''
</body>
</html>
'''
with open("freq_tab_after.html","w",encoding="utf-8") as f:
    f.write(HEADER)
    f.write(df.to_html(classes='df'))
    f.write(FOOTER)
    
