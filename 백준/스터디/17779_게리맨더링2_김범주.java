import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N,x,y,d1,d2,total, min = Integer.MAX_VALUE;
	static int[][] ar;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 구역을 5개 선거구로 나눠야 함
		// 각 구역은 5개의 선거구 중 하나에 포함되어야만 함
		// 각 선거구는 최소 하나의 구역을 포함해야 함.
		// 한 선거구에 있는 구역은 모두 연결되어야 함(구역 A에서 인접한 구역을 통해 구역 B로 이동 가능 : A와 B는 연결)
		// 인접 구역은 0개 이상
		
		/*
		 기준점 (x,y)와 경계의 길이 (d1,d2)를 정함
		 */
		N = Integer.parseInt(br.readLine());
		ar = new int[N][N];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				ar[i][j] = Integer.parseInt(st.nextToken());
				total += ar[i][j];
				//구역 (i,j)의 인구수눈 ar[i][j]
			}
		}
		
		/*
	 	N과 배열이 주어지고, 그 배열 안에서 모든 걸 구현해야 함
		 */
		// x : 세로, y : 가로
		// d1,d2,x,y가 정해진 후 그 안에서 영역표시 진행
		 for (int x = 0; x < N; x++) {
	            for (int y = 0; y < N; y++) {
	                for (int d1 = 1; d1 < N; d1++) {
	                    for (int d2 = 1; d2 < N; d2++) {
	                        if (x + d1 + d2 >= N) continue;
	                        if (y - d1 < 0 || y + d2 >= N) continue;

	                        bfs(d1, d2, x, y);
	                    }
	                }
	            }
	        }
		System.out.println(min);
		
	}

	static void bfs(int d1,int d2,int x,int y) {
		boolean[][] board = new boolean[N][N];
		
		for (int i = 0; i <= d1; i++) {
			board[x+i][y-i] = true;
			board[x+d2+i][y+d2-i] = true;
		}
		
		for (int i = 0; i <= d2; i++) {
			board[x+i][y+i] = true;
			board[x+d1+i][y-d1+i] = true;
		}
		
		int[] peoples = new int[5];
		
		// 1 구역 인구수
        for (int i = 0; i < x + d1; i++) {
            for (int j = 0; j <= y; j++) {
                if (board[i][j]) break;
                peoples[0] += ar[i][j];
            }
        }

        // 2 구역 인구수
        for (int i = 0; i <= x + d2; i++) {
            for (int j = N - 1; j > y; j--) {
                if (board[i][j]) break;
                peoples[1] += ar[i][j];
            }
        }

        // 3 구역 인구수
        for (int i = x + d1; i < N; i++) {
            for (int j = 0; j < y - d1 + d2; j++) {
                if (board[i][j]) break;
                peoples[2] += ar[i][j];
            }
        }

        // 4 구역 인구수
        for (int i = x + d2 + 1; i < N; i++) {
            for (int j = N - 1; j >= y - d1 + d2; j--) {
                if (board[i][j]) break;
                peoples[3] += ar[i][j];
            }
        }

        // 5 구역 인구수
        peoples[4] = total;

        for (int i = 0; i < 4; i++) {
            peoples[4] -= peoples[i];
        }

        // 정렬
        Arrays.sort(peoples);

        // 최대 - 최소
        min = Math.min(min, peoples[4] - peoples[0]);
	}
}
