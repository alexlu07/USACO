#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> used_edges(m, 0);
    vector<pair<int, int>> edges;
    vector<vector<pair<int, int>>> adj(m);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;

        edges.push_back({a, b});
        adj[a].push_back({i, b});
        adj[b].push_back({i, a});
    }

    vector<int> bestimates(n, numeric_limits<int>::max());
    vector<bool> visited(n);
    priority_queue<pair<int, int>> pqueue;

    visited[0] = true;
    for (auto[edge, j] : adj[0]) {
        if (visited[j]) continue;
        if (edge >= bestimates[j]) continue;
        
        pqueue.push({-edge, j});
        bestimates[j] = edge;
    }

    while (!pqueue.empty()) {
        auto[edge, i] = pqueue.top();
        edge = -edge;
        pqueue.pop();

        if (visited[i]) continue;

        visited[i] = true;
        used_edges[edge] = true;

        for (auto[edge, j] : adj[i]) {
            if (visited[j]) continue;
            if (edge >= bestimates[j]) continue;
            
            pqueue.push({-edge, j});
            bestimates[j] = edge;
        }
    }

    for (int i = 0; i < m; i++) {
        if (used_edges[i] == 0) {
            cout << edges[i].first+1 << " " << edges[i].second+1 << "\n";
        }
    }

    return 0;

}