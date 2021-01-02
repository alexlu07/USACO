/**
ID: alexlu.1
LANG: C++
TASK: ariprog
**/
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib> 
#include <fstream> 
#include <set>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <chrono>

struct Result
{
  int a;
  int b;

  bool operator<(const Result& rhs) const { 
    if (b < rhs.b) return true;
    else if (b == rhs.b) return a < rhs.a;
    else return false;
  }
};

int main() {
  // read n and m
  std::ifstream fin("ariprog.in", std::ifstream::in);
  int n, m;
  fin >> n >> m;
  std::cout << "n=" << n << ", m=" << m << std::endl;

  // generate bisquares
  int max = m * m * 2;
  std::vector<bool> bisquares_table(max+1);
  std::set<int> bisquares_set;
  for (int i = 0; i <=m; ++i)
  {
    for (int j=0; j <=m; ++j)
    {
      int num = i * i + j * j;
      bisquares_set.insert(num);
      bisquares_table[num] = true;
    }
  }
  std::vector<int> bisquares(bisquares_set.begin(), bisquares_set.end());
  int size = bisquares.size();
  
  std::cout << "bisquares: size=" << bisquares.size() << ", max=" << max << std::endl;
  // for (int num: bisquares) std::cout << num << " ";
  // std::cout << std::endl;
 
  // run
  auto start = std::chrono::steady_clock::now();
  std::set<Result> results;
  for (int i = 0; i < size; ++i)
  {
    for (int j = i + 1; j < size; ++j)
    {
      int first = bisquares[i];
      int delta = bisquares[j] - first;
      // std::cout << "i=" << i << ", j=" << j << ", first=" << first << ", delta=" << delta << std::endl;

      if (first + (n-1) * delta > max) break;

      bool sucess = true;
      for (int k = n-1; k >= 0; --k)
      {
        int num = first + k * delta;
        if (bisquares_table[num] == false)
        {
          sucess = false;
          break;
        }
      }

      if (sucess) results.insert(Result{first, delta});
    }
  }
  auto end = std::chrono::steady_clock::now();
  double duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
  std::cout << "Elapsed time in seconds : " << duration/1000000 << " sec" << std::endl;

  // dump results
  std::ofstream fout("ariprog.out", std::ifstream::out);
  if (results.empty())
  {
    fout << "NONE" << std::endl;
  }
  else
  {
    for (const auto& result: results)
    {
      fout<< result.a << " " << result.b << std::endl;
      std::cout << result.a << " " << result.b << std::endl;
    }
  }
  
  return 0;
}