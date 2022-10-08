class MedianFinder:
    def __init__(self):
        self.list = []
        self.count = 0
        self.left = -pow(10,5)
        self.right =pow(10,5)
        self.leftcount = 0
        self.rightcount = 0

    def addNum(self, temp):
        if len(self.list) >= 5*pow(10, 5):
            raise ValueError('The number of elements is more than 5*10^5')
        elif temp > pow(10, 5) or temp < -1 * pow(10, 5):
            raise ValueError('The entered value'+str(temp)+' < −10^5 or > 10^5')
        self.list.append(temp)
        self.count = self.count + 1
    
    def find_median(self): 
        if len(self.list)==0:
            return .0
        elif len(self.list)==1:
            return self.list[0] 
        elif self.list[0]<self.list[1]:
            self.left=self.list[0]
            self.right=self.list[1]
        else:
            self.left=self.list[1]
            self.right=self.list[0]
        if len(self.list)==2:
            return (self.left+self.right)/2
        for i in range(2,len(self.list),1):
            if self.list[i] > pow(10, 5) or self.list[i] < -1 * pow(10, 5):
               raise ValueError('The entered value'+ str(self.list(i))+ ' < −10^5 or > 10^5')
            if self.list[i] <=self.left:
                self.leftcount+=1
            elif self.list[i]<=(self.left+self.right)/2:
                self.left = self.list[i]
            
            elif self.list[i]<self.right:
                self.right = self.list[i]
                
            elif self.list[i] >=self.right:
                self.rightcount+=1
        if self.leftcount==self.rightcount:
            return (self.left+self.right)/2
        elif self.leftcount > self.rightcount:
            return self.left
        else:
            return self.right

median_finder = MedianFinder()
assert median_finder.find_median() == .0

median_finder.addNum(1)
median_finder.addNum(2)
assert median_finder.find_median() == 1.5

median_finder.addNum(3)
assert median_finder.find_median() == 2.
        
        
            
            

