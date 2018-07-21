class Polygon():
    def __init__(self):
        self.list_of_points = []

    def addPoint(self, x, y):
        self.list_of_points.append([x, y])
        
    def dist(self, x1, y1, x2, y2):
        # distance(x,y) = sqrt((x1-x2)^2 + (y1-y2)^2)
        return (((x1-x2)**2 + (y1-y2)**2)**0.5)
    
    def perimeter(self):
        self.perimeter = 0.0
        for i in range(0, len(self.list_of_points)):
            x1 = self.list_of_points[i-1][0]
            x2 = self.list_of_points[i][0]
            y1 = self.list_of_points[i-1][1]
            y2 = self.list_of_points[i][1]
            self.perimeter = self.perimeter + self.dist(x1, x2, y1, y2)
            
        
            
        
        return self.perimeter
        
    def area(self):
        self.area = 0.0
        self.area1 = 0
        self.area2 = 0
        for i in range(0,len(self.list_of_points)):
            self.area1 += self.list_of_points [i][0] * self.list_of_points [i-1][1]
            
        for i in range(0,len(self.list_of_points)):
            self.area2 += self.list_of_points [i][1] * self.list_of_points [i-1][0]
            
        self.area = abs((self.area1 - self.area2)/2)
        return self.area
p = Polygon()
#p.addPoint (1.0,1.0)
#p.addPoint (5.0,1.0)
#p.addPoint (1.0,5.0)
#p.addPoint (5.0,5.0)
p.addPoint (1.0, 1.0)
p.addPoint (5.0,1.0)
p.addPoint (5.0,5.0)
p.addPoint (1.0,5.0)

print(p.area())