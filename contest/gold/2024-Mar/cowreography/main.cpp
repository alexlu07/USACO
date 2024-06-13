#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<char> s(n);
    for (int i = 0; i < n; i++) cin >> s[i];
    
    vector<vector<int>> m0(k);
    vector<vector<int>> m1(k);

    unordered_set<int> l0;
    unordered_set<int> l1;
    for (int i = 0; i < n; i++) {
        char c;
        cin >> c;
        if (c != s[i]) {
            if (c == '0') {
                m0[i % k].push_back(i);
                l0.insert(i);
            } else {
                m1[i % k].push_back(i);
                l1.insert(i);
            }
        }
    }

    int steps = 0;

    for (auto i : m0) {
        for (auto j : i) cout << j << " ";
        cout << "| ";
    }
    cout << '\n';

    for (auto i : m1) {
        for (auto j : i) cout << j << " ";
        cout << "| ";
    }
    cout << '\n';

    for (int i : l0) cout << i << " ";
    cout << '\n';

    for (int i : l1) cout << i << " ";
    cout << '\n';


    for (int i = 0; i < k; i++) {
        for (int j = 0; j < min(m0[i].size(), m1[i].size()); j++) {
            l0.erase(m0[i][j]);
            l1.erase(m1[i][j]);
            steps += abs(m1[i][j] - m0[i][j]) / k;
        }
    }

    for (int i : l0) cout << i << " ";
    cout << '\n';

    for (int i : l1) cout << i << " ";
    cout << '\n';

    for (auto i = l1.begin(), j = l0.begin(); i != l1.end(); i++, j++) {
        steps += abs(*i - *j) / k + 1;
    }

    cout << steps << "\n";

    return 0;
}