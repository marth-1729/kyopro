import string
a=string.ascii_uppercase
print(a)

# 入力した文字列が回文かどうかを判定
def disc_Palindrome(S):
    for i in range(len(S)//2):
        if S[i]!=S[-i-1]:
            print("No")
            exit()