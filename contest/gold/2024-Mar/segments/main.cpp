#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<pair<int, int>> points; // s, k
    vector<tuple<int, int, int>> endpoints; // x, s/e = 1/0, p
    for (int i = 0; i < n; i++) {
        int l, r, k;
        cin >> l >> r >> k;
        endpoints.push_back({r, 0, i});
        endpoints.push_back({l, 1, i});
        points.push_back({l, k});
    }

    sort(endpoints.begin(), endpoints.end());

    vector<int> overlaps(n);
    unordered_set<int> stack;

    for (auto[x, t, i] : endpoints) {
        if (t) {
            stack.insert(i);
        } else {
            stack.erase(i);
            for (int j : stack) {
                int d = x - max(points[i].first, points[j].first);
                if (points[i].second <= d) overlaps[i]++;
                if (points[j].second <= d) overlaps[j]++;
            }
        }
    }

    for (int i : overlaps) {
        cout << i << "\n";
    }

    return 0;
}