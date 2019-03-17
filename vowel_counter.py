
def vowel_counter():
    mystr = input("input a  string of  your choice")
    mystr = mystr.casefold()
    mystr_list= list(mystr)
    vowels=['a','e','i','o', 'u']
    count = 0
    mystrVowel =[]
    for j in mystr_list:
        if j in vowels and j not in mystrVowel:
                mystrVowel.append(j)
    duplicates=set([j for j in mystr_list if mystr_list.count(j)>1])
    mytuple = mystrVowel, len(duplicates)
    print (mytuple) 
vowel_counter()    