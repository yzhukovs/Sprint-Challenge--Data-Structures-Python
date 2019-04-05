import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:   #runtime: 7.575293064117432 seconds
#         if name_1 == name_2:
#             duplicates.append(name_1)

#USING DICTIONARY AND LOOP------------
# lookup_names = {} #using dictionary 
# for name_1 in names_1:  # O(n)
#     lookup_names[name_1] = name_1	# O(1)
    
# for name_2 in names_2:  # 0(n)
#     if name_2 in lookup_names:  # lookup in dictionary is O(1)
#         duplicates.append(lookup_names[name_2])

# #runtime: 0.005610942840576172 seconds

#USING SET() ------------------------
duplicates = set(names_1) & set(names_2)
#runtime: 0.004784107208251953 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

