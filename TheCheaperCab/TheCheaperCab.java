import java.util.*;

class TheCheaperCab{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        //initializing variables and array
        String res[] = new String[T];

        for(int i = 0; i<T; i++){
            int X = sc.nextInt();
            int Y = sc.nextInt();

            if(X>Y){
                res[i] = "SECOND";
            }
            else if(Y>X){
                res[i] = "FIRST";
            }
            else if(X==Y){
                res[i] = "ANY";
            }
        }

        //printing result
        for(int j = 0; j<T; j++){
            System.out.println(res[j]);
        }
    }
}