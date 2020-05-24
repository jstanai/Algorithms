# Check if the given string is shuffled substring of another string

s1 = "geekforgeeks"
s2 = "ekegorfkeegsgeek"

# is A a shuffled substring of B?
def is_shuffled_substring(A, B):

    n = len(A)
    m = len(B)

    if (n > m):
        return False
    else:

        A = sorted(A)

        # window slideing over string B
        for i in range(m):

            # only go until length of n (string A)
            if (i + n - 1 >= m): 
                return False

            s = ""

            # copy n elements of B into temp string
            for j in range(n):
                s += B[i + j]

            s = sorted(s)

            if (s == A):
                return True



print(is_shuffled_substring(s1, s2))