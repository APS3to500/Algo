import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		int[] in = new int[T+1];
		int[] time = new int[T+1];
		int[] time_after = new int[T+1];
		Queue<Integer> q = new LinkedList<Integer>();
		ArrayList<Integer>[] list = new ArrayList[T+1];
		
		for (int i = 0; i < list.length; i++) {
			list[i] = new ArrayList<Integer>();
		}
		
		for (int i = 1; i <= T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			time[i] = Integer.parseInt(st.nextToken());
			while(true) {
				int a=  Integer.parseInt(st.nextToken());
				if(a == -1) break;
				list[a].add(i);
				in[i]++;
			}
			
		}
		for (int i = 1; i < in.length; i++) {
			if(in[i] == 0) {
				q.offer(i);
			}
		}
		
		for (int i = 1; i < list.length; i++) {
			System.out.println(list[i]);
		}
		
		
		// 위상정렬 start
		
		while(!q.isEmpty()) {
			// 초기 time_after = 0
			int now = q.poll();
			for (int next : list[now]) { // 2,3,4
				// next : 3
				time_after[next] = Math.max(time_after[next], time_after[now] + time[now]);
				//time_after[3] = 10; , [4] = 10 ,[2] = 10;
				
				/*
				 now = 3 (4,5)
				 time_after[4] = max(10,4+10) == 14
				 
				 
				 */
				in[next]--; 
				if(in[next] == 0) q.offer(next); // 2,3 이 들어감
			}
		}
		
		for (int i = 1; i <= T; i++) {
			System.out.println(time[i] + time_after[i]);
		}
}

}
