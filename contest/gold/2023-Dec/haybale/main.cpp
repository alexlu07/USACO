#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> raw_barns(n);
    long long base_cost = 0;
    for (int i = 0; i < n; i++) {
        cin >> raw_barns[i];
        base_cost += raw_barns[i]+1;
    }
    sort(raw_barns.begin(), raw_barns.end());

    vector<int> barns;
    vector<int> counts;
    int last = -1;
    for (int i = 0; i < n; i++) {
        if (raw_barns[i] == last) continue;
        barns.push_back(raw_barns[i]);
        counts.push_back(i);
        last = raw_barns[i];
    }
    int un = barns.size();

    vector<long long> l(un);
    vector<long long> r(un);
    vector<long long> sl(un);
    vector<long long> sr(un);
    for (int i = 0; i < un; i++) {
        if (i > 0) {
            long long d = barns[i] - barns[i-1];
            l[i] = d * counts[i];
            r[i] = d * (n - counts[i]);
            sl[i] = sl[i-1] + l[i];
            sr[i] = sr[i-1] + r[i];
        } else {
            long long d = barns[i] + 1;
            l[i] = d * counts[i];
            r[i] = d * (n - counts[i]);
            sl[i] = l[i];
            sr[i] = r[i];
        }
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        long long a, b;
        cin >> a >> b;

        int lb = 0;
        int rb = un;
        int m;

        while (lb < rb) {
            m = (lb + rb) / 2;

            if (b * r[m] < a * l[m]) rb = m;
            else lb = m+1;

        }

        int loc = lb-1;
        cout << b * base_cost + a * sl[loc] - b * sr[loc] << "\n";
    }

    return 0;
}