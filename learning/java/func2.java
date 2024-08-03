class Garden{
    int price = 20;
    int count = 5;
    void Add(){
        System.out.println("total amount="+price*count);
    }
    public static void main(String args[]){
        Garden a = new Garden();
        a.Add();
    }
}