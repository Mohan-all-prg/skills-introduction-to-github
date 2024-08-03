class Tv{
    String Model="";
    String Brand="";
    int Price=0;
    int Tax=0;

    public static void main(String args[]){
        Tv seller1 = new Tv();

        seller1.Model="AMD a6";
        seller1.Brand="Lenova";
        seller1.Price=20000;
        seller1.Tax=500;

        Tv seller2 = new Tv();

        seller2.Model="AMD a7";
        seller2.Brand="Lenova";
        seller2.Price=30000;
        seller2.Tax=600;

        System.out.println(seller1.Price);
    }
}