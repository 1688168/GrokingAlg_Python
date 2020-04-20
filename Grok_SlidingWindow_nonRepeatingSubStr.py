from timeit import default_timer as timer

def non_repeat_substring(str):
    ss = set()

    max_len = -1
    curr_len = 0

    for c in str:
        if c in ss:
            curr_len = 1
            ss=set(c)
        else:
            curr_len += 1
            max_len = max(max_len, curr_len)
            ss.add(c)

    return max_len


start = timer()
o=non_repeat_substring("abccde")
end = timer()
print(end - start)
print(o)