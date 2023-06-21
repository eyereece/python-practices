def romanToInt(s):
    tmp_d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ans = 0

    for i in range(len(s)):
        if i < len(s) - 1 and tmp_d[s[i]] < tmp_d[s[i+1]]:
            ans -= tmp_d[s[i]]
        else:
            ans += tmp_d[s[i]]

    return ans

s = 'MCMXCIV'
print(romanToInt(s))