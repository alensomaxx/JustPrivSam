import java.io.*;
import java.io.IOException;

class Main { 
    public static void main(String args[]) {
        File file = new File("demo.txt");

        try {
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            } else {
                System.out.println("File already exists.");
            }
            System.out.println("Absolute path: " + file.getAbsolutePath());
            System.out.println("File Name: " + file.getName());
            System.out.println("Parent file: " + file.getParent());
            System.out.println("Parent Directory: " + file.getParent());
            System.out.println("Path: " + file.getPath());
            System.out.println("can Read: " + file.canRead());
            System.out.println("can write: " + file.canWrite());
            System.out.println("Is Directory: " + file.isDirectory());
            System.out.println("File Size: " + file.length());
        } catch (IOException e) {
            System.out.println("An error occurred while creating or accessing the file: " + e.getMessage());
            return;
        }

        
        if (file.exists()) {
            if (file.delete()) {
                System.out.println("File Deleted");
            } else {
                System.out.println("Failed to delete the file.");
            }
        } else {
            System.out.println("File does not exist, cannot delete."); 
        }
    }
}