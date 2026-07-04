"""
sets-unordered collection of unique items
"""
tags={"python","ai","ml","python"}
print(tags)
print("ai"in tags)
tags.add("rag")
tags.add("ai")
print(tags)
tags.discard("ml")
print (tags)


#to declare an empty dict not set---> empty={}
empty=set()#it declare an emptyy set

#use sets to dedup(removing duplicates) any list
signups=["huoio@.com","hui@.com","hui@.com","yoy.com"]
unique_signups=set(signups)
print(unique_signups)


#set algebra
arjit_skills={"python","ai","devops","containers"}
rohit_skills={"python","git","devops","aws"}
print("Both know ",arjit_skills & rohit_skills) #common in both variables
print("Either knows | ",arjit_skills | rohit_skills)#performing union function
print("Only Arjit ",arjit_skills - rohit_skills)#only found in first variable
print("Exactly one ",arjit_skills ^ rohit_skills)#unique in both variables
