#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int l1, l2, cha, del, ins;
    cin >> l1 >> l2 >> cha >> del >> ins;

    vector<char> s1(l1);
    vector<char> s2(l2);
    for (int i = 0; i < l1; i++) cin >> s1[i];
    for (int i = 0; i < l2; i++) cin >> s2[i];

    vector<vector<int>> dp(l1+1, vector<int>(l2+1, numeric_limits<int>::max()));
    dp[0][0] = 0;

    for (int i = 0; i <= l1; i++) {
        bool i_bound = i < l1;
        for (int j = 0; j <= l2; j++) {
            bool j_bound = j < l2;

            if (j_bound && dp[i][j] + ins < dp[i][j+1]) dp[i][j+1] = dp[i][j] + ins;
            if (i_bound && dp[i][j] + del < dp[i+1][j]) dp[i+1][j] = dp[i][j] + del;
            if (i_bound && j_bound) {
                int new_cost = dp[i][j] + cha;
                if (s1[i] == s2[j]) new_cost = dp[i][j];
                if (new_cost < dp[i+1][j+1]) dp[i+1][j+1] = new_cost;
            }
        }
    }

    cout << dp[l1][l2] << '\n';

    return 0;
}