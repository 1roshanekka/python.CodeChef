import java.lang.*;
import java.util.*;

class CountingWords{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        //initializing Variables and array
        int i,j = 0;
        int arr[] = new int[T];

        for(i=0;i<T;i++){
            Scanner data = new Scanner(System.in);
            /*  N is the number of pages
                M is the number of words on a page */
            int N = data.nextInt();
            int M = data.nextInt();
            arr[i] = M*N;
        }
        
        for(j=0;j<T;j++){
            System.out.println(arr);
        }
    }
}