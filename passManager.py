import random
import os

from cryptography.fernet import Fernet


def createPass():
    charSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890$@!'
    passLen = input('Enter the password length: ')
    randPass = ''

    for i in range(int(passLen)):
        randPass = randPass + charSet[random.randint(0, len(charSet) )]
    return randPass

def details():
    website = input('Enter the website: ')
    account = input('Enter the Account name: ')
    username = input('Enter the username: ')
    email = input('Email: ')
    otherDetails = input('Other Details: ')
    details = website + '--'+ account +'--' + username + '--' + email + '--' + otherDetails
    return details

def memory(details, password):
    myfile = open('mem.txt','a+')
    toWrite = details + '--' + str(password) + '\n'
    myfile.write(toWrite)
    myfile.close()



def readInfo():
    infoFile = open('mem.txt', 'r')
    info = infoFile.read()
    contents = info.splitlines()


    for acc in range(len(contents)):
        item = contents[acc]
        replaceItem = item.replace('--','\n',5)
        arrayItem = replaceItem.splitlines()
        print(str(acc+1) + ' '+ arrayItem[1])
    
        
    whatAcc = input('What is the index of Account: ')
    acc = contents[int(whatAcc)-1]
    replaceAcc = acc.replace('--','\n',5)
    arrayAcc = replaceAcc.splitlines()
    return arrayAcc

### used https://www.youtube.com/watch?v=H8t4DJ3Tdrg
def encrypt(password_given):
    keyFile = open('key.key','rb')
    key = keyFile.read()
    keyFile.close()


    message = password_given 
    encoded = message.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return encrypted

def decrypt(encryptedPassword):
    keyFile = open('key.key','rb')
    key = keyFile.read()
    keyFile.close()

    f = Fernet(key)
    replacePass = encryptedPassword.replace('b','',1)
    replacePass = replacePass.replace("'",'',2)
    encryptedPassword = bytes(replacePass, 'utf-8')
    decrypted = decrypted = f.decrypt(encryptedPassword)
    
    original = decrypted.decode()
    return original

    
def quit():
    quitInput = input(':> ')
    if quitInput == ':q':
        return False
    else:
        return True


    
    
    
    


   



    


### MAIN ####
notQuit = True
while notQuit:
    print('#########################################\n###                                   ###\n###  Welcome to the Password Manager  ###\n###                                   ###\n#########################################')
    print('[1] = Add Account\n[2] = Create Account and Password\n[3] = Retrive info\n:q = Quit')
    userinput = input(':> ')
      
    if userinput == '1':
        enteredDetails = details()
        enteredPassword = input('Enter the Password: ')
        encryptedPass = encrypt(enteredPassword)
        memory(enteredDetails, encryptedPass)
        notQuit = quit()
    
    if userinput == '2':
        details = details()
        password = createPass()
        encryptedPass = encrypt(password)
        memory(details, encryptedPass)
        notQuit = quit()
    
    if userinput == '3':
        info = readInfo()
        names = ['Website: ','Account: ' ,'Username: ','Email: ','otherDetails: ','Passwords: ']
        for i in range(len(info)):
            if i == 5:
                password = decrypt(info[i])
                print('\n'+names[i]+password)
            else:
                print('\n'+names[i]+info[i])
        
        
        notQuit = quit()
   
    if userinput == ':q':
        notQuit = False
        
    if userinput == '4':
        encrypt()




