#include <bits/stdc++.h>
using namespace std;

using row = vector<long long>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    const long long max_num = numeric_limits<long long>::max();

    int n, m;
    cin >> n >> m;

    vector<row> dist(n, row(n, max_num));

    for (int i = 0; i < m; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        dist[a-1][b-1] = c;
    }
    
    for (int i = 0; i < n; ++i) {
        dist[i][i] = 0;
    }

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j] &&
                    dist[i][k] != max_num && dist[k][j] != max_num) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            total += dist[i][j];
        }
    }

    cout << total << "\n";

    return 0;

}