#Create Freq map
#create buckets
#add number and counts into bucket
#create results
#Append to results until results = k

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for number in nums:
            if number not in freq:
                freq[number] = 1
            else:
                freq[number] += 1
        buckets = [[] for i in range(len(nums)+ 1)]

        for number, count in freq.items():
            buckets[count].append(number)
        results = []    
        for i in range(len(buckets) - 1, -1, -1):
            for number in buckets[i]:
                results.append(number)

                if len(results) == k:
                    return results
