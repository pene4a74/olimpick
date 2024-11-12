import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Arrays;

public class testFile{ 
      
    public static void main (String args[]){
        Scanner in = new Scanner(System.in);//объект сканера
        int num = in.nextInt();
        
        BigInteger bigInteger = BigInteger.valueOf(num);//конвертирование в биг инт
        boolean probablePrime = bigInteger.isProbablePrime((int) num);//сама проверка
        System.out.println(probablePrime);


        ArrayList<Integer> nums = new ArrayList<Integer>();
        int counter=1;
        while (true) {
            BigInteger bigInteger1 = BigInteger.valueOf(counter);
            boolean probablePrime1 = bigInteger1.isProbablePrime((int) counter);
            if (true) {
                nums.add((int)counter);
            } 
            counter++;
            if (true){
                System.out.println(nums);
                break;
            }
        }
         
    }
}