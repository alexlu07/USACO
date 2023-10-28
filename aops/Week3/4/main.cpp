#include <bits/stdc++.h>
using namespace std;


using IntPair = pair<int, int>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> colors(n);

    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        colors[i] = c - 1;
    }

    vector<vector<IntPair>> adj(1000);

    for (int i = 0; i < m; i++) {
        int a, b, d;
        cin >> a >> b >> d;
        a = colors[a-1];
        b = colors[b-1];

        adj[a].push_back({d, b});
        adj[b].push_back({d, a});
    }

    vector<bool> visited(n);
    vector<int> bestimates(n, numeric_limits<int>::max());
    priority_queue<IntPair, vector<IntPair>, greater<IntPair>> pqueue;
    pqueue.push({-1, 0});

    long long dist = 0;

    while (!pqueue.empty()) {
        auto [d, i] = pqueue.top();
        pqueue.pop();

        if (visited[i]) continue;

        visited[i] = true;
        if (d != -1) dist += d;
        
        for (auto [dj, j] : adj[i]) {
            if (visited[j]) continue;
            if (dj >= bestimates[j]) continue;
            
            pqueue.push({dj, j});
            bestimates[j] = dj;
        }
    }

    cout << dist << "\n";

    return 0;

}