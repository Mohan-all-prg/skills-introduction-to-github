import java.util.Scanner;
class Do{
    public static void main(String args[]){
        Scanner a = new Scanner(System.in);
        int b = 0;
        do{
            System.out.println("give the num which is greater then 10");
            b = a.nextInt();
        }while(b<10);
    }
}