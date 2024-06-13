#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, d, k;
    cin >> n >> d >> k;

    vector<vector<int>> edges(n);

    for (int i = 0; i < n-1; i++) {
        int a, b;
        cin >> a >> b;
        edges[a-1].push_back(b-1);
        edges[b-1].push_back(a-1);
    }

    vector<vector<int>> order;
    vector<vector<int>> children(n);

    vector<bool> visited(n);
    queue<pair<int, int>> queue;
    queue.push({0, 0});

    while (!queue.empty()) {
        auto [i, l] = queue.front();
        queue.pop();
        visited[i] = true;


        if (order.size() <= l) order.push_back({});
        order[l].push_back(i);

        for (int j : edges[i]) {
            if (visited[j]) continue;
            queue.push({j, l+1});
            children[i].push_back(j);
        }
    }

    vector<vector<vector<int>>> dp(n, vector<vector<int>>(d, vector<int>(d)));

    for (int i = order.size()-1; i >= 0; i--) {
        if (i == order.size()-1) {
            for (int x = 0; x < d; x++) fill(dp[i][x].begin(), dp[i][x].end(), x+1);
            continue;
        }

        for (int x = 0; x < d; x++) {
            vector<int> dp2(1 << d);
            
        }
    }

    return 0;
}