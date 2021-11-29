import re
inputfile = 'orwiki.xml'

input = open(inputfile,'r')
out = open('odia-words.txt','w')

def is_odia(word):
#    word = word.decode('utf-8')
    first_char = word[:1]
    lang_number = ord(first_char)
    if lang_number >= 2816 and lang_number <= 2943:
        return True


for line in input.readlines():
    for word in line.split(" "):
 #       try:
        if len(word) > 1:
            output = re.sub(r'\s*[A-Za-z]+\b', '' , word)
            output = re.sub(r'[?|$|।|`|~|@|#|^|&|*|(|)|+|=|{|}|<|,|>|/|\|.|?|!|:|;]','',output)
            output = output.replace('|','')
            output = output.replace('"','')
            output = output.replace('[','')
            output = output.replace(']','')
            output = output.replace("'",'')
            output = output.replace("‘",'')
            output = output.replace("’",'')
            output = output.replace("“",'')
            output = output.replace("”",'')
            output = output.replace("--",'-')
            output = output.rstrip()
            if len(output) > 1:
                if is_odia(output):
                    print (output)
                    out.write(output+'\n')

#        except:
#            print (" ")


input.close()
out.close()



odia_words_set = set(map(str.strip, open('odia-words.txt')))
uniq_words = open('unique_odia_words.txt','w')

for word in odia_words_set:
    uniq_words.write(word)
    uniq_words.write("\n")
uniq_words.close()
