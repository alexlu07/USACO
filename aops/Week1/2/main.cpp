#include <iostream>
#include <algorithm>
#include <array>
#include <limits>
#include <queue>
#include <tuple>

using namespace std;

using EndPoint = pair<int, int>; // height, loc
using Point = tuple<int, int, int, bool>; // loc, end, height, type 1=start


int main() {
    int n;
    cin >> n;

    vector<Point> timeline;

    for (int i = 0; i < n; i++) {
        int l, r, h;
        cin >> l >> r >> h;

        timeline.push_back({l, r, h, true});
        timeline.push_back({r, r, h, false});
    }

    sort(timeline.begin(), timeline.end());
    
    priority_queue<EndPoint> q;
    q.push({0, numeric_limits<int>::max()});
    long long area = 0;
    int lastTime = 0;
    for (auto [loc, end, height, type] : timeline) {
        long long lastHeight = q.top().first;

        if (type) { // start window
            if (height > lastHeight) {
                area += (loc - lastTime) * lastHeight;
                lastTime = loc;
            }
            q.push({height, end});
        } else { // end window
            if (height == lastHeight && loc == q.top().second) {
                while (q.top().second <= loc) q.pop();
                area += (loc - lastTime) * lastHeight;
                lastTime = loc;
            }
        }
    }

    cout << area << endl;

    return 0;
}

