def alphabetical_subset(word):
    n = len(word)
    unique = 0
    m_cnt = [0 for _ in range(ord("a"), ord("z")+1)]
    in_stack = [False for _ in range(ord("a"), ord("z") + 1)]
    for l in word:
        idx = ord(l)-97
        if m_cnt[idx] == 0:
            unique += 1
        m_cnt[idx] += 1
    stack = []
    for i in range(n):
        if len(stack) == 0:
            stack.append(word[i])
            in_stack[ord(word[i])-97] = True
            m_cnt[ord(word[i])-97] -= 1
            continue
        print(stack, ord(stack[-1]) - 97, stack[-1])
        while len(stack) != 0 and ord(word[i]) < ord(stack[-1]) and m_cnt[ord(stack[-1]) - 97] > 0:
            in_stack[ord(stack[-1]) - 97] = False
            stack.pop()

        if not in_stack[ord(word[i])-97]:
            in_stack[ord(word[i]) - 97] = True
            stack.append(word[i])
        print(word[i])
        m_cnt[ord(word[i]) - 97] -= 1
    print(stack)

alphabetical_subset("cbacdcbcdcabcd")
