import java.util.LinkedList;
import java.util.Queue;

class Solution {
	static boolean[] num;
	static boolean[][] graph;
	static Queue<node> queue = new LinkedList<node>();
    static int[] depth;
    static int maxdep;
	public int solution(int n, int[][] edge) {
    	
    	graph = new boolean[n+1][n+1];
    	num = new boolean[n+1];
    	depth = new int[n+1];
    	for (int i = 0; i < edge.length; i++) {
			graph[edge[i][0]][edge[i][1]] = true;
			graph[edge[i][1]][edge[i][0]] = true;
		}
    	bfs(n);
        int answer = 0;
        answer = depth[maxdep];
        return answer;
    }
    
    static void bfs(int n) {
    	queue.offer(new node(1,0));
    	num[1] = true;
    	while(!queue.isEmpty()) {
    		node val = queue.poll();
    		maxdep = Math.max(maxdep, val.d);
    		for (int i = 1; i <= n; i++) {
				if(i == val.n) continue;
				if(graph[val.n][i] && !num[i]) {
					queue.offer(new node(i,val.d+1));
					num[i] = true;
					depth[val.d+1]++;
				}
				
			}
    	}
    }
    
    static class node {
    	int n;
    	int d;
		public node(int n, int d) {
			super();
			this.n = n;
			this.d = d;
		}
    	
    }
}
