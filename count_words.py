##from collections import Counter
##
##words = [
##'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
##'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
##'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
##'my', 'eyes', "you're", 'under'
##]
##
##word_counts = Counter(words)
##top_three = word_counts.most_common(3)
##print(top_three)

##from operator import itemgetter
##from pprint import pprint
##
##rows = [
##{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
##{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
##{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
##{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
##]
##
##rows_by_fname = sorted(rows, key=itemgetter('fname'))
##rows_by_uid = sorted(rows, key=itemgetter('uid'))
##
##pprint(rows_by_fname)
##pprint(rows_by_uid)
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
