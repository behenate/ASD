def quick_sort_half(t,start=0,end=None):
    if end is None:
        end = len(t)-1
    left = start
    right = end
    half_element = t[(start+end)//2]
    while left <= right:
        while t[left] < half_element:
            left += 1
        while t[right] > half_element:
            right -= 1
        if left <= right:
            t[left], t[right] = t[right], t[left]
            left +=1
            right -=1
    if start < right:
        quick_sort_half(t, start, right)
    if end > left:
        quick_sort_half(t, left, end)
    return t