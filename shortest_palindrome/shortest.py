def shortest_palindrome(b):
    def find_palindrome(a):
        start = 0
        end = len(a)-1
        while start < end:
            if a[start] != a[end]:
                return False
            start += 1
            end -= 1
        return True

    if find_palindrome(b):
        if len(b) % 2 == 0:
            return b[round(len(b)/2)-1:round(len(b)/2)+1]
        else:
            return b[round(len(b)/2)-2:round(len(b)/2)+1]

print(shortest_palindrome('hajjah'))
print(shortest_palindrome('halalah'))