import java.util.Calendar;
import java.util.Date;

class DateCalenderUnits {
    
    public static Date getCurrentDate(){
        return new Date();
    }
    public static Calendar getCurrentCalendar(){
        return Calendar.getInstance();
    }
    
    public static void main(String args[]){
        System.out.println("Current Date: "+ getCurrentDate());
        System.out.println("Current Calendar Time: "+ getCurrentCalendar().getTime());
    }
}
