#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    const int MIN_INT = numeric_limits<int>::min();

    int t;
    cin >> t;

    for (int c = 0; c < t; c++) {
        int s, n, x;
        cin >> s >> n >> x;

        vector<array<int, 3>> edges;
        for (int i = 0; i < s; i++) {
            int a, b, d;
            cin >> a >> b >> d;
            edges.push_back({a-1, b-1, d});
        }

        vector<int> dist(n, MIN_INT);
        dist[0] = 1e6;

        bool found = false;

        for (int k = 0; k < n; k++) {
            bool unchanged = true;
            for (int i = 0; i < s; i++) {
                auto [a, b, d] = edges[i];

                int new_dist = dist[a] - d;

                if (dist[a] != MIN_INT && new_dist > dist[b] && new_dist >= 0) {
                    dist[b] = new_dist;
                    unchanged = false;

                    if (new_dist >= x) {
                        found = true;
                        unchanged = true;
                        break;
                    }
                }
            }
            if (unchanged) break;
            else if (!unchanged && k == n-1) found = true;
        }

        cout << (found ? "YES\n" : "NO\n");
    }

    return 0;

}