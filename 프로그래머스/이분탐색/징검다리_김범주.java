import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
    	Arrays.sort(rocks);
        int answer = 0;
        int start = 0;
        int end = distance;
        while(start <= end) {
        	int mid = (start + end)/2;
        	int prevpos = 0;
        	int removeCnt = 0;
        	for (int i = 0; i < rocks.length; i++) {
				if(Math.abs(prevpos-rocks[i]) < mid) {
					removeCnt++;
					if(removeCnt > n) {
						break;
					}
				}
				else {
					prevpos = rocks[i];
				}
			}
        	if(removeCnt > n) {
        		end = mid-1;
        	}
        	else {
        		answer = answer > mid ? answer : mid;
        		start = mid+1;
        	}
        }
        return answer;
    }
}
