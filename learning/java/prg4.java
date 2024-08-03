import java.util.Scanner;
class Bank{
    public static void main(String args[]){
        System.out.println("Enter you salary and Age:");
        Scanner a = new Scanner(System.in);
        System.out.println("Enter your salary=");
        int b =a.nextInt();
        System.out.println("Enter your Age=");
        int c =a.nextInt();
        System.out.println("Enter your loan amount=");
        int d =a.nextInt();
        if(b>=20000 && c<=25){
            if(d<=50000){
                System.out.println("Your eligible for loan");
            }
            else{
                System.out.println("Max loan amount is 50000");
            }
        }
        else{
            System.out.print("Your not eligible for loan");
        }
    }
}