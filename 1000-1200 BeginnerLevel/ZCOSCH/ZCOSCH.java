import java.lang.* ;
import java.util.Scanner ;

public class ZCOSCH{

  public static void main(String[] args){

    Scanner sc = new Scanner(System.in);
    int n;

    n = sc.nextInt() ; // takes input from the user 
    
    if ( (1<=n) & (n<=50) ) {
      System.out.println(100);
    }
    else if ( (51<=n) & (n<=100) ){
      System.out.println(50);
    }
    else {
      System.out.println(0);
    }
  }
}
   
