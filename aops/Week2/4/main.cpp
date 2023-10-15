#include <bits/stdc++.h>
using namespace std;


void solve() {
    int n, p;
    cin >> n >> p;

    vector<int> x(n);
    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }

    vector<int> indegree(p);
    vector<vector<int>> edges(p);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < x[i]; j++) {
            int a, b;
            cin >> a >> b;
            indegree[b-1]++;
            edges[a-1].push_back(b-1);
        }
    }
    
    stack<int> next_root;
    vector<int> topological;

    for (int i = 0; i < p; i++) {
        if (indegree[i] == 0) next_root.push(i);
    }

    bool multiple = false;
    while (next_root.size()) {
        if (next_root.size() > 1) {
            multiple = true;
        }

        int i = next_root.top();
        next_root.pop();

        topological.push_back(i);

        for (int j : edges[i]) {
            indegree[j]--;
            if (indegree[j] == 0) next_root.push(j);
        }
    }
    if (topological.size() != p) {
        cout << "NONE\n";
        return;
    }

    if (multiple) {
        cout << "MULTIPLE\n";
        return;
    }

    for (int i : topological) cout << i+1 << " ";
    cout << "\n";
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) solve();

    return 0;

}