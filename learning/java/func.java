class Mobiles{
    void iphone(){
        System.out.println("I have iphone");
        moto();
        samsung();
        redmi();
    }
    void moto(){
        System.out.println("I have Moto");
    }
    void samsung(){
        System.out.println("I have Samsung");
    }
    void redmi(){
        System.out.println("I have Redmi");
    }
    public static void main(String args[]){
        Mobiles a = new Mobiles();
        a.iphone();
    }
}