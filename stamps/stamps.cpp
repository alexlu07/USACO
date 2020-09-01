/**
ID: alexlu.1
LANG: C++14
TASK: stamps
**/
#include <iostream>
#include <fstream>

using namespace std;

const int BIG = 10000;

short   minstamps[10000 * (200 + 3) + 3];
int     stamps;
int     value[200];
int     number;


int main ()
{

  ifstream filein ("stamps.in");
  filein >> number >> stamps;
  int     biggest = -1;
  for (int i = 0; i < stamps; ++i) {
    filein >> value[i];
    if (biggest < value[i]) {
	    biggest = value[i];
    }
  }
  filein.close ();

  for (int i = 0; i <= biggest * number + 3; ++i) {
    minstamps[i] = BIG;
  }

  minstamps[0] = 0;
  for (int i = 0; i < stamps; ++i) {
    for (int j = 0; j <= biggest * number; ++j) {
	    if (minstamps[j] < number) {
        if (minstamps[j + value[i]] > 1 + minstamps[j]) {
          minstamps[j + value[i]] = 1 + minstamps[j];
        }
	    }
    }
  }


  int     string = 0;
  while (minstamps[string + 1] <= number) {
    ++string;
  }

  ofstream fileout ("stamps.out");
  fileout << string << endl;
  fileout.close ();

  return (0);
}
