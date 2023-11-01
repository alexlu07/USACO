#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    long long min_long = numeric_limits<long long>::min();

    vector<long long> dp(k+1, min_long);
    vector<long long> new_dp(k+1);

    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        
        for (int j = 0; j < k+1; j++) {
            new_dp[j] = min_long;
            if (j > 0 && dp[j-1] == min_long) continue;

            if (j > 0) new_dp[j] = dp[j-1];
            if (dp[j] != min_long && dp[j] > new_dp[j]) new_dp[j] = dp[j];

            new_dp[j] += x * ((j % 2) ? -1 : 1);
        }

        dp = new_dp;
    }

    cout << *max_element(dp.begin(), dp.end()) << "\n";

    return 0;
}