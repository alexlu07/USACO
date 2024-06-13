#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    long long s = 0;
    vector<pair<int, int>> milk;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;

        s += a;
        milk.push_back({a, i});
    }

    vector<pair<int, int>> sorted_milk(n);
    partial_sort_copy(milk.begin(), milk.end(), sorted_milk.begin(), sorted_milk.end(), greater<pair<int, int>>());

    vector<int> lifespan(n);
    vector<long long> dd(n);

    for (auto[a, i] : sorted_milk) {
        int j = 0;
        int b;
        while (a < (b = milk[(i+j+1) % n].first)) {
            dd[j] += b-a;
            j += 1 + lifespan[(i+j+1) % n];
            dd[j] -= b-a;
        }
        lifespan[i] = j;
    }

    long long d = 0;
    for (long long x : dd) {
        d += x;
        s -= d;
        cout << s << "\n";
    }

    return 0;
}