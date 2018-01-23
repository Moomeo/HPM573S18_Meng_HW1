#Question 4
yours=['Yale','MIT','Berkeley']
mine=['Yale','Stanford','Tsinghua']

ours1=mine+yours

ours2=[]
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)
#ours1 and ours2 are both lists.
#ours1 contains 6 elements that are either in list yours or list mine.
#ours 2 contains 2 lists, which are list yours and list mine.

yours[2]='Harvard'
print(yours)
print(ours1)
print(ours2)
#List ours2 contains yours, it stores list yours in its own storage
#When list yours is changed, list ours2 automatically changes itself
#ours1 has its own value and is not operated after list yours is changed
#Therefore it still has its original value and remains the same