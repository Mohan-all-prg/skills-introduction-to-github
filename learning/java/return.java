class Game{
    String name(){
        return "Mohan Kumar";
    }
    String num(){
        return "9123540963";
    }
    public static void main(String args[]){
        Game a = new Game();
        String c = a.name();
        String b = a.num();
        System.out.println("Name="+c);
        System.out.println("Phone Number="+b);
    }
}