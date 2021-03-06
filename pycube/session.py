import statistics

class Session:
    
    def __init__(self, datastring=None):
        if not datastring:
            self.data = []
            self.num_items = 0
        else:
            self.data = [entry.split(';') for entry in datastring.split('\n') if len(entry) > 0]
            self.num_items = len(self.data)
            
            for r in range(len(self.data)):
                for c in range(1, 6):
                    try:
                        self.data[r][c] = float(self.data[r][c])
                    except ValueError:
                        continue
    
    def addtime(self, time, penalty, scramblestring):
        self.num_items += 1
        num_items_hex = hex(self.num_items)[2:].upper()
        id = 'I'
        if len(num_items_hex) < 3:
            id += '0'
            if len(num_items_hex) < 2:
                id += '0'
                id += num_items_hex
            else:
                id += num_items_hex
        else:
            id += num_items_hex
        
        entry = [id, time]
        entry = self.calcstats(entry)
        
        entry.append(scramblestring)
        self.data.append(entry)
    
    # This is kinda ugly, might fix up later
    def calcstats(self, entry=None):
        times = [self.data[i][1] for i in range(len(self.data))]
        if entry:
            times.append(entry[1])
        else:
            entry = [self.data[-1][0], self.data[-1][1]]
        
        # Calculate average of 5
        if len(times) >= 5:
            last5 = times[-5:]
            if "DNF" in last5:
                last5.remove("DNF")
                if "DNF" in last5:
                    entry.append("")
            else:
                last5.remove(max(last5))
            last5.remove(min(last5))
            entry.append(float("%.3f" % (sum(last5) / 3)))
        else:
            entry.append("DNF")
            
        # Calculate average of 12
        if len(times) >= 12:
            last12 = times[-12:]
            if "DNF" in last12:
                last12.remove("DNF")
                if "DNF" in last12:
                    entry.append("")
            else:
                last12.remove(max(last12))
            last12.remove(min(last12))
            entry.append(float("%.3f" % (sum(last12) / 3)))
        else:
            entry.append("DNF")
            
        # Calculate session mean
        if "DNF" in times:
            times.remove("DNF")
        entry.append(float("%.3f" % (sum(times) / len(times))))
        
        # Calculate standard deviation
        if len(times) >= 2:
            entry.append(float("%.3f" % statistics.stdev(times)))
        else:
            entry.append("")
        
        # Append penalty; 0 for none, 1 for +2, 2 for DNF
        entry.append(0)
        
        return entry
        
    def removetime(self, id):
        del self.data[self.getidindex(id)]
    
    def getidindex(self, id):
        for i in range(len(self.data)):
            if self.data[i][0] == id:
                return i
    
    def getlastitemid(self):
        return self.data[-1][0]
    
    def clear(self):
        self.data = []
        
    def __str__(self):
        s = ""
        for i in range(len(self.data)):
            s += ';'.join([str(value) for value in self.data[i]]) + '\n'
        return s