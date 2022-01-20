import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        
        for (int i = 0; i < 10001; i++) {
        	int cnt = 0;
			for (int j = citations.length-1; j >= 0; j--) {
				if(i > citations[j]) break;
				cnt++;
			}
			if(i > cnt) {
				answer = i-1;
				break;
			}
		}
        return answer;
    }
}
