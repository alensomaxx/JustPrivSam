//full code of Java for Input File

import java.io.*;
import java.lang.*;

class Main{
    public static void main(String[] args){
        copyUsingCharStream("input.txt", "output_char.txt");
        copyUsingByteStream("input.txt", "output_char.txt");
    }
    public static void copyUsingCharStream(String input, String output){
        try (FileReader reader = new FileReader(input);
        FileWriter writer = new FileWriter(output)){
            int ch;
            while ((ch = reader.read()) != -1){
                writer.write(ch);
            }
        }
        catch (Exception e){
            System.out.println("Character stream error: "+ e.getMessage());
        }
    }
    public static void copyUsingByteStream(String input, String output){
        try (FileInputStream in = new FileInputStream(input);
        FileOutputStream out = new FileOutputStream(output)){
            int b;
            while ((b = in.read()) != -1){
                out.write(b);
            }
        }
        catch (Exception e){
            System.out.println("Byte stream error: " + e.getMessage());
        }
    }
}