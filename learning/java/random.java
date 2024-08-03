import java.util.Random;
class Ran{
    public static void main(String args[]){
        Random a = new Random();
        int b = 0;
        while(b!=10){
            b = a.nextInt(11);
            System.out.println(b);
        }
    }
}