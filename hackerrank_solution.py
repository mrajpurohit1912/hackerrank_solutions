#The Minion Game

# def minion_game(string):
#     vowels = "AEIOU"
#     stuart_score = 0
#     kevin_score = 0
#     len_str = len(string)
#     for i in range(len_str):
#         if string[i] in vowels:
#             kevin_score += 1
#         else:
#             stuart_score += 1

#     if stuart_score > kevin_score:
#         print("Stuart {}".format(stuart_score))
#     elif kevin_score > stuart_score:
#         print("Kevin {}".format(kevin_score))
#     else:
#         print("Draw")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)



#itertools.product() 

# from itertools import product

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))


# print(list(product(a,b)))


#itertools.permutations()

# s = "HACK"

# for i in s:
#     for j in s:
#         print(i + j)


# from itertools import permutations
# str1, int1 = input().split()

# for i in sorted(permutations(str1, int(int1))):
#     print (''.join(i))