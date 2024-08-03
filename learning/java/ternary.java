import java.util.Scanner;
class Ter{
    public static void main(String args[]){
        Scanner a = new Scanner(System.in);
        boolean rain= a.nextBoolean();
        String b = rain?"Take an umberla":"Enjoy the sun light";
        System.out.println(b);
        }
}