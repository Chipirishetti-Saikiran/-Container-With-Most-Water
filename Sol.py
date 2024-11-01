 def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        area=0 
        while i<j:
            area=max(area,min(height[i],height[j])*abs(i-j))
            if height[i]<height[j]:
                i=i+1 
            else:
                j=j-1 
        return area     
