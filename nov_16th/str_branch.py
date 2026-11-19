def is_interleave(s1, s2, s3, i=0, j=0):
    if i + j == len(s3):
        return True
    if i < len(s1) and s1[i] == s3[i+j]:
        if is_interleave(s1, s2, s3, i+1, j):
            return True
    if j < len(s2) and s2[j] == s3[i+j]:
        return is_interleave(s1, s2, s3, i, j+1)
    return False

print(is_interleave(s1 = "abc", s2 = "def", s3 = "abdfec"))