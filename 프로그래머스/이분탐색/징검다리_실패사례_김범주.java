import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_잘못품_포기 {
	static int distance,n,rockq,answer;
	static int[] rocks,tgt; // 돌의 위치가 적힌 배열, tgt : 다리에서 제외될 돌의 위치가 기록될 배열
	static boolean[] del; // 제외된 돌을 기록하는 배열
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		distance = Integer.parseInt(br.readLine());
		rockq = Integer.parseInt(br.readLine());
		rocks = new int[rockq+2]; // 0 : 시작 위치, 1~rockq : 돌의 위치 , rockq : 최종 도착 위치
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= rockq; i++) {
			rocks[i] = Integer.parseInt(st.nextToken());
		}
		rocks[rockq+1] = distance;
		Arrays.sort(rocks);
		n = Integer.parseInt(br.readLine());
		tgt = new int[n];
		comb(0,0);
		
		System.out.println(answer);
	}
	
	static void comb(int tgtIdx,int srcIdx) {
		if(tgtIdx == n) { // 제거할 바위의 위치를 다 기억했다면
			del = new boolean[rockq+2];
			for (int i = 0; i < tgt.length; i++) {
				del[tgt[i]] = true;
			}
			System.out.println(Arrays.toString(tgt));
			move(tgt);
			return;
		}
		for (int i = srcIdx; i < rocks.length; i++) {
			if(i == 0 || i == rocks.length-1) continue;
			tgt[tgtIdx] = i;
			comb(tgtIdx+1,i+1);
 		}
	}
	
	static void move(int[] tgt) {
		int pos = 0; // 초기 위치
		int mindist = Integer.MAX_VALUE; // 다리를 다 건넜을 때 거리 최솟값
		//현재 위치에서 목표 지점까지의 각 거리를 구함
		for (int i = 0; i < rocks.length-1; i++) {
			pos = rocks[i]; //시작 위치를 기록
			//만약 이동하게될 위치의 돌이 없으면(del true) => 다음 돌로 이동해야함.
			do
			{
				i++;	
			} while(del[i] && i < rocks.length);
			
			pos = Math.abs(pos-rocks[i]);
			mindist = Math.min(mindist, pos);
			System.out.println("최소 거리  : "+mindist);
//			while(del[i]) { // 같은 위치의 돌을 봐서도 안됨
//				i++;
//			}
		}
		answer = Math.max(answer, mindist);
	}
}
