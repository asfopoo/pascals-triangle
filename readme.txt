1. Author: Edward Nardo, JHED ID: C2FFF9
2. Module Info: Module 4, Mathematical Sequences, due: Sunday, March 07, 2021
3. Approach:

catalan.py - I started by defining my main and catalan functions.  In my main function I loop through the range
1-15 and print whats returned from calling catalan(i, i).  In the catalan function I started by setting up my base case.
The base case is when k = 1.  You'll notice I sent i to catalan twice.  One of the i's represents n, which does not change
the other i represents k, which is decremented in each recursive call.  That brings us to the recursive call.
I calculate (n+k)/k and multiply it to the call to catalan(n, k-1).  Once we hit our base case, the program multiplies
all of the values and returns.

pascal.py - I started by creating my main and pascal functions.  In the main function I do a nested for loop
where the outer loop goes from 0-10 and the inner loop goes from 0 to i + 1, where i is from the outer loop.
Instead of using lists, I compute each value independently using pascals recursive rule.  I then append the result
to a list and print the values once the inner loop finishes.  This represents each row.  My pascal function is passed
i and j, these represent n and k.  I first set up my base case.  If k == 0, you can sort of think of it as we are
at the beginning of a row.  If n == k then we are at the end of the row so we return 1.  Then using pascals rule,
we add (n - 1, k - 1) to the call to pascal(n-1, k).  Im attaching a breakdown of the process as an example if
the pascal function was computing the fourth row.  I think that's the easiest way to break down the recursion.

                            |n| = |n-1| + |n-1|  Imagine that's all on the same line
Pascals Rule ->             |k| = |k-1| + | k |  and the pipes are multiline parens

4. Known bugs:  None