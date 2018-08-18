num_list = [22,45,65,23,45,87,89,56]
 
odd_nums = []
even_nums = []
 
for x in num_list:    
    if x % 2 == 0:        
        even_nums.append(x)
    else:       
        odd_nums.append(x)
 
print(even_nums)
print(odd_nums)
