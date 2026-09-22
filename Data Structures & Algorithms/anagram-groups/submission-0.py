class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words_seen = {}
        for i, word in enumerate(strs):
            (words_seen.setdefault("".join(sorted(word)), [])).append(word)
            
        return list(words_seen.values())
            