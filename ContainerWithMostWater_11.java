public class ContainerWithMostWater_11 {
    public static void main(String[] args) {
        int[] height = { 1, 8, 6, 2, 5, 4, 8, 3, 4 };
        System.out.println(maxArea(height));
    }

    public static int maxArea(int[] height) {
        int max = 0;
        int lp = 0;
        int rp = height.length - 1;

        while (lp < rp) {
            if (max < (rp - lp) * (Math.min(height[lp], height[rp]))) {
                max = (rp - lp) * (Math.min(height[lp], height[rp]));
            }
            if (height[lp] < height[rp]) {
                lp++;
            } else {
                rp--;
            }
        }

        return max;
    }

}
