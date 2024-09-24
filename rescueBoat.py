class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        boat = 0
        l = 0
        r = len(people)-1
        while l <= r:
            if people[l] + people[r] <=limit:
                l+=1
            r-=1
            boat +=1
        return boat       