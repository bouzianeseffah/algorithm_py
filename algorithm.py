# Write an algorithm that checks if a string contains another string


from ast import Num


def containString(str1, str2):
    return (str2 in str1)

strg1 = "hello everyone" 
strg2 = "z"
print(containString(strg1, strg2))


#Write a recursive function that takes in a number and returns the sum of the numbers from 0 to the number
def sum_number(num):
    if num == 0 or num == 1:
        return num 
    else:
        return  num + sum_number(num-1)



print(sum_number(5))


#Write a function that takes in a string and returns the string reversed.
def string_reversed(str):
    if len (str) == 0 or len(str) == 1:
        return str
    else:     
       return str[::-1]

print(string_reversed('hello'))    
# Write a recursive function that takes in a list of strings and returns the words capitalized.
def capitalized_str(list):
    if len(list) == 0:
        return ""
    else:
        return(f"{list[0].upper()}  {capitalized_str(list[1:])}")  

sample_list = ['pandas', 'monkeys', 'koalas', 'kangaroos']             
print(capitalized_str(sample_list))

# Write a function that takes in a list of numbers and returns the product of the numbers in the list.
def product_numbers(list):
    if len(list) == 0 :
        return 0
    elif len(list) == 1 :
        return list[0]
    else:
        return list[len(list)-1]*product_numbers(list[:len(list)-1])

           
        
number= [2, 3, 5]
print(product_numbers(number))   

#Write an algorithm that prints the non-repeating integers in a list.
def nonrepeating_integers(test_list):

    # insert elements of list into dictionary (hash table)
    elements = {}
    for i in range(len(test_list)):
        if test_list[i] not in elements:
            elements[test_list[i]]=0
        elements[test_list[i]]+=1
    
    # traverse through elements in dictionary
    for j in elements:
        if (elements[j] == 1):
            print(j)
test_list = [1, 5, 1, 6, 8, 5]
nonrepeating_integers(test_list)











