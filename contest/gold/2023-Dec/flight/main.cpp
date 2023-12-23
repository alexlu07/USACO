#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<vector<int>> routes(n, vector<int>(n));
    vector<vector<int>> flight(n, vector<int>(n));

    int ans = 0;

    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            char d;
            cin >> d;
            int f = d - '0';
            routes[i][j] = f;
            flight[i][j] = f;
            if (j == i + 1) ans += f;
        }
    }

    for (int j = 1; j < n; j++) {
        for (int i = j-2; i >= 0; i--) {
            int r = 0;
            for (int k = i+1; k < j; k++) {
                r += routes[i][k] * flight[k][j];
            }

            flight[i][j] = (r + routes[i][j]) % 2;
            routes[i][j] = r + flight[i][j];
            ans += flight[i][j];
        }
    }

    cout << ans << "\n";

    // for (size_t i = 0; i < routes.size(); ++i) {
    //     for (size_t j = 0; j < routes[i].size(); ++j) {
    //         std::cout << routes[i][j] << " ";
    //     }
    //     std::cout << std::endl;
    // }
    // for (size_t i = 0; i < flight.size(); ++i) {
    //     for (size_t j = 0; j < flight[i].size(); ++j) {
    //         std::cout << flight[i][j] << " ";
    //     }
    //     std::cout << std::endl;
    // }
    return 0;
}