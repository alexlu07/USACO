#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<long long> p(n);
    vector<int> s(n);

    for (int i = 0; i < n; i++) cin >> p[i];
    for (int i = 0; i < n; i++) cin >> s[i];

    priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<tuple<long long, int, int>>> queue;
    for (int i = 0; i < n-1; i++) {
        long long o = 2 * (1 + (p[i+1]-p[i]-1) / (s[i]+s[i+1])) - (i+1) % 2;
        queue.push({o, i, i+1});
    }

    vector<int> disappeared(n);
    vector<long long> observation(n);

    vector<int> left(n);
    vector<int> right(n);

    for (int i = 0; i < n; i++) {
        left[i] = i;
        right[i] = i;
    }

    while (!queue.empty()) {
        auto [o, i, j] = queue.top();
        queue.pop();

        // cout << o << "|" << i << " " << j << "\n";

        if (disappeared[i] || disappeared[j]) continue;
        
        observation[i] = o; observation[j] = o;
        disappeared[i] = 1; disappeared[j] = 1;

        right[i] = (j < n-1) ? right[j+1] : -1;
        left[j] = (i > 0) ? left[i-1] : -1;

        int q = right[i];
        while (q != right[q] && q != -1) {
            q = right[q];
        }
        right[i] = q;

        int r = left[j];
        while (r != left[r] && r != -1) {
            r = left[r];
        }
        left[j] = r;


        int next_i = left[j];
        int next_j = right[i];

        // cout << next_i << next_j << "\n";
        if (next_i != -1 && next_j != -1) {
            long long next_o = 2 * (1 + (p[next_j]-p[next_i]-1) / (s[next_j]+s[next_i])) - (next_i+1) % 2;
            queue.push({next_o, next_i, next_j});
        }
    }

    cout << observation[0];
    for (int i = 1; i < n; i++) cout << " " << observation[i];
    cout << "\n";

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}

