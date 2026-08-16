public class TwoSumTwo_167 {
    public static void main(String[] args) {
        int[] numbers = { 1, 3, 8, 10, 12 };
        for (int num : twoSum(numbers, 22)) {
            System.out.println(num);
        }
    }

    public static int[] twoSum(int[] numbers, int target) {

        int[] indices = new int[2];
        boolean keepGoing = true;
        int lp = 0;
        int rp = numbers.length - 1;
        while (lp < rp && keepGoing) {
            if (numbers[lp] + numbers[rp] == target) {
                indices[0] = ++lp;
                indices[1] = ++rp;
                keepGoing = false;
            } else if (numbers[lp] + numbers[rp] > target) {
                rp--;
            } else {
                lp++;
            }
        }

        return indices;
    }
}