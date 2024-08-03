import java.util.Scanner;
public class even{
    void solve(int a){
        if(a%2==0){
            System.out.println("Even");
        }
        else{
            System.out.println("Odd");
        }
    }
    public static void main(String args[]){
        Scanner b = new Scanner(System.in);
        int c = b.nextInt();
        even d = new even();
        d.solve(c);
    }
}