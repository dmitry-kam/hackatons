import time
from itertools import permutations as itertools_permutations


def cmp(a, b):
    return (a > b) - (a < b) 

def next_permutation(seq, pred = cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""

    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    
    if not seq:
        raise StopIteration

    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")

    first = 0
    last = len(seq)
    seq = seq[:]

    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            # Step 1.
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                # Step 3.
                reverse(seq, next1, last)

                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration
    
def permutations(arr):
    global filled
    global unfilled
    result = []
    print(itertools_permutations(arr))
    for perm in itertools_permutations(arr):
        v = list(perm)
        print(perm)
        #exit()
        if v not in result and checkPermutation(v): 
         #result.append(expandPermutation(v, filled))
         result.append(v)
    
    return list(map(lambda x: expandPermutation(x, filled), result))    
    
xfadfaf = [3, 3, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']   
xfadfaf = [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

start = time.time()   

try:
    for p in next_permutation(xfadfaf):
        print(p)  
except:
    print("An exception occurred")

	
end = time.time()
time1 = end - start
print("1", time1, "seconds!")

start = time.time()

for perm in itertools_permutations(xfadfaf):
    v = list(perm)
    
   

end = time.time()
time2 = end - start
print("2", time2, "seconds!")	
print(time2/time1)	    
exit()
