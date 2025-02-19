# pattern = "abba" 
# s = "dog cat cat dog"
# unique=[]
# for i in pattern:
#     if i not in unique:
        
#         unique.append(i)
# t=s.split()     
# for i,j in enumerate(unique):
#     j=t[i]
#     print(j)
#     for k in pattern:
        
#         if k!=t:
            
#             print(False)
            
#         else:
            
#             print(True)

# pattern = "abba"
# s = "dog cat cat dog"

# # Split the string into words
# words = s.split()

# # Check if the length of the pattern matches the number of words
# if len(pattern) != len(words):
#     print(False)
# else:
#     # Create dictionaries to map characters to words and vice versa
#     char_to_word = {}
#     word_to_char = {}

#     for char, word in zip(pattern, words):
#         # Check the mapping from character to word
#         if char in char_to_word:
#             if char_to_word[char] != word:
#                 print(False)
#                 break
#         else:
#             char_to_word[char] = word

#         # Check the mapping from word to character
#         if word in word_to_char:
#             if word_to_char[word] != char:
#                 print(False)
#                 break
#         else:
#             word_to_char[word] = char
#     else:
#         print(True)

    
    
# nums = [2,2,1,1,1,2,2,1,1]
# # Output: 2
# dic={}
# for i in nums:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# maxi=max(dic.values())
# for i in dic:
#     if dic[i]==maxi:
#         print(i)

# n=int(input())
# k=list(map(int,input().split()))
# t=k[0]
# l=k[1]
# new=list(map(int,input().split()[:t]))

# for i in range(l):

#     new[0]==new[-1]
    

# print(new)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# size_count=int(input())
# sizes_available=list(map(int,input().split()))
# number_customer=int(input())
# sum=0
# for i in range(number_customer):
#     size_price=list(map(int,input().split()))
#     if size_price[0] in sizes_available:
#         sizes_available.pop(size_price[0])
#         sum+=size_price[1]
# print(sum)
        
        
# n="sswwwwiiisertysdfgytttttss"
# dic={}
# new=[]
# for i in n:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# for i in dic:
#     if dic[i]==1:
#         new.append(i)
# print(new[0])
# Simple version of the code to map numbers to letters

# Function to map numbers to letters (a-z for 0-26, '.' otherwise)



# def number_to_alphabet(num):
#     if num>0:
#         alpha=chr(ord('A')+num-1)
    
#         return alpha
#     else:
        
#         return "."

# n,m=list(map(int,input().split()))

# storage=[]

# for i in range(n):
    
#     row=list(map(int,input().split()))
    
#     storage.append(row)

# main_output=[]
# for k in storage:
#     output=[]
#     for num in k:
#         final_output=number_to_alphabet(num)
#         output.append(final_output)
#     main_output.append(output)
    
# print("output")
# for i in main_output:
#     print(" ".join(i))
    
# Input the number of rows


# n = int(input("Enter the number of rows: "))

# print("Enter the grid values:")
# grid = []

# # Input the grid
# for _ in range(n):
#     row = list(map(int, input().split()))
#     grid.append(row)

# # Process to find indices of numbers left to zero
# print("\nOutput:")
# for row in grid:
#     for i in range(1, len(row)):  # Start from 1 to check the left side
#         if row[i] == 0:
#             print(row[i - 1])  # Print the number to the left of zero


# import datetime

# day,month,year=map(int,input().split())

# date_obj=datetime.date(year,month,day)

# day_of_week=date_obj.strftime("%A").upper()

# print(day_of_week)

# s="India is my country"

# new_s=s.lower()

# emty={}

# for i in new_s:
    
#     if i in emty:
        
#         emty[i]+=1
        
#     else:
        
#         emty[i]=1
        
# print((emty))
    
    
# input:
    
#     ( ()) (((()()()))) (() )

# output:
#     ["(()),(((()()())))","(())"]


# input_str = "( ())((( ()()() )))(() )"
# stack=[]
# result=[]
# temp=""
# for i in input_str:
    
#     if i =="(":
        
#         stack.append(i)
        
#         temp+=i
        
#     elif i==")":
        
#         if stack:
            
#             stack.pop()
            
#             temp+=i
            
#             if not stack:
                
#                 result.append(temp)
                
#                 temp=""
                
# print(result)

# import re

# password=input("Enter The Password: ")

# if(8<= len(password) <20) and re.search(r"\d",password) and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[$&@]",password):
    
#     print("password Valid")
    
# else:
    
#     print("Invalid")


# n=4
# k=1

# for i in range(1,n+1):
    
#     for j in range(i):
        
#         print(chr(64+k),end=" ")
        
#         k+=1
        
#     print()

# n = 4
# k = 1

# for i in range(1, n + 1):
#     for j in range(i):
#         if (i + j) % 2 == 0:
#             print(chr(64 + k).lower(), end=" ")  # Uppercase letter
#         else:
#             print(chr(64 + k), end=" ")  # Lowercase letter
#         k += 1
#     print()

# n=5

# for i in range(1,n+1):
    
