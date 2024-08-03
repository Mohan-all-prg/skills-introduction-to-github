import java.util.Scanner;
class Add{
    public static void main(String args[]){
        Scanner c = new Scanner(System.in);
        int a = c.nextInt();
        int b = c.nextInt();
        if(a<b || a==b){
            System.out.println(b);
        }
        else{
            System.out.println(a);
        }
        c.nextLine();
        String d = new String(c.nextLine());
        String e = new String(c.nextLine());
        if(d.equals(e)){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        } 
        System.out.println(d==e); //here the str are in differnt place it take only the arg of str
    }
}