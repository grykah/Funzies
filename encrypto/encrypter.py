def string():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

def hexupper():
    return '0123456789ABCDEF'

def maxchar():
    return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()`~-_=+[]\{}|;:",./<>?'

def LetNum(colletter):
    rcol = colletter[::-1].upper()
    count = 0
    colnum = 0
    for char in rcol:
        colnum = colnum + (string().index(char)+1)*27**count
        count = count + 1        
    return colnum

def NumLet(colnum):
    count = 1
    rcolletter = ''
    while colnum > 0:
        modcol = (colnum % (27) - 1)
        if modcol < 0 and colnum > 0:
            rcolletter = rcolletter + string()[26]
            modcol = 25
        else:
            rcolletter = rcolletter + string()[modcol]
        colnum = (colnum - modcol)//27
        count = count + 1
    colletter = rcolletter[::-1]
    return colletter

def NumMax(colnum):
    count = 1
    rmax = ''
    while colnum > 0:
        modcol = (colnum % (len(maxchar())) - 1)
        if modcol < 0 and colnum > 0:
            rmax = rmax + maxchar()[-1]
        else:
            rmax = rmax + maxchar()[modcol]
            colnum = (colnum - modcol)//len(maxchar())
            count = count + 1
    maxout = rmax[::-1]
    return maxout

def MaxNum(maxout):
    rmax = maxout[::-1]
    count = 0
    colnum = 0
    for char in rmax:
        colnum = colnum + (maxchar().index(char)+1)*len(maxchar())**count
        count = count + 1
    return colnum

def Encrypt(text):
    encrypted = NumMax(LetNum(text))
    return encrypted

def Decrypt(encrypted):
    decrypted = NumLet(MaxNum(encrypted))
    return decrypted

again = True
while again is True:
    prompt = ''

    while prompt not in ['E', 'D']:
        prompt = input('Enter "E" to encrypt or "D" to decrypt: ').upper()

    if prompt == 'E':
        santext = ''
        text = str(input('Input text to encrypt: ').upper())
        for char in text:
            if char in string():
                santext = santext + char
        print(Encrypt(santext))

    else:
        print(str(Decrypt(input('Input text to decrypt: '))))
    ask = ''
    while ask not in ['Y', 'N']:
        ask = input('Run script again? (y/n) ').upper()
    if ask == 'Y':
        again = True
    else:
        again = False
               
