import java.util.Scanner;
class Signel{
    public static void main(String args[]){
        Scanner d = new Scanner(System.in);
        String a = new String(d.nextLine());
        if("Red".equals(a))
        {
            System.out.println("Stop");
        }
        else if("Yellow".equals(a)){
            System.out.println("Get Ready");
        }
        else{
            System.out.println("GO..");
        }       
    }
}