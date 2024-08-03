class This{
    int a;
    void get(int a){
        this.a=a;
    }
    public static void main(String args[]){
        This b = new This();
        b.get(20);
        System.out.println(b.a);
    }
}