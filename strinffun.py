from string import punctuation
def remove_punc(text):



    for punc in punctuation:
        text=text.replace(punc,'')
    return text

def word_count(text):
    wordlist=text.split()
    wc={}
    for word in wordlist:
        if word in wc:
            wc[word]+=1
        else:
            wc[word]=1
    return wc  

if __name__=='__main__':
   long_text=''''''
    cln_text=remove_punc(msg)
    print('original:',msg)
    print('cleaned:',cln_text)