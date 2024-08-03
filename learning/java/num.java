class Num{
    void add(int a,int b){
        System.out.println("Addition="+(a+b));
        sub(a,b);
        mul(a,b);
        div(a,b);
    }
    void sub(int a,int b){
        System.out.println("Subraction="+(a-b));
    }
    void mul(int a,int b){
        System.out.println("Multiplication="+a*b);
    }
    void div(int a,int b){
        System.out.println("Devesion="+a/b);
    }
    public static void main(String args[]){
        Num start = new Num();
        start.add(5,3);
    }
}