class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start_color = image[sr][sc]
        
        def visit(x, y):
            if x<0 or x>=len(image):
                return
            if y<0 or y>=len(image[0]):
                return
            
            if image[x][y] == color:
                return
            if image[x][y] != start_color:
                return
            
            image[x][y] = color
            
            visit(x+1, y)
            visit(x-1, y)
            visit(x, y+1)
            visit(x, y-1)
            
        visit(sr, sc)
        return image
        