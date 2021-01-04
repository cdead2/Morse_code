import sys,huepy
morse={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','P':'.--.','Q':'--.-','O':'---','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','.':'.-.-.-',',':'--..--',';':'-.-.-.','?':'..--..','!':'-.-.--'}
def morse_encoder(text):

    date=text
    morse_data=[]
    for i in date:
        try:
            i=i.upper()
            morse_data.append(morse[i])
        except:
            morse_data.append(' ')
    return morse_data
revers_={}
def morse_decoder(morse_,morse):
    for i in morse:
        revers_[morse[i]]=i
    data=[]
    for i in morse_:
        try:
            
            data.append(revers_[i])
        except:
            data.append(i)
            #pass
    return data
   


def help():
    return  '''
    en >to encrypt a text
    de >to decrypt a text
To encode_text:
    Example : python3 morse_decoder en hello world
    Output :  .... . .-.. .-..   .--   .-. .-.. -..
To decode_morse:
    Example : python3 morse_decoder de .... . .-.. .-..   .--   .-. .-.. -..
    Output : hello world

'''
try:
    choose=sys.argv[1]
    text=sys.argv[2:]
    if choose=='en':
        text=''.join(text)
        text=list (text)
        print (huepy.yellow('Your morse encryption : '+' '.join(morse_encoder(text))))
    elif choose=='de':
        text=sys.argv[2::]
        print(huepy.green('Your decrypted text : '+' '.join(morse_decoder(text,morse))).lower())
    else:
        print (huepy.green(help()))

except:
    print (huepy.green(help()))

