class Solution {
public:
    char kthCharacter(int k) {
        string x = "a";
        while (x.size() < k) {
            int len = x.size();
            for (int i = 0; i < len; i++) {
                x.push_back(x[i] + 1);
            }
        }
        return x[k - 1];
    }
    };