class Session:
    
    def __init__(self):
        self.times = []
        self.avg5 = []
        self.avg12 = []
        self.mean = []
    
    def addtime(self, time):
        self.times.append(time)
        
        # Calculate average of 5
        if len(self.times) >= 5:
            last5 = self.times[-5:]
            last5.remove(min(last5))
            last5.remove(max(last5))
            self.avg5.append(float("%.3f" % (sum(last5) / 3)))
        else:
            self.avg5.append(0)
            
        # Calculate average of 12
        if len(self.times) >= 12:
            last12 = self.times[-12:]
            last12.remove(min(last12))
            last12.remove(max(last12))
            self.avg12.append(float("%.3f" % (sum(last12) / 3)))
        else:
            self.avg12.append(0)
            
        # Calculate session mean
        self.mean.append(float("%.3f" % (sum(self.times) / len(self.times))))
    
    def removetime(self, index):
        del self.times[index]