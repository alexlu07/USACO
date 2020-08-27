/**
   ID: alexlu.1
   LANG: C++14
   TASK: inflate
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAXCAT 10000
#define MAXTIME 10000

int best[MAXTIME+1];

int main(void)
{
  FILE *fin, *fout;
  int tmax, ncat;
  int i, j, m, p, t;

  fin = fopen("inflate.in", "r");
  fout = fopen("inflate.out", "w");
  assert(fin != NULL && fout != NULL);

  fscanf(fin, "%d %d", &tmax, &ncat);

  for(i=0; i<ncat; i++) {
    fscanf(fin, "%d %d", &p, &t);
    for(j=0; j+t <= tmax; j++)
	    if(best[j]+p > best[j+t])
	    	best[j+t] = best[j]+p;
  }

	m = 0;
  for(i=0; i<=tmax; i++)
    if(m < best[i])
	    m = best[i];

  fprintf(fout, "%d\n", m);
  return 0;
}
