class Constructor{
    int b;
    String c;
    Constructor(int d,String e){
        b=d;
        c=e;
    }
    public static void main(String args[]){
        Constructor a = new Constructor(40,"Mohan");
        Constructor b = new Constructor(50,"Kumar");
        System.out.println(b.b);
        System.out.println(a.c);
    }
}