#     for j in range(6-i):
        
#         print(j+i,end=" ")
        
#     print()
    
# for i in range(n):
    
#     for j in range(i):
        
#         print(j+1,end=" ")
        
#     print()

# n = 5

# for i in range(n):
    
#     for j in range(n):
#         print((i + j) % n + 1, end=" ")  # Circular shifting logic
#     print()

# n=5

# for i in range(n+1):
    
#     for k in range(6-i):
        
#         print(" ",end=" ")
    
#     for j in range(i,0,-1):
        
#         print(j,end=" ")
        
#     print()


# n = 5

# for i in range(n-1):

#     for k in range(n - i - 1):
        
#         print(" ", end="")

#     for j in range(2):
        
#         if j == 0:
            
#             print("*", end="")
            
#         else:
            
#             print(" " * (2 * i - 1) + "*", end="") if i > 0 else None

#     print()
    
# for i in range(n-3,-1,-1):

#     for k in range((n-1)-i):
        
#         print(" ", end="")

#     for j in range(2):
        
#         if j == 0:
            
#             print("*", end="")
            
#         else:
            
#             print(" " * (2 * i - 1) + "*", end="") if i > 0 else None

#     print()

# n=5

# p=1

# for i in range(1,n):
    
#     for k in range((n-1)-i):
        
#         print(" ",end="")
        
#     row=[]
        
#     for j in range(i):
        
#         row.append(p)
        
#         p+=1
        
#     for l in reversed(row):
            
#         print(l,end=" ")

#     print()
    
# d=10

# for i in range(n-1,0,-1):
    
#     for k in range((n-1)-i):
        
#         print(" ",end="")
        
        
#     for j in range(i):
            
#         print(d,end=" ")
        
#         d-=1

#     print()
    
# n=6
# d=1
# for i in range(1,n+1):
    
#     for j in range(i):
        
#         if d%2!=0:
            
#             print(d,end=" ")
            
#             d+=1
            
#         elif d%2==0:
            
#             print(d,end=" ")
            
#             d+=1
        
#     print()
    
    
# n=6
# d=1
# for i in range(1,n+1):
    
#     for k in range(n-i):
        
#         print(" ",end=" ")
    
#     if i%2!=0:
        
#         start=1+(i//2)*2
        
#         d+=1
        
#     else:
        
#         start=2+(i//2-1)*4
        
#         d+=1
        
#     for j in range(i):
        
#         print(start+2*j,end=" ")
        
#     print()
        
# s="CD"
# roman={"I":1,
#        "V":5,
#        "X":10,
#        "L":50,
#        "C":100,
#        "D":500,
#        "M":1000}

# res=0

# for i in range(len(s)):
    
#     if i+1 < len(s) and roman[s[i]]<roman[s[i+1]]:
        
#         res-=roman[s[i]]
        
#     else:
#         res+=roman[s[i]]
        
# print(res)

# s=8889
# roman=[(1000,"M")]
# ""
# n="u=r-gm,o=r-,t=gwr--"
# result1=""
# for i in n:
#     if i=="u" or i=="o" or i=="t" or i=="=":
#         continue
#     else:
#         result1+=i
# result2=result1.split(",")
# result3=""
# val={"r":4,"w":3,"g":2,"m":1,"-":0}
# for i in result2:
#     sum=0
#     for j in i:
#         sum+=val[j]
#     result3+=str(sum)
# print(result3)

# n="XXX"
# val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# values=0
# for i in range(len(n)):
    
#     if i+1<len(n) and val[n[i]]<val[n[i+1]]:
        
#         values-=val[n[i]]
#     else:                                 I V X L C D M
        
#         values+=val[n[i]]
# print(values)

# n=256
# val=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

# roman=""

# for value,string in val:
    
#     while n >=value:
        
#         roman+=string
        
#         n=n-value
# print(roman) 


# word=["suha","suh","suhai"]
# res=""
# for i in range(len(word[0])):
#     for h in word:
#         if i==len(h) or h[i]!=word[0][i]:
            
#             print(res)
            
#             exit()
#     res+=word[0][i]
# print(res)
        
        
# s="(({{}}(())))"
# stack=[]
# close_to_open={")":"(","}":"{","]":"["}
# for i in s:
#     if i in close_to_open:
#         if stack and stack[-1]==close_to_open[i]:
#             stack.pop()
            
            
#         else:
            
#             print(False)
            
#             exit()
            
            
#     else:
        
#         stack.append(i)
        
# if stack:
    
#     print(False)
    
# else:
    
#     print(True)
        
        
# Find prime numbers in a given range
# start = 1
# end = 50
# for num in range(start,end+1):
    
#     if num >1:
#         for i in range(2,int(num**0.5)+1):
            
#             if num%i==0:
                
#                 break
#         else:
#             print(num,end=" ")

# import sys
# val=sys.stdin.read().split()
# assign=""
# for i in val:
#     assign+=i
# a=int(assign[0])
# d=int(assign[1])
# n=int(assign[2])
# arithmetic=a+(n-1)*d
# print(arithmetic)

    