# 1.
string_ = 'banana'
index = len(string_) - 1
while index > -1:
    print(string_[index])
    index -= 1

# 2.
string_[:] # this means read all string from start to end

# 3.
def count(word):
    count_ = 0
    for letter in word:
        if letter == 'a':
            count_ = count_ + 1
    return  count_

a_count = count(string_)
print("Number of a in string: ",a_count)

# 4.

#5.

str_ = 'X-DSPAM-Confidence:0.8475'

index = str_.find(':')
str_ = float(str_[index + 1:])
print(str_)

