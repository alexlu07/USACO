#include <iostream>
#include <limits>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

int main() {
    
    int n, m;
    cin >> n >> m;

    vector<vector<tuple<int, int, int>>> edges(n);

    for (int i = 0; i < m; ++i) {
        int a, b, l, s;
        cin >> a >> b >> l >> s;
        
        edges[a-1].push_back({b-1, s, l});
        edges[b-1].push_back({a-1, s, l});

    }

    vector<int> sizes(n, -1);
    vector<bool> visited1(n);

    priority_queue<tuple<int, int>> heap1; // size, node
    heap1.push({numeric_limits<int>::max(), 0});
    
    while (!heap1.empty()) {
        auto [s, i] = heap1.top();
        heap1.pop();

        if (visited1[i]) continue;
        visited1[i] = true;

        for (auto [j, ds, dl] : edges[i]) {
            if (visited1[j]) continue;
            int newS = min(s, ds);
            if (newS > sizes[j]) {
                sizes[j] = newS;
                heap1.push({newS, j});
            }
        }
    }

    int max_size = sizes[n-1];

    vector<long long> dists(n, numeric_limits<long long>::min());
    vector<bool> visited2(n);

    priority_queue<tuple<long long, int>> heap2; // -length, node
    heap2.push({0, 0});
    
    while (!heap2.empty()) {
        auto [l, i] = heap2.top();
        heap2.pop();

        if (visited2[i]) continue;
        visited2[i] = true;

        for (auto [j, ds, dl] : edges[i]) {
            if (visited2[j] || ds < max_size) continue;
            long long newD = l - dl;
            if (newD > dists[j]) {
                dists[j] = newD;
                heap2.push({newD, j});
            }
        }
    }

    cout << sizes[n-1] << " " << -dists[n-1] << endl;

}