import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
	static boolean[][] check;
	static boolean[] visit;
	static Queue<Integer> queue = new LinkedList<Integer>();
    static ArrayList[] lists;
	public int solution(int n, int[][] computers) {
		check = new boolean[n][n];
		visit = new boolean[n];
		
		lists = new ArrayList[n];
		for (int i = 0; i < n; i++) {
			lists[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if(i == j) continue;
				if(computers[i][j] == 1)	lists[i].add(j);
			} 
		}
        int answer = 0;
        
       
        return bfs(n,answer);
    }
	
	static int bfs(int n,int answer) {
		for (int i = 0; i < n; i++) {
			if(visit[i]) continue;
			queue.offer(i);
			while(!queue.isEmpty()) {
				int a = queue.poll();
				visit[a] = true;
				for (int j = 0; j < lists[a].size(); j++) {
					if(visit[(int)lists[a].get(j)]) continue;
					check[i][(int)lists[a].get(j)] = true;
					
					if(check[i][(int) lists[a].get(j)] && check[(int) lists[a].get(j)][i]) {
						visit[(int) lists[a].get(j)] = true;
						continue;
					}
					queue.offer((int) lists[a].get(j));
				}
			}
			answer++;
		}
		return answer;
	}
}
//
