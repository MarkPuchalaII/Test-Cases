import java.util.Scanner;
import java.lang.Math;
class test0 {

	public static int rs(int r, int n) {   // Recursive r^2^n
		if (n==1) return r*r;                // square r for the base case
		int sum = rs(r*r, n-1);              // then square our RESULT with each call
		return (sum);                        // because r^2^2 is not the same as (r^2)^2
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("this is r^2^n. Give us r & n: ");
		int r = in.nextInt();
		int n = in.nextInt();
		in.nextLine();

		System.out.println(r+"^2^"+n+" : "+ rs(r, n));
	}
}
