## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>
# Use the following list - 
def lessThan_ten(n):
    lst=[]
    for i in lst:
        if i<10:
            lst.append(i)
    return(lst)
print(lessThan_ten([1,11,14,5,8,9]))




## Exercise 2 <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# Hint: You can use the .sort() method
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
def twoList(l_1,l_2):
    list1=[]
    list2=[]
    for i in range (1,list1+1):
        list1.append(list1)
    for i in range (1,list2+1):
        list2.append(list2)

    list3=list1+list2
    list.sort()
    print(list3)



