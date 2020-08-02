# The length of the smallest substring consisting of maximum distinct characters
# Python 3 code
# Name -> sumal 


def findSubString(s):
    n = len(s)
    # Check is there is a valid string i.e. 0<s<10^5
    if n == 0 and n > 10000:
        return 0
    else:
        temp = ''        # Temp string  
        max_len = 0      # length of string with max distinct characters
        start_index = 0  # starting index of the string

        for no in range(start_index, n):
            for number in range(start_index, n):
                if not temp.__contains__(s[number]):
                    temp += s[number]
                    if len(temp) > max_len:
                        max_len = len(temp)
            temp = ''           # empty temp string with a specific starting index 
            start_index += 1    # Increment the value of starting index to check all the substring 
        return max_len


if __name__ == '__main__':
    print("Length of smallest substring containing maximum distinct characters is: {}"
          .format(findSubString("abcda")))

