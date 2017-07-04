## Contest 39

### Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
```
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
```
Example 2:
```
Input: 3
Output: False
```
**Solution**
```Python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if(math.sqrt(c).is_integer()):
            return True
        top = int(math.sqrt(c))
        for i in range(1,top+1):
            if(math.sqrt(c-i*i).is_integer()):
                return True
        return False
```

### Design Log Storage System
You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: `Year:Month:Day:Hour:Minute:Second`, for example, `2017:01:01:23:59:59.` All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.


int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:
```
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
```
**Note:**
There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.

**Solution**
```Python
import datetime
import calendar
class LogSystem(object):

    def __init__(self):
        self.logList = []
        self.index = {'Year':4, 'Month':7,'Day':10,'Hour':13,'Minute':16,'Second':19}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logList.append((id,timestamp))
        return
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        index = self.index[gra]
        sCut = s[:index]
        eCut = e[:index]
        
        ans = []
        for tid, timestamp in self.logList:
            if(sCut <= timestamp[:index] and eCut >= timestamp[:index]):
                ans.append(tid)
        
        return sorted(ans)    


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
```

**Summary:**
> In python, string can be directly compared with each other. So in this problem, first cut the log string to the provided `gra`. For instance, if `gra='Month'`, then `2017:01:01:23:00:00` should be cut to `2017:01`.

### Find the Derangement of An Array
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 10e9 + 7.

Example 1:
```
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
```
**Note:**
n is in the range of [1, 10e6].
**Solution**
```Python
class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        F0, F1 = 1, 0
        for i in range(2,n+1):
            F0, F1 = F1, (i-1)*(F0 + F1) % MOD
        return F1
```
**Summary:**
> For an array of length N, say we have D(N) derangements. Then we consider the first element and put it somewhere else, say we put it at the ith position. Then item i has two choices, one is ending up at position 1, then the other N-2 elements has D(N-2) derangements; or element i chooses somewhere other than 1, then i along with the other N-2 elements have D(N-1) derangements. So D(N) = (N-1)*(D(N-2) + D(N-1)). This is similar to the Fibonacci sequence with an additional (N-1). So we use a for loop to calculate D(N).

### Smallest Range
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
```
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
```
Note:
1. The given list may contain duplicates, so ascending order means >= here.
2.  1 <= k <= 3500
3. -105 <= value of elements <= 105.
4. For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

**Solution**
```Python
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        for i,row in enumerate(nums):
            heap.append((row[0], i, 0))
        heapq.heapify(heap)

        ans = -1e9,1e9
        right = max(row[0] for row in nums)
        while(heap):
            (left,i,j) = heapq.heappop(heap)
            if(right - left < ans[1] - ans[0]):
                ans = left,right
            if(j+1 == len(nums[i])):
                return ans
            
            next = nums[i][j+1]
            right = max(next, right)
            heapq.heappush(heap, (next, i, j+1))
        return ans
```
**Summary:**
A detailed explaination can be found in this [Yotube video](https://www.youtube.com/watch?v=Fqal25ZgEDo).

