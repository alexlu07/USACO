#include <bits/stdc++.h>
using namespace std;


void contiguous(int n, vector<int> str) {
    vector<int> prefix(n, 1);
    vector<int> suffix(n, 1);

    int premax = str[0];
    int sufmax = str[n-1];

    for (int i = 1; i < n; i++) {
        if (str[i] < premax) {
            premax = str[i];
            prefix[i] = 1;
        } else {
            prefix[i] = prefix[i-1]+1;
            premax = str[i];
        }

        if (str[n-i-1] < sufmax) {
            sufmax = str[n-i-1];
            suffix[i] = 1;
        } else {
            suffix[i] = suffix[i-1]+1;
            sufmax = str[n-i-1];
        }
    }

    int max = 0;
    for (int i = 0; i < n; i++) {
        if (prefix[i] + suffix[n-i-1] - 1 > max) max = prefix[i] + suffix[n-i-1] - 1;
    }

    cout << max << "\n";
}

void noncontiguous(int n, vector<int> str) {
    vector<int> dp_inc(26);
    vector<int> dp_dec(26);

    vector<int> ndp_inc(26);
    vector<int> ndp_dec(26);

    vector<int> prefix(n);
    vector<int> suffix(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 26; j++) {
            if (j <= str[i] && dp_inc[j]+1 > ndp_inc[str[i]]) ndp_inc[str[i]] = dp_inc[j]+1;
            if (j <= str[n-i-1] && dp_dec[j]+1 > ndp_dec[str[n-i-1]]) ndp_dec[str[n-i-1]] = dp_dec[j]+1;
        }

        dp_inc = ndp_inc;
        dp_dec = ndp_dec;

        prefix[i] = dp_inc[str[i]];
        suffix[i] = dp_dec[str[n-i-1]];
    }

    int max = 0;
    for (int i = 0; i < n; i++) {
        if (prefix[i] + suffix[n-i-1] - 1 > max) max = prefix[i] + suffix[n-i-1] - 1;
    }

    cout << max << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t, n;
    cin >> t >> n >> ws;

    vector<int> str;
    for (int i = 0; i < n; i++) {
        char c;
        cin >> c;
        str.push_back(c - 'A');
    }

    t ? noncontiguous(n, str) : contiguous(n, str);

    return 0;
}