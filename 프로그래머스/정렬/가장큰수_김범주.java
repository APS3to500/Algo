import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] ar = new String[numbers.length];
        
        for (int i = 0; i < ar.length; i++) {
			ar[i] = String.valueOf(numbers[i]);
		}
        
        // 정렬 진행
        Arrays.sort(ar, new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				// TODO Auto-generated method stub
				return ((o2 + o1).compareTo(o1+o2));
			}
        	
        });
        
        //0만 여러개 있는 원소의 경우, 하나의 0만 리턴하게 만들어야 함!
        if(ar[0].equals("0")) {
        	return "0";
        }
        
        for (String a : ar) {
			answer += a;
		}
        return answer;
    }
}
