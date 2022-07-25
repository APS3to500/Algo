package prob_나만안되는연애_14621_220712;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] parents;
	static edge[] edgelist;
	static int V,E;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		
		edgelist = new edge[E];
		char[] gender_list = new char[V+1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < gender_list.length; i++) {
			char g = st.nextToken().charAt(0);
			gender_list[i] = g;
		}
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			edgelist[i] = new edge(start,end,weight);
		}
		Arrays.sort(edgelist);
		make();
		int cnt = 0;
		int result = 0;
		
		for (int i = 0; i < edgelist.length; i++) {
			edge e = edgelist[i];
			if(gender_list[e.start] == gender_list[e.end]) continue;
			if(union(e.start,e.end)) {
				result += e.weight;
				if(++cnt == V-1) break;
			}
		}
		if(cnt < V-1) {
			result = -1;
		}
		System.out.println(result);
	}
	static class edge implements Comparable<edge>{
		int start;
		int end;
		int weight;
		public edge(int start, int end, int weight) {
			super();
			this.start = start;
			this.end = end;
			this.weight = weight;
		}
		@Override
		public int compareTo(edge o) {
			// TODO Auto-generated method stub
			return this.weight-o.weight;
		}
	}
	
	static void make() {
		parents = new int[V+1];
		for (int i = 1; i <= V; i++) {
			parents[i] = i;
		}
	}
	
	static int find(int a) {
		if(parents[a] == a) return a;
		return parents[a] = find(parents[a]);
	}
	
	static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		if(aRoot == bRoot) return false;
		
		parents[bRoot] = aRoot;
		return true;
	}
}
