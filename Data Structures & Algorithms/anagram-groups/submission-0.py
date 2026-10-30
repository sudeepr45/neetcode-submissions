class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         anagrams = {}

         for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

         return list(anagrams.values())