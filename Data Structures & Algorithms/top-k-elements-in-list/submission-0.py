#Create a frequency map
#sort the keys by their value greatest to least
#Output K values by slicing (:k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for number in nums:
            if number not in freq:
                freq[number] = 1
            else:
                freq[number] += 1
        sorted_nums = sorted(freq, key = freq.get, reverse = True)

        return sorted_nums[:k]

