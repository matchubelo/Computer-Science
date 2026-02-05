package Java;
import java.util.*;

public class AugustCalenendarMJB 
{
    public static void main(String[] args) 
    {
      // August 2026 starts on a Saturday
      int[][] calendar = {
        {0, 0, 0, 0, 0, 0, 1},
        {2, 3, 4, 5, 6, 7, 8},
        {9, 10, 11, 12, 13, 14, 15},
        {16, 17, 18, 19, 20, 21, 22},
        {23, 24, 25, 26, 27, 28, 29},
        {30, 31, 0, 0, 0, 0, 0}
      };

      String[] days = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
      System.out.println("    August 2026");
      for (String d : days) {
        System.out.printf("%4s", d);
      }
      System.out.println();
      for (int week = 0; week < calendar.length; week++) {
        for (int day = 0; day < 7; day++) {
          if (calendar[week][day] == 0) {
            System.out.printf("    ");
          } else {
            System.out.printf("%4d", calendar[week][day]);
          }
        }
        System.out.println();
      }
    }
}