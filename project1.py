from nltk.stem import SnowballStemmer
snowball = SnowballStemmer('hindi')
a=input("Enter the word/sentence to be stemmed: ").split(' ')

for i in range(len(a)) :    
    print('Actual : ',a[i],' || ', 'Stem : ', snowball.stem(a[i]),)

