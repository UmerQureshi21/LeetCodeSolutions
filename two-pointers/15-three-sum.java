import java.util.ArrayList;
import java.util.List;

public class ThreeSum_15 {
    public static void main(String[] args) {
        int[] nums = { -1, 0, 1, 2, -1, -4 };
        for (int i = 0; i < threeSum(nums).size(); i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println(threeSum(nums).get(i).get(j));
            }
            System.out.println();
        }
    }

    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();
        
        
        return triplets;
    }

}
