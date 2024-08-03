import java.lang.System;
import java.util.Scanner;
class Name{
    public static void main(String args[]){
        Scanner a = new Scanner(System.in);
        String b = a.nextLine();
        int c = a.nextInt();
        a.nextLine(); //here we given this statement to get str when we need get input after a int
        String d = a.nextLine();
        double e=a.nextDouble();
        System.out.println("Name="+b);
        System.out.println("Age="+c);  
        System.out.println("Adderss="+d);
        System.out.println("my score="+e/10+"/10");
    }
}