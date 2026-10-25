#[list], we can add any type of data inside it and they are ordered and mutuable
listing = ["tarun", 1, 89.45, True]
listing[0] = "taru"
for i in listing :

    print(i)

#{dictionary}, key value pair, it is also mutable and duplicates not allowed
dictionary = {"name" : "tarun", "age" : 27, "skills" : "Devops" }
dictionary["name"] = "taru"

for i in dictionary :
    print(dictionary[i])

#(tuples), can store any type of data inside it, they are immutable that is 
# once added then cannot be changed 
tup = ("tarun", 27, "Devops")
print(tup[0])

#{sets}, can store any form of data, they are immutable that is 
#once stored then cannot be changed, dubplicates not allowed, 
#it automatically removes duplicates
sets = {"tarun", 27, "Devops"}
#print(sets[2]) as there is no indexing inside sets and they are not even arranged

#converting a sets into a list 
myList = list(sets)
print(myList[1])

newSet = {1,4,3,6,7,4,5,6,3,4,6,5,2,3,4,1,2,3,4,5,6,7,8,9}

print(newSet)

print("git diff and git diff --staged commnad checking")

print("git rm --cached filename")

print("checking git merge command")

print("hello world") 

print("GIT MERGE CONFLICTS")

print("git merge conflicts Commandssss") 

print("taking fresh pull that will not lead to any merge conflicts")