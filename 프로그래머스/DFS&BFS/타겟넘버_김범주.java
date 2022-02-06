class Solution {
	static String[] cal = {"+","-"},tgt;
	static int numb;
    public int solution(int[] numbers, int target) {
        int answer = 0;
        tgt = new String[numbers.length];
        perm(0,target,numbers,numbers.length);
        answer = numb;
        return answer;
    }
    
    static void perm(int tgtIdx,int target,int[] numbers,int N) {
    	if(tgtIdx == N) {
    		int num = 0;
    		for (int i = 0; i < N; i++) {
				if(tgt[i].equals("-")) num -= numbers[i];
				else if(tgt[i].equals("+")) num += numbers[i];
			}
    		if(num == target) numb++;
    		return;
    	}
    	
    	for (int i = 0; i < cal.length; i++) {
			tgt[tgtIdx] = cal[i];
			perm(tgtIdx+1,target,numbers,N);
		}
    }
}
