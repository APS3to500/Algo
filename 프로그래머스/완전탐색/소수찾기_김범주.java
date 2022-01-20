import java.util.ArrayList;
class Solution {
    static ArrayList<Integer> list = new ArrayList<Integer>();
	static int[] ar,tgt;
	static boolean[] num = new boolean[10000001];
	static boolean[] selected;
    public int solution(String numbers) {
        int answer = 0;
        
        String[] str = numbers.split("");
		ar = new int[str.length];
		selected = new boolean[ar.length];
		for (int i = 0; i < str.length; i++) {
			ar[i] = Integer.parseInt(str[i]);
		}
		for (int i = 1; i <= str.length; i++) {
			tgt = new int[i];
			perm(0,i);
		}
		
		//에라토스테네스의 체
		num[0] = num[1] = true;
		for (int i = 2; i*i <= 10000000; i++) {
			if(!num[i]) {
				for (int j = i*i; j <= 10000000; j+=i) {
					num[j] = true;
				}
			}
		}
		
		for (Integer a : list) {
			if(!num[a]) answer++;
		}
        
        return answer;
    }
    
    	static void perm(int tgtIdx,int size) {
			if(tgtIdx == size) {
				int sum = 0;
				for (int i = 0; i < tgt.length; i++) {
					sum+= tgt[i]*Math.pow(10,tgt.length-1-i);
				}
				//에라토스테네스의 체를 활용
				if(!list.contains(sum)) {
					list.add(sum);
				}
				return;
			}
			for (int i = 0; i < ar.length; i++) {
				if(selected[i]) continue;
				if(tgtIdx == 0 && ar[i] < 1) continue;
				if(size == 1 && ar[i] == 1) continue;
				tgt[tgtIdx] = ar[i];
				selected[i] = true;
				perm(tgtIdx+1,size);
				selected[i] = false;
			}
		
	}
}
