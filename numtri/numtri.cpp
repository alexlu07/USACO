/**
ID: alexlu.1
LANG: C++14
TASK: numtri
**/
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib> 
#include <fstream> 
#include <set>
#include <vector>
#include <chrono>
#include <algorithm>

struct Node{
  Node(int v) : val(v) {}

  int   val;
  int   max{-1};
  Node* left{nullptr};
  Node* right{nullptr}; 

};

using Data = std::vector<std::vector<Node>>;

void print_data(const Data& data)
{
  for (const auto& row: data)
  {
    for (const auto& node: row)
    {
      std::cout << node.val;
      if (node.max != -1) std::cout << "," << node.max;
      if (node.left) std::cout << "," << node.left->val;
      if (node.right) std::cout << "," << node.right->val;
      std::cout << " ";
    }
    std::cout << std::endl;
  }
}

int main() 
{
  Data data;
  std::ifstream fin("numtri.in", std::ifstream::in);
  int n;
  fin >> n;
  for (int i = 0; i < n; ++i)
  {
    std::vector<Node> row;
    row.reserve(i+1);
    data.push_back(std::move(row));

    for (int j = 0; j <= i; ++j)
    {
      int num;
      fin >> num;
      data[i].push_back(Node(num));
    }
  }
  //print_data(data);

  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j <= i; ++j)
    {
      if (i < n - 1)
      {
        data[i][j].left  = &data[i+1][j];
        data[i][j].right = &data[i+1][j+1];
      }
    }
  }
  //print_data(data);

  std::reverse(std::begin(data), std::end(data));
  //print_data(data);

  for (auto& row: data)
  {
    for (auto& node: row)
    {
      if (not node.left and not node.right)
        node.max = node.val;
      else
        node.max = std::max(node.left->max, node.right->max) + node.val;
    }
  }

  int result = data[n-1][0].max;
  std::ofstream fout("numtri.out", std::ifstream::out);
  fout << result << std::endl;
  std::cout << result << std::endl;

  return 0;
}