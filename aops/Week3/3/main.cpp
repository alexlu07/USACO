#include <bits/stdc++.h>
using namespace std;


using Edge = pair<int, int>;
using Edges = vector<Edge>;
using Adjacency = vector<Edges>;

int n, m;
char x, y;


void prims(Adjacency &adj) {
    vector<int> weights;
    vector<int> sizes;
    int size = 1;

    vector<bool> visited(n);
    vector<int> bestimates(n, numeric_limits<int>::max());
    priority_queue<Edge, vector<Edge>, greater<Edge>> pqueue;
    pqueue.push({-1, 0});

    while (!pqueue.empty()) {
        auto [edge, i] = pqueue.top();
        pqueue.pop();

        if (visited[i]) continue;

        visited[i] = true;
        if (edge != -1) {
            weights.push_back(edge+1);
            sizes.push_back(++size);
        }
        
        for (auto [dist, j] : adj[i]) {
            if (visited[j]) continue;
            if (dist >= bestimates[j]) continue;
            
            pqueue.push({dist, j});
            bestimates[j] = dist;
        }
    }

    for (int i : ((y == 'W') ? weights : sizes)) cout << i << "\n";
}

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

int merge(int i, int j, vector<int> &uf, vector<int> &masses) {
    i = find(i, uf);
    j = find(j, uf);

    if (i == j) return 0;

    if (masses[i] < masses[j]) swap(i, j);
    uf[j] = i;
    masses[i] += masses[j];

    return masses[i];
}

void kruskals(Edges &edges) {
    vector<int> weights;
    vector<int> sizes;
    int weight = 1;
    int size = 0;

    vector<int> union_find(n);
    vector<int> masses(n, 1);

    for (int i = 0; i < n; i++) union_find[i] = i;

    for (auto [i, j] : edges) {
        int mass = merge(i, j, union_find, masses);
        if (mass) {
            if (mass > size) size = mass;
            weights.push_back(weight);
            sizes.push_back(size);
        }
        weight++;
    }

    for (int i : ((y == 'W') ? weights : sizes)) cout << i << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m >> ws >> x >> ws >> y;

    Edges edges;
    Adjacency adj(n);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a--;
        b--;

        edges.push_back({a, b});
        adj[a].push_back({i, b});
        adj[b].push_back({i, a});
    }

    if (x == 'P') prims(adj);
    else kruskals(edges);

    return 0;

}