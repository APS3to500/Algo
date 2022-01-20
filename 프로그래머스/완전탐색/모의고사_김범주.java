import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
    	int max = Integer.MIN_VALUE;
        int[] scores = new int[4];
        // 1 : 1,2,3,4,5,1,2,3,4,5,....
        // 2 : 2,1,2,3,2,4,2,5,2,1,....
        // 3 : 3,3,1,1,2,2,4,4,5,5,3,3,1,1,....
        int twocount = 1;
        for (int i = 1; i <= 3; i++) {
			for (int j = 0; j < answers.length; j++) {
				switch(i) {
				case 1 :
					if(answers[j] == j%5+1) scores[i]++;
					break;
				case 2 : 
					// 홀수번째 위치마다 2가 들어오는지 계산
					if(j % 2 == 0) {
						if(answers[j] == 2) scores[i]++;
					}
					else {
						if(answers[j] == twocount) scores[i]++;
						twocount++;
						if(twocount == 2) twocount++;
						if(twocount == 6) twocount = 1;
					}
					break;
				case 3 : //3,3,1,1,2,2,4,4,5,5의 순서로 진행
					if(j % 10 == 0 || j % 10 == 1) { // 3이 오면 정답
						if(answers[j] == 3) scores[i]++;
					}
					else if(j % 10 == 2 || j % 10 == 3) { // 1이 오면 정답
						if(answers[j] == 1) scores[i]++;
					}
					else if(j % 10 == 4 || j % 10 == 5) { // 2가 오면 정답
						if(answers[j] == 2) scores[i]++;
					}
					else if(j % 10 == 6 || j % 10 == 7) { // 4가 오면 정답
						if(answers[j] == 4) scores[i]++;
					}
					else if(j % 10 == 8 || j % 10 == 9) { // 5가 오면 정답
						if(answers[j] == 5) scores[i]++;
					}
					break;
				}
			}
			max = Math.max(max, scores[i]);
		}
        
        ArrayList<Integer> ar = new ArrayList<Integer>();
        if(max > 0) {
        	for (int i = 1; i < scores.length; i++) {
    			if(scores[i] == max) {
    				ar.add(i);
    			}
    		}
        }
        
        
        int[] answer = new int[ar.size()];
        for (int i = 0; i < answer.length; i++) {
			answer[i] = ar.get(i);
		}
        return answer;
    }
}
