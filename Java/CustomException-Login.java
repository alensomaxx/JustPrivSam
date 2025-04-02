// You are using Java
class InvalidLoginException extends Exception{
    public InvalidLoginException(String message){
        super (message);
    }
}
class CustomExceptionExample{
    public static void login(String username, String password) throws InvalidLoginException{
        if (username.equals("admin") && password.equals("1234")){
            throw new InvalidLoginException("Invalid username or password!");
        }
        System.out.println("Login Successful!");
    }
    
    public static void main(String[] args){
        try{
            login("user", "wrongpass");
            login("admin", "1234");
        } catch (InvalidLoginException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}