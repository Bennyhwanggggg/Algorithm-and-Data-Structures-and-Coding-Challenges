class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        Queue<ArrayList<Integer>> q = new LinkedList<>();
        for(int a=0; a<grid.length; a++){
            for(int b=0; b<grid[0].length; b++){
                if (grid[a][b] == 1){
                    q.add(new ArrayList<Integer>(Arrays.asList(a, b)));
                }
                int area = 0;
                while(q.peek() != null){
                    List<Integer> curr = q.poll();
                    int i = curr.get(0);
                    int j = curr.get(1);
                    grid[i][j] = -1;
                    area += 1;
                    if (i-1>=0 && grid[i-1][j] == 1 && !q.contains(new ArrayList<Integer>(Arrays.asList(i-1, j)))){
                        q.add(new ArrayList<Integer>(Arrays.asList(i-1, j)));
                    }
                    if (i+1<grid.length && grid[i+1][j] == 1 && !q.contains(new ArrayList<Integer>(Arrays.asList(i+1, j)))){
                        q.add(new ArrayList<Integer>(Arrays.asList(i+1, j)));
                    }
                    if (j-1>=0 && grid[i][j-1] == 1 && !q.contains(new ArrayList<Integer>(Arrays.asList(i, j-1)))){
                        q.add(new ArrayList<Integer>(Arrays.asList(i, j-1)));
                    }
                    if (j+1<grid[0].length && grid[i][j+1] == 1 && !q.contains(new ArrayList<Integer>(Arrays.asList(i, j+1)))){
                        q.add(new ArrayList<Integer>(Arrays.asList(i, j+1)));
                    }
                }
                maxArea = Math.max(maxArea, area);
            }
        }
        return maxArea;
    }
}

class SolutionDFS {
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    max = Math.max(dfs(grid, i, j), max);
                }
            }
        }
        
        return max;
    }
    
    int dfs(int[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0) {
            return 0;
        }
        
        if (grid[i][j] == 1) {
            grid[i][j] = 999;
            return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1) ;
         }
        return 0;
    }
}