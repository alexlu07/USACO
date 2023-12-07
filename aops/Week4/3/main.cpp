#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int l, k;
    cin >> l >> k;

    vector<long long> dp(l+1);

    for (int c = 0; c < k; c++) {
        long long n, p, t;
        cin >> n >> p >> t;
        
        int m = 1;
        while (m <= n/2) {
            long long p_m = p * m;
            long long t_m = t * m;

            for (int i = l; i >= t_m; i--) if (dp[i-t_m] + p_m > dp[i]) dp[i] = dp[i-t_m] + p_m;

            m *= 2;
        }

        m = n-m+1;
        for (int i = l; i >= t*m; i--) if (dp[i-t*m] + p*m > dp[i]) dp[i] = dp[i-t*m] + p*m;
    }

    cout << *max_element(dp.begin(), dp.end()) << "\n";  

    return 0;
}