abstract class Stud{
    abstract void details();
}
class Name extends Stud{
    void details(){
        System.out.println("Name=Mohan");
    }
}
public class Abstract{
    public static void main(String args[]){
        Name a = new Name();
        a.details();
    }
}