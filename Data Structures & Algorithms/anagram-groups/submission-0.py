# create a hashmap to store the values of those that are anagrams
# create loop to loop through each value
#sort word and make sorted word a key 
# if key is not in the hashmap, put it in
# add value to hashmap
#return list of hashmap values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        return list(groups.values())
            