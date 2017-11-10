import java.util.Scanner;

class test1{

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int x = 1;
		int y = 0;
		System.out.print("Give me a number to illustrate n(n+1)/2 : ");
		int r = in.nextInt();
		y = r;
		in.nextLine();
		for ( int i = 0; i < r/2; i++){
			if (y == r) System.out.println((i+1) + " : " + (y/2) + " + " + y--);
			else System.out.println((i+1) + " : " + x++ + " + " + y--);
		}

		System.out.println("So we have "+(r/2)+"*"+r+"+"+(r/2)+" in "+(r/2)+" steps.");
		System.out.println("If "+(r/2)+" = "+r+"/2, and "+(r/2)+"*"+r+"+"+(r/2));
		System.out.println("We then get "+r+"*"+r+"/2 +"+r+"/2");
		System.out.println("A.K.A. ("+r+"*"+r+"+"+r+")/2, or "+r+"("+r+"+1)/2");
		System.out.println("n(n+1)/2 WORKS, BABY!");

	}
}
