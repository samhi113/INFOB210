# Question 1
print("Question 1:")

user1FirstName = "Linus"
user1MiddleName = "Benedict"
user1LastName = "Torvalds"
user1PhoneNumber = "3175551969"
user1Username = "0"
user1Password = "0"

user2FirstName = "Alan"
user2MiddleName = "Mathison"
user2LastName = "Turing"
user2PhoneNumber = "3175555346"
user2Username = "0"
user2Password = "0"

user3FirstName = "Stephan"
user3MiddleName = "Gary"
user3LastName = "Wozniak"
user3PhoneNumber = "3175553720"
user3Username = "0"
user3Password = "0"

user4FirstName = "Adele"
user4MiddleName = ""
user4LastName = "Goldberg"
user4PhoneNumber = "3175552345"
user4Username = "0"
user4Password = "0"

def userCreate(firstName, middleName, lastName, phoneNumber, username, password):
    username = lastName[:6]+firstName[:1]+middleName[:1]
    password = firstName[:2]+middleName[1:6:2]+phoneNumber[6:10]
    
    print("Username: ", username)
    print("Password: ", password)

userCreate(user1FirstName, user1MiddleName, user1LastName, user1PhoneNumber, user1Username, user1Password)
userCreate(user2FirstName, user2MiddleName, user2LastName, user2PhoneNumber, user2Username, user2Password)
userCreate(user3FirstName, user3MiddleName, user3LastName, user3PhoneNumber, user3Username, user3Password)
userCreate(user4FirstName, user4MiddleName, user4LastName, user4PhoneNumber, user4Username, user4Password)
print("\n\n\n")





#Question 2
print("Question 2:")
originalWord1 = "simple"
originalWord2 = "friends"
originalWord3 = "omelet"
originalWord4 = "ions"
newWord = ""

def toPigLatin(originalWord):
    if (originalWord[0] != "a" or originalWord[0] != "e" or originalWord[0] != "i" or originalWord[0] != "o" or originalWord[0] != "u"):
        newWord = originalWord[1:99] + originalWord[:1]+"ay"
    else:
        if (originalWord[1] != "a" or originalWord[1] != "e" or originalWord[1] != "i" or originalWord[1] != "o" or originalWord[1] != "u"):
            newWord = originalWord[2:99] + originalWord[:2]+"ay"
        else:
            if (originalWord[2] != "a" or originalWord[2] != "e" or originalWord[2] != "i" or originalWord[2] != "o" or originalWord[2] != "u"):
                newWord = originalWord[3:99] + originalWord[:3]+"ay"
    
    print("Original Word: ", originalWord)
    print("Pig Latin: ", newWord, "\n")


toPigLatin(originalWord1)
toPigLatin(originalWord2)
toPigLatin(originalWord3)
toPigLatin(originalWord4)