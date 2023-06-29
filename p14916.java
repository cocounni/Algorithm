import java.util.*;

public class p14916 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count_coin = 0;

        // List<Integer> coin = new ArrayList<Integer>(Arrays.asList(2, 5));

        // for (Integer e : coin) {
        //    count_coin += N / e;
        //    money = N % e;
        // }
        // if (count_coin == 0) {
        //     System.out.println(-1);
        // }
        // else {
        //     System.out.println(count_coin);
        // }

        while (N > 0) {
			//5로 나뉘는 경우
			if (N % 5 == 0) {
				count_coin = N / 5 + count_coin;
				break;
			}
			
			//5로 나뉘지 않으면 2씩 빼기
			N -= 2;
			count_coin++;
		}
		
		if (N < 0) {
			System.out.println(-1);
		}
        else {
			System.out.println(count_coin);
		}

    }
} 