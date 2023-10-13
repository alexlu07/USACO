#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
#include <limits>
#include <bitset>


int main() {
    
    int t;
    std::cin >> t;

    for (int x = 0; x < t; ++x) {
        int n;
        std::cin >> n >> std::ws;

        std::bitset<23> start;

        char ch;
        int oLoc = 0;
        int g = 0;
        for (int i = 0; i < n; ++i) {
            std::cin.get(ch);
            if (ch == 'G') {
                start.reset(i+5);
                ++g;
            } else if (ch == 'H') {
                start.set(i+5);
            } else {
                start.reset(i+5);
                oLoc = i;
            }
        }
        
        start &= -32;
        start ^= (oLoc-1);

        int answer = -1;

        std::unordered_set<std::bitset<23>> visited;
        std::queue<std::pair<std::bitset<23>, int>> queue;

        queue.push({start, 0});

        while (!queue.empty()) {
            auto[i, dist] = queue.front();
            queue.pop();

            // std::cout << "==========\n";
            // std::cout << i << " " << dist << "\n\n";

            int oLoc = i.to_ulong() % 32;

            bool found = false;
            for (int x = 0; x < n; ++x) {
                if (i[x+5]) {
                    if (oLoc < x && x >= g+2 || oLoc > x && x >= g) found = true;
                    break;
                }
            }

            if (found) {
                answer = dist;
                break;
            }

            for (int o = 0; o < n-1; ++o) {
                if (o == oLoc || o == oLoc+1 || o == oLoc-1) continue;

                std::bitset<23> j = i;

                j.set(oLoc+5, i[o+5]);
                j.set(oLoc+1+5, i[o+1+5]);

                j.reset(o+5);
                j.reset(o+1+5);

                j &= -32;
                j ^= (o);

                // std::cout << j << " " << o << "\n";

                if (!visited.count(j)) {
                    visited.insert(j);
                    queue.push({j, dist+1});
                }
            }            
        }

        if (answer == -1) std::cout << "IMPOSSIBLE\n";
        else std::cout << answer << "\n";

    }

}