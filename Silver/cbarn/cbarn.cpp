#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
using namespace std;

long long sumn2(long long v) {
  return v * (v + 1) * (2 * v + 1) / 6;
}

int main() {
	ifstream cin;
	cin.open("cbarn.in");

  int N; cin >> N;
  vector<long long> A(N);

  int c = 0;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
    c = max(0ll, c + A[i] - 1);
  }

  for (int i = 0; ; i++) {
    if (c == 0) {
      rotate(A.begin(), A.begin() + i, A.begin() + N);
      break;
    }
    c = max(0ll, c + A[i] - 1);
  }


  long long result = 0;
  for (int i = 0; i < N; i++) {
    result += sumn2(A[i] + c - 1) - sumn2(c - 1);
    c = max(0ll, c + A[i] - 1);
  }
  ofstream cout;
  cout.open("cbarn.out");
  cout << result << endl;
  cout.close();
}
