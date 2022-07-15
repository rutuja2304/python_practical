#P7 Q.6 To find tuples which have all elements divisible by k from list of tuple.


my_tuple = [(4, 24, 12), (7, 9, 6), (12, 18, 21)]
print("The original list is : " + str(my_tuple))
K = 4
l=[]
for i in range(len(my_tuple)):
    # for j in range(len(my_tuple)):
    if ((all(my_tuple[i]))%K==0):
                # l=my_tuple.pop(my_tuple[i])
        l.append(my_tuple[i])
print(l)
# print(len(my_tuple))


