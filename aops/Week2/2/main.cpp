#include <bits/stdc++.h>
using namespace std;

using Stack = stack<int>;
using Edges = vector<vector<int>>;
using Visit = vector<bool>;

void postorder_dfs(int i, Stack& postorder, Visit& visited, Edges& adj) {
    for (int j : adj[i]) {
        if (!visited[j]) {
            visited[j] = true;
            postorder_dfs(j, postorder, visited, adj);
        }
    }

    postorder.push(i);

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    Edges adj(n);
    Edges rev(n);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a-1].push_back(b-1);
        rev[b-1].push_back(a-1);
    }

    Stack postorder;
    Visit visited1(n);
    
    for (int i = 0; i < n; i++) {
        if (!visited1[i]) {
            visited1[i] = true;
            postorder_dfs(i, postorder, visited1, adj);
        }
    }

    int ans = 0;
    Visit visited2(n);
    Stack dfs_stack;

    while (!postorder.empty()) {
        int x = postorder.top();
        postorder.pop();

        if (visited2[x]) continue;

        dfs_stack.push(x);
        visited2[x] = true;

        while (!dfs_stack.empty()) {
            int i = dfs_stack.top();
            dfs_stack.pop();

            for (int j : rev[i]) {
                if (!visited2[j]) {
                    visited2[j] = true;
                    dfs_stack.push(j);
                }
            }
        }

        ans++;
    }

    cout << ans << "\n";    

    return 0;

}