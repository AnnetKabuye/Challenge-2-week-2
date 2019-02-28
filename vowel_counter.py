
def vowel_counter():
    mystr = input("input a  string of  your choice")
    mystr_list= list(mystr)
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for i in vowels:
            for j in mystr_list:
                    if i==j:
                            count +=1
                            print(j, count)
vowel_counter()