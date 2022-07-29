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
def sort(word_dict):
    ans =sorted(word_dict.items(),key=lambda val:val[1],reverse=True)    
    return dict(ans)#convert list to dic

if __name__=='__main__':
   long_text='''
   The student of twelth class are going to picnic they all have to bring thier 
   lunch and towels with them and the have to all follow all rules. 
   if they do not follow rules then they have to give fine
   '''
   cln_text=remove_punc(long_text)
   counted_word=word_count(cln_text)
   sorted_words=sort(counted_word)
   print(sorted_words)