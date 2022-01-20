import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
    	ArrayList<Integer> answer = new ArrayList<Integer>();
    	
        for(int i = 0; i < commands.length; i++) { // 첫 반복문
            int[] ar = new int[array[commands[i][1]]-array[commands[i][0]]+1]; // i번마다 새로운 배열 만들기
            for (int j = 0; j < ar.length; j++) {
				ar[j] = array[commands[i][0]-1+j]; // 배열 원소 채우기
			}
            Arrays.sort(ar); // 내용을 다 채워낸 원소를 정렬
            answer.add(ar[commands[i][2]-1]); // 정렬된 배열에서 n번째 원소를 수집하기 0부터 시작
        }
        int[] answers = new int[answer.size()+1]; // 정답을 내기 위한 원소
        for (int i = 0; i < answer.size(); i++) {
			answers[i] = answer.get(i);
		}
        return answers;
    }
}
