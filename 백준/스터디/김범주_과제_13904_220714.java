package prob_과제_13904_220711;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main_정리 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		LinkedList<lecture> list = new LinkedList<lecture>();
		int score = 0;
		int term = 0;
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int d = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			list.add(new lecture(d,w));
			term = Math.max(term, d);
		}
		Collections.sort(list, new Comparator<lecture>() {
			@Override
			public int compare(lecture o1, lecture o2) { // [o1, o2]
				if(o1.d > o2.d) {
					return -1;
				}
				else if(o1.d == o2.d) {
					if(o1.w > o2.w) {
						return -1;
					}
				}
				return 0;
			}
		});
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
		while(term > 0) {
			for (int i = 0; i < list.size(); i++) {
				if(list.get(i).d != term) continue;
				if(list.get(i).d < term) break;
				pq.offer(list.get(i).w);
			}
			if(pq.size() > 0) {
				score += pq.poll();
			}
			--term;
		}
		System.out.println(score); 
	}
	static class lecture {
		int d;
		int w;
		public lecture(int d, int w) {
			super();
			this.d = d;
			this.w = w;
		}
	}
}
