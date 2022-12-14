from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    perimeter = 0                                               
    for i in range(len(grid)):                                  
        for j in range(len(grid[0])):                           
            if(grid[i][j] == 1):                                
                if(i-1 < 0 or grid[i-1][j] != 1):               
                                                                
                    perimeter += 1                              
                if(i+1 > len(grid)-1  or grid[i+1][j] != 1):    
                                                                
                    perimeter += 1                              
                if(j-1 < 0 or grid[i][j-1] != 1):               
                    perimeter += 1                              
                if(j+1 > len(grid[0])-1  or grid[i][j+1] != 1): 
                                                                
                    perimeter += 1                              
    return perimeter  