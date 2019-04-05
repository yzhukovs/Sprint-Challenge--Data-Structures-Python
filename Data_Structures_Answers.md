Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method? O(1) no matter how big the buffer is we are not adding more operations. 

2. What is the space complexity of your ring buffer's `append` function? O(1) -- because we're not allocating any new data structures.

3. What is the runtime complexity of your ring buffer's `get` method? O(n) -- because we're looping once

4. What is the space complexity of your ring buffer's `get` method? O(1) - Since we are just returning the list and getting rid of None values. 


5. What is the runtime complexity of the provided code in `names.py`?  0(n^2) - because of the nested loops with each one of them is n 

6. What is the space complexity of the provided code in `names.py`? O(n) - with duplicates and everything

7. What is the runtime complexity of your optimized code in `names.py`? O(n) - optimized by using set() without using loops at all. 

8. What is the space complexity of your optimized code in `names.py`? in the best case it's O(1) without duplicates and smaller list and worse case it's O(n)
