
'''

Hannah loves halloween because of trick and treat. She not only loves collecting candies during trick and treat
but also loves giving the candies she collects to a children's orphange later. However, there are few rules

1) The number of candies she is donating should be equal to the number of children
2) She cannot open the box and has to give the boxes to the orphanage without adding or removing the candies from the box
3) She does not have any candies of her own and only has the candies that she collects.

Sample Input:

2
3 1 2 3
10
5 5 3 2 5 1
12

Sample Output:

NO
YES

Explanation

For the 1st case, the number of boxes is 3 and the number of children in the orphanage is 10. There is no way that
she can choose the boxes such that the total number of candies add upto 10. Therefore the answer is NO
For the 2nd case, the number of boxes is 5 and number of children in the orphanage is 12. If she picks the boxes with
5,2 and 5 candies, she will have total of 12 candies. Therefore the answer is YES


'''


import itertools

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

def check_chandies(x,y):
    total_candies = 0
    for j in x:
        total_candies += j
        if total_candies == y:
            return 'YES'

def solution(box_list,total_children):
    total_candies = 0
    perm = permutation(box_list)
    result = map(check_chandies,perm,itertools.repeat(total_children, len(perm)))
    if 'YES' in list(set(result)):
        return 'YES'
    else:
        return  'NO'


print(solution([1,2,3],10))
print(solution([5,3,2,5,1],12))
