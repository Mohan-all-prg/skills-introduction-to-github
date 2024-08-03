class loop{
    public static void main(String args[]){
        int n=0;
        for(int i=1;i<=10;i=i+1){
            if(i%2==0){
                System.out.println("Even num="+i);
            }
            else{
                System.out.println("Odd num="+i);
                n=n+1;
            }
        }
        System.out.println("total odd num="+n);
    }
}