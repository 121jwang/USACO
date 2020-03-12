#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define FOREACH(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define MOD 1000000007
#define INF 2000000000

void union_init(int d[], int s) { for (int i=0; i < s; i++) d[i]=i; }
int union_query(int d[], int n) { int res=n; while (d[res]!=res) res=d[res]; int m; while (d[n]!=n) {m=d[n];d[n]=res;n=m;} return res; };
int union_merge(int d[], int x, int y) { x=union_query(d,x); y=union_query(d,y); if (x==y)return -1; d[x]=y; return 1; }

const int MAXN = 100010;
int order[MAXN], place[MAXN], u[MAXN], v[MAXN], par[MAXN]; bool res[MAXN];

int N, M;

vector< vector<int> > adj;

int main() {
	ifstream infile;
	infile.open("closing.in");

    infile >> N >> M;
    FORN(i, M) infile >> u[i] >> v[i];

    ofstream outputFile;
    outputFile.open("closing.out");

    FORN(i, N) {
	    infile >> order[i];
        place[order[i]] = i;
    }

    adj.resize(N+1);

    FORN(i, M) {
        if (place[u[i]] > place[v[i]]) adj[v[i]].push_back(u[i]);
        else adj[u[i]].push_back(v[i]);
    }

    union_init(par, N+1); int comps = 0;

    FORD(i, N) {
        int u = order[i]; comps++;
        FORN(j, adj[u].size()) {
            int v = adj[u][j];
            if (union_query(par, u) != union_query(par, v)) {
                union_merge(par, u, v);
                comps--;
            }
        }

        res[i] = (comps <= 1);
    }

    for (int i = 0; i < N; i++){
	    if (res[i]){ 
		    outputFile << "YES\n";} 
	    else {
		    outputFile << "NO\n";}
    }
    outputFile.close();
    return 0;
}
