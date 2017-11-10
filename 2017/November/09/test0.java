class test0 {


	public static void main(String[] args) {
		int x = 0;
		for (int i = 1; i < 100; i++){
			int j = (i-2 > 0) ? i-2 : 1;
			System.out.println(i + " players : " + x + " games : " + ((i-1)*j)+" wins per player");
			x += i;
		}
	}
}
