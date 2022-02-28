def file2list(filename):
    return open(filename).readlines()

a = file2list("prep.txt")
dict = {}
cnf=""
and_clauses=""
or_clauses=""

for line in a:
    dict = {}
    words=line.split(",")
    cnf = words[0]
    or_clauses = cnf.split("^")
    print("CNF: ", cnf)
    print("Or Clauses: ", or_clauses)
    for word in words:
        if '=' in word:
            print(word)
            dict[word[:-2]]=word[-1]
            if word[-1]=="\n":
                word=word.replace('=','')
                dict[word[:-2]]=word[-2]
    print("Dictionary: " , dict)
    
    final_string = ''.join(str(dict.get(a, a)) for a in cnf)
    print("Final String: ", final_string)
    
    '''clauses_and = final_string.split("^")
    print("Clause And: ", clauses_and)'''
    not_value = final_string.find("~")
    if not_value>0:
        print("Not value index: ", not_value)
        print("Not:",final_string[not_value+1])
        if final_string[not_value+1]=="F":
            updated_string = final_string[:not_value+1] + "T" + final_string[not_value+1+1:]
        final_updated_string = updated_string.replace("~","")
        if final_string[not_value+1]=="T":
            updated_string = final_string[:not_value+1] + "F" + final_string[not_value+1+1:]
        final_updated_string = updated_string.replace("~","")
        print("Updated string:",final_updated_string)
    
    clauses_and = final_updated_string.split("^")
    print("Clause And: ", clauses_and)
    true_value="T"
    for string in clauses_and:
        if true_value in string:
            print("Value:" , true_value)
        else:
            print("This value is F. So the whole sentence is False" )
    print("Every values are `T` so the whole sentence is True")
  
