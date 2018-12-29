# 1. we have hash password, need to find the real password.
# 2. we need to create the dictionary
# 3. Dictionary need to be input to same crypto function
# 4. Compare output of our hash function to the hash password.
# 5. how is the design for user
# 6. user need to input the dictionary file and password file
# 7. Password file is in some format
import crypt
def testpass(cryptPass):
    try:
        dictFile = open("dic.txt")
        salt = cryptPass[0:2]
        for line in dictFile.readlines():
            line = line.strip('\n')
            password = crypt.crypt(line,salt)
            if password == cryptPass:
                print "[+] The password is " + password
                return
    except:
        print "There is wrong dictionary file"
    print "[-] Hmm, No password found."
    return
        
def main():
    try:
        passFile = open("passwd.txt")
        for line in passFile.readlines():
            if ":" in line:
                user = line.split(':')[0]
                print "Cracking Password for user: " + user
                cryptPass = line.split(':')[1].strip(' ')
                testpass(cryptPass)    

    except:
        print "No passwd file"
if __name__ == "__main__":
    main()

