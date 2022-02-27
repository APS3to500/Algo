import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int[] dy = {0,-1,1,0,0};
	static int[] dx = {0,0,0,1,-1};
	static int R,C,M,ans;
	static ArrayList<shark>[][] ar;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		if(M == 0) {
			System.out.println(0);
			return;
		}
		ar = new ArrayList[R+1][C+1];
		for (int i = 1; i <= R; i++) {
			for (int j = 1; j <= C; j++) {
				ar[i][j] = new ArrayList<shark>();
			}
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken()); 
			int z = Integer.parseInt(st.nextToken()); 
			
			ar[r][c].add(new shark(s,d,z,false));
		}
		
		for (int i = 1; i <= C; i++) { 

			for (int j = 1; j <= R; j++) {
				if(ar[j][i].size() > 0) { 
					ans += ar[j][i].get(0).z; 
					ar[j][i].remove(0);
					break;
				}
			}
			for (int j = 1; j <= R; j++) {
				for (int k = 1; k <= C; k++) {
					if(ar[j][k].size() > 0 && !ar[j][k].get(0).moved) {
						shark sh = ar[j][k].get(0);
						sh.moved = false;
						ar[j][k].remove(0);
						int dist = sh.s;
						int r = j;
						int c = k;
						int my = dy[sh.d];
						int mx = dx[sh.d];
						while(dist > 0) {
							if(r <= 1 | r >= R || c <= 1 || c >= C) {
								if(r <= 1 && sh.d ==1) 	sh.d = 2; 
								else if(r >= R && sh.d == 2) sh.d = 1; 
								else if(c <= 1 && sh.d == 4) sh.d = 3; 
								else if(c >= C && sh.d == 3) sh.d = 4; 
								
								my = dy[sh.d];
								mx = dx[sh.d];
							}
							r += my;
							c += mx;
							dist--;
						}
						ar[r][c].add(new shark(sh.s,sh.d,sh.z,true));
					}
				}
			}
			for (int j = 1; j <= R; j++) {
				for (int k = 1; k <= C; k++) {
						if(ar[j][k].size() >0) {
							int maxsize = 0;
							int maxdist = 0;
							int dir = 0;
							
							for (int q = 0; q < ar[j][k].size(); q++) {
								if(maxsize < ar[j][k].get(q).z) {
									maxsize = ar[j][k].get(q).z;
									maxdist = ar[j][k].get(q).s;
									dir = ar[j][k].get(q).d;
								}
							}
							ar[j][k].clear();
							ar[j][k].add(new shark(maxdist,dir,maxsize,false));
							
						}
				}
			}
			 
		}
		System.out.println(ans);
	}
	static class shark {

		int s; 
		int d; 
		int z; 
		boolean moved;

		public shark(int s, int d, int z, boolean moved) {
			super();
			this.s = s;
			this.d = d;
			this.z = z;
			this.moved = moved;
		}

		@Override
		public String toString() {
			return "shark [s=" + s + ", d=" + d + ", z=" + z + ", moved=" + moved + "]";
		}
	}
}
//1차 수정
