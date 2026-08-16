public class TrappingRainWater_42 {

    public static void main(String[] args) {
        new TrappingRainWater_42();
    }

    public TrappingRainWater_42() {

        int[] height = {0,1,0,2,1,0,1,3,2,1,2,1};
        System.out.println(trap(height));
    }

    public int trap(int[] height) {
        int lp = 0;
        int rp = lp + 1;
        int rain = 0;
        int currRain = 0;

        while (rp < height.length) {
            if (height[rp] > height[lp]) {
                lp = rp++;
                rain += currRain;
                currRain = 0;
            } else {
                currRain += (height[lp] - height[rp++]);
            }
        }
        // lp is now at max height and rp is now at height.length
        int maxIndex = lp;
        rp--;
        lp = rp - 1;

        currRain = 0;
        while (lp >= maxIndex) {
            if (height[lp] > height[rp]) {
                rp = lp--;
                rain += currRain;
                currRain = 0;
            } else {
                currRain += (height[rp] - height[lp--]);
                System.out.println(currRain);
            }
        }

        return rain;
    }

}
