set1 = {0,2,4,6,8}
set2 = {1,2,3,4,5}
union_set = set1 | set2
# or
union_set = set1.union(set2)
intersection_set = set1 & set2
# or
intersection_set = set1.intersection(set2)
difference_set = set1 - set2
# or
difference_set = set1.difference(set2)
symmetric_diff_set = set1 ^ set2
# or
symmetric_diff_set = set1.symmetric_difference(set2)
print(union_set,intersection_set,difference_set,symmetric_diff_set)

