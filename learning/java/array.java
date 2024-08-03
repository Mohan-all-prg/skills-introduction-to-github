import java.util.Scanner;
class Array{
    public static void main(String args[]){
        Scanner a = new Scanner(System.in);
        System.out.println("Enter the range:");
        int b = a.nextInt(); 
        int e=0;
        int[] d = new int[b];  
        for(int c=0;c<b;c=c+1){
            d[c]=a.nextInt();
            e=e+d[c];
        }
        System.out.println("The total num="+e);
    }
}