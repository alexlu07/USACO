#include <iostream>
#include <vector>

using namespace std;

int main() {
    int q = 0;
    cin >> q;

    std::vector<int> heap;
    heap.reserve(q);

    for (size_t i = 0; i < q; ++i)
    {
        int x = 0;
        cin >> x;

        if (x == 0) 
        {
            auto last = heap.size() - 1;
            heap[0] = heap[last];
            heap.resize(last);

            // propogate down

            size_t parent = 0;
            size_t child = 0;
            while (true) // while node has at least 1 child
            {
                auto child1 = parent*2+1;
                auto child2 = parent*2+2;

                if (child1 >= heap.size()) break;

                if (child2 >= heap.size())
                {
                    child = child1;
                }
                else
                {
                    child = heap[child1] > heap[child2] ? child1 : child2;
                }
                    
                if (heap[child] <= heap[parent]) break;

                swap(heap[child], heap[parent]);
                parent = child;
            }
        } 
        else 
        {
            heap.push_back(x);
      
            // propogate up
            int parent = 0;
            int child = heap.size() - 1;
            while (child > 0) // while child has parent
            {
                parent = (child-1) / 2;

                if (heap[child] <= heap[parent]) break;

                swap(heap[child], heap[parent]);
                child = parent;
            }
        }

        for (auto i = 0; i < heap.size(); ++i)
        {
            std::cout << heap[i] << (i == heap.size() - 1 ? "" : " ");
        }
        std::cout << std::endl;    
    }

    return 0;
}