import java.util.ArrayList;

class Solution {
	static ArrayList<int[]> list = new ArrayList<int[]>();
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int a = yellow;
		for (int i = 1; i <= a; i++) {
			if(a % i == 0 && a/i >= i) {
				list.add(new int[] {a/i,i});
			}
		}
		answer[0] = list.get(list.size()-1)[0]+2;
		answer[1] = list.get(list.size()-1)[1]+2;
        return answer;
    }
}
