import java.util.Scanner;
import java.lang.Math;
class test1 {

	public static int rm(int x, int y) {  //Recursive Multiplication!
		if (y==0) return 0;                 // with a base case of 0, 
		int sum = x + rm(x, y-1);           // count down from x to 0
		return (sum);                       //
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Give us two numbers to multiply: ");
		int x = in.nextInt();
		int y = in.nextInt();
		in.nextLine();

		System.out.println(rm(x, y));
	}
}
