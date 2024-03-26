# l = [3,7,[1,4,'hello']] Reassign "hello" to be "goodbye"
l=[3,7,[1,4,'hello']]
print('before Reassign',l)
l[2][-1]="goodbye"
print('after Reassign',l)
