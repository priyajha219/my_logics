# 1...
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str);

# 2...
# n=int(input())
# i=1
# while i<=n:
#     if i%2==0 or i%3==0:
#         print("*",end=" ")
#     else:
#          print(i,end=" ")
#     i+=1

#3...
# valid date
# d=int(input("enter a no."))
# m=int(input("enter a no."))
# y=int(input("enter a no."))
# if d>0:
#     if m>0:
#         if y>0:
#             if d<=31:
#                 if m<=12:
#                     print("valid date")
#                 else:
#                     print("invalid date")
#             else:
#                 print("invalid date")
#         else:
#             print("invalid date")
#     else:
#         print("invalid date")
# else:
#     print("invalid date")

# 4...
# check prime number or not
# n=int(input("enter a no."))
# i=1
# count=0
# while i<=n:
#     if i%2==0:
#         count+=1
#         i+=1
#     i+=1
# if count==2:
#     print("not prime")
# else:
#     print("prime")

# 5...
# fibonacci
# n=int(input("enter a no."))
# i=1
# a=0
# b=1
# c=0
# while i<=n:
#     a=b
#     b=c
#     c=a+b
#     i+=1  
#     print(c,end="  ")


# 6...
# k="abcdefabcdefg"
# l1=[]
# for i in k:
#     c=0
#     for l in k:
#         if i==l:
#             c+=1
#     if c>0:
#         l1.append([c,i]) 
# print(l1)


# 7...
# str1="Welcome to my blog"
# str2="Welcome to my \n Blog"
# print(str1)
# print(str2)


# 8...
# A="Priya"
# B=1,2,3
# C=str(B)
# for i in (C):
#     if i=="(" or i==")" or i=="," or i==" ":
#         continue
#     A+=i
# print(A)


# 9...
# str="madhu"
# V="a,e,i,o,u"
# vowel=""
# consonant=""
# for i in range(len(str)):
#     if str[i] in V:
#         vowel+=str[i]
#     else:
#         consonant+=str[i]
# print(vowel,consonant)


# 10...
# (1)..simple calculator
# a=int(input("enter a no."))
# b=int(input("enter a no."))
# op=input()
# if op=="+":
#     print(a+b)
# elif op=="-":
#     print(a-b)
# elif op=="*":
#     print(a*b)
# elif op=="/":
#     print(a/b)
# else:
#     print(a**b)


# 11...print "priya123"
# A="Priya"
# B=1,2,3
# C=str(B)
# for i in (C):
#     if i=="(" or i==")" or i=="," or i==" ":
#         continue
#     A+=i
# print(A)


# 12... prime no. till n
# n=int(input("enter a no."))
# for i in range(n):
#     count=0
#     j=1
#     for j in range(1,i+1):
#         if(i%j==0):
#             count=count+1
#     if count==2:
#         print(i)


# 13...prime no. of n numbers
# n=int(input())
# a=0
# i=1
# while True:
#     c=0
#     j=1
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         print(f"{i},is prime no.")
#         a+=1
#     if a==n:
#         break
#     i+=1


# 14...find duplicates in a list
# l=[42,9,9,0,5,42,1,1]
# l2=[]
# for i in range(len(l)):
#     for j in range(i+1,(len(l))):
#         if l[i]==l[j]:
#             l2+=[l[j]]
# print(l2)


# 15...pascal triangle:-
# row=int(input())
# k=1
# for i in range(1,row+1):
#     for a in range(1,(row-i)+1):
#         print(" ",end=" ")
#     for j in range(0,i):
#         if j==0 or i==0:
#             k=1
#         else:
#             k=k*(i-j)//j
#         print(format(k,"<2"),end=" ")
#     print()


# 16...check number is prime or not by using if else:-
# num=int(input())
# p=((2**num-1)%num)
# if p==1:
#     print(num,"is a prime number")
# else:
#     print(num,"is prime number")


# 17...find occurence in a list
# l=["a","b","c","d","a","b","g"]
# for i in range(len(l)):
#     c=1
#     for j in range(i+1,(len(l))):
#         if l[i]==l[j]:


# 18...sum of two list with their carry:-
# l=[2,4,1,3,7]
# l1=[4,2,3,1,5]
# a=[]
# i=1
# c=0
# while i<=len(l):
#     d=l[-i]+l1[-i]+c
#     if i==len(l):
#         a+=[d]
#     else:
#         e=d%10
#         c=d//10
#         a+=[e]
#     i+=1
# print(a)


# 19...year is leap year or not:-
# Year=int(input("enter a year."))
# if Year%400==0:
#     print(Year,"is leap year")
# elif Year%4==0:
#         if Year%100!=0:
#             print(Year,"is leap year")
#         else:
#             print(Year,"is not leap year")
# else:
#      print(Year,"is not leap year")   


# 20...



































        


        












