class Solution(object):
    def commonChars(self, words):
        answer = list(words[0])  
        for i in words[1:]:
            x = [] 
            for letter in answer:
                if letter in i:
                    x.append(letter) 
                    i = i.replace(letter, '', 1) 
            answer = x  
        
        return answer 