import java.util.Scanner;
import java.lang.Math;
class test0 {

	public static int rc(int n) {          // Recursive cube:
		if (n==1) return 1;                  // with a base case of 1
		int sum = rc(n-1);                   // count down from x to 1
		return ((int) Math.pow(n,3) + sum);  // Add them all together as cubes
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Give us a number to cube: ");
		int s = in.nextInt();
		in.nextLine();

		System.out.println(rc(s));
	}
}
