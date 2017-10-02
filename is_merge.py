def is_merge(s, part1, part2):
    queue = [(s,part1,part2)]
    while queue:
        str, p1, p2 = queue.pop()
        if str:
            if p1 and str[0] == p1[0]:
                queue.append((str[1:], p1[1:], p2))
            if p2 and str[0] == p2[0]:
                queue.append((str[1:], p1, p2[1:]))
        else:
            if not p1 and not p2:
                return True
    return False
print is_merge('codewars', 'code', 'warss')

'''
At a job interview, you are challenged to write an algorithm to check if a given string, s,
can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2 are in the same order as in s.
The interviewer gives you the following example and tells you to figure out the rest from the given test cases.
'''
