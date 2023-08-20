k=0; j=0; d=0
email= input("Enter your Email: ")
if len(email) >=6:
    if email[0].isalpha(): #email 0th index is an alphabet or not
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]=='.') ^ (email[-4]=='.'): # xor operator
                for i in email:
                    if i==i.isspace(): # no space in email
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                     print('fck off')     
            else:
                print('fck off')
        else:
            print('fck off')
    else:
        print('Fck off')
else:
    print('Fck off')
