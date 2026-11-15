class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # list_word = []
        # for index in range(len(words)):
        #     if x in words[index]:
        #         list_word.append(index)
        # return list_word 
        return [i for i in range(len(words)) if x in words[i]]
