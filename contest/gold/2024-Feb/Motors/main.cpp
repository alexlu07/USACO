#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m, c, r, k;
    cin >> n >> m >> c >> r >> k;

    vector<vector<pair<int, int>>> roads(n);
    for (int i = 0; i < m; i++) {
        int u, v, l;
        cin >> u >> v >> l;
        u--; v--;
        roads[u].push_back({v, l});
        roads[v].push_back({u, l});
    }

    vector<int> connected(n);

    for (int x = 0; x < c; x++) {
        priority_queue<pair<long long, int>, 
                        vector<pair<long long, int>>, 
                        greater<pair<long long, int>>> queue;
        vector<long long> dist(n, numeric_limits<long long>::max());

        dist[x] = 0;
        queue.push({0, x});

        while (!queue.empty()) {
            auto [d, i] = queue.top();
            queue.pop();

            if (d > dist[i]) continue;
            if (d <= r) connected[i]++;
            else break;

            for (auto [j, e] : roads[i]) {
                long long new_d = d + e;
                if (new_d < dist[j]) {
                    dist[j] = new_d;
                    queue.push({new_d, j});
                }
            }
        }
    }

    // for (int i : connected) cout << i << "\n";

    vector<int> wellConnected;
    for (int i = c; i < n; i++) {
        if (connected[i] >= k) {
            wellConnected.push_back(i);
        }
    }

    sort(wellConnected.begin(), wellConnected.end());

    cout << wellConnected.size() << "\n";
    for (int i : wellConnected) cout << i+1 << "\n";

    return 0;
}