import java.util.Scanner;
class Mid{
    public static void main(String args[]){
        System.out.println("Enter the range");
        Scanner a = new Scanner(System.in);
        int e = a.nextInt();
        int[] b = new int[e];
        int  c= b.length/2;
        for(int d=0;d<e;d=d+1){
            b[d]=a.nextInt();
        }
        int f=b.length%2;
        System.out.println(f);
        if(f==0){
            System.out.println("Given range is odd:");
            System.out.println(b[(c-1)]+" "+b[c]);
        }
        else{
            System.out.println("Center of the given num="+b[c]);
        }
    }
}