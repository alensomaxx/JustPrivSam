import java.util.Scanner;
import java.io.*;

class Main{
    public static void main(String args[]){

        try{
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String nameBuffered = reader.readLine();
            String ageBufferedStr = reader.readLine();
            int ageBuffered = Integer.parseInt(ageBufferedStr);

            System.out.println("BufferedReader name-" + nameBuffered + " Age: "+ ageBuffered);
        }catch (Exception e){
            System.out.println("An Error occurred: " + e.getMessage());
        }
    }
}