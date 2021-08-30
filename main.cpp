#include <bits/stdc++.h>
#define FOR(i,s,n) for(int i = s;i<n;i++)
using namespace std;

void listret(int * a);

int main() { 
  int b[5];
  listret(b);
  FOR(i,0,5){
    cout<<b[i]<<' ';
  }
}

void listret(int * a){
  FOR(i,0,5) a[i] = i;
}