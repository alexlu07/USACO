#include <bits/stdc++.h>
using namespace std;

using Edge = pair<int, int>;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        return h1 ^ h2;  
    }
};


int find(int i, vector<int> &uf) {
    int group = i;
    while (group != uf[group]) group = uf[group];

    while (uf[i] != group) {
        int j = uf[i];
        uf[i] = group;
        i = j;
    }

    return group;
}

void merge(int i, int j, vector<int> &uf, vector<int> &mass) {
    i = find(i, uf);
    j = find(j, uf);

    if (i == j) return;

    if (mass[i] < mass[j]) swap(i, j);
    uf[j] = i;
    mass[i] += mass[j];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m, d, q;
    cin >> n >> m >> d >> q;

    unordered_set<Edge, pair_hash> edges;
    unordered_set<Edge, pair_hash> blacklist;

    list<tuple<bool, int, int>> instructions;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        edges.insert({a-1, b-1});
    }

    for (int i = 0; i < q; i++) {
        char t;
        int x, y;
        cin >> ws >> t >> x >> y;
        x--;
        y--;

        if (d) {
            if (t == 'C') {
                instructions.push_front({false, x, y});
            } else {
                if (!blacklist.count({x, y}) && edges.count({x, y})){
                    instructions.push_front({true, x, y});
                    blacklist.insert({x, y});
                }
            }
        } else {
            if (t == 'C') {
                instructions.push_back({false, x, y});
            } else {
                instructions.push_back({true, x, y});
            }
        }
    }

    vector<int> union_find(n);
    vector<int> mass(n);

    for (int i = 0; i < n; i++) {
        union_find[i] = i;
        mass[i] = 1;
    }

    for (auto [i, j] : edges) {
        if (!blacklist.count({i, j})) {
            merge(i, j, union_find, mass);
        }
    }

    list<int> ans;

    for (auto [op, i, j] : instructions) {
        if (op) {
            merge(i, j, union_find, mass);
        } else {
            if (d) ans.push_front(find(i, union_find) == find(j, union_find));
            else ans.push_back(find(i, union_find) == find(j, union_find));
        }
    }

    for (int i : ans) cout << (i ? "YES\n" : "NO\n");

    return 0;
}