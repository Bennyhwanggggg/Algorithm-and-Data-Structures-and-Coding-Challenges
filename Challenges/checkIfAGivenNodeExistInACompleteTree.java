// https://leetcode.com/discuss/interview-question/236898/Google-Phone-Interview
// https://leetcode.com/discuss/interview-experience/305582/Google-SWE-L3-phone-screen

// Time and space: O(log(n))
public class Main {
    private static final int ROOT = 1;

    public static boolean doesNodeExist(TreeNode root, int target) {
        if (root == null) return false;
        Deque<Integer> path = getPathFromRootTo(target);
        return verifyPath(root, path);
    }

    private static boolean verifyPath(TreeNode node, Deque<Integer> path) {
        while (!path.isEmpty()) {
            node = path.pop() % 2 == 0 ? node.left : node.right;
            if (node == null) return false;
        }
        return true;
    }

    private static Deque<Integer> getPathFromRootTo(int child) {
        Deque<Integer> stack = new ArrayDeque<>();
        while (child != ROOT) {
            stack.push(child);
            child = getParentIndex(child);
        }
        return stack;
    }

    private static int getParentIndex(int childIndex) {
        return childIndex / 2;
    }
    
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(6);

        System.out.println(doesNodeExist(root, 5)); // false
        System.out.println(doesNodeExist(root, 7)); // false
        System.out.println(doesNodeExist(root, 20)); // false
        System.out.println(doesNodeExist(null, 1)); // false
        System.out.println(doesNodeExist(root, 1)); // true
        System.out.println(doesNodeExist(root, 2)); // true
        System.out.println(doesNodeExist(root, 3)); // true
        System.out.println(doesNodeExist(root, 4)); // true
        System.out.println(doesNodeExist(root, 6)); // true
    }
}
