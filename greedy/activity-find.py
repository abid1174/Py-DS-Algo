
class Solution:
    
    def sortActivity(self,n, start, end):
        activities = [ (start[i], end[i]) for i in range(n)]
        return sorted(activities, key = lambda x: x[1])
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        activities = self.sortActivity(n, start, end)
        
        s = []
        e = []
        for item in activities:
            s.append(item[0])
            e.append(item[1])
        
        a = 1
        i = 0
        
        for j in range(1, n):
            if s[j] > e[i]:
                a += 1
                i = j
            
        return a
