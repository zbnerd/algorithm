#include <iostream>
#include <queue>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void bfs(long long s, long long t){
    
    long long max = 1000000000LL;
    
    unordered_set<int> visited;
    queue<pair<long long, string> > q;
    
    q.push(make_pair(s, ""));
    visited.insert(s);
    
    while(!q.empty()){
        pair<long long, string> pop_pair = q.front(); q.pop();
        long p = pop_pair.first;
        string op = pop_pair.second;
        
        if(p == t){
            cout << op;
            return;
        }
        
        if((0 <= p*p && p*p <= max) && (visited.find(p*p) == visited.end())){ //p*p 방문안한경우
            visited.insert(p*p);
            q.push(make_pair(p*p,op+"*"));
        }
        
        if((0 <= p+p && p+p <= max) && (visited.find(p+p) == visited.end())){ //p+p 방문안한경우
            visited.insert(p+p);
            q.push(make_pair(p+p,op+"+"));
        }
        
        if((0 <= p-p && p-p <= max) && (visited.find(p-p) == visited.end())){ //p-p 방문안한경우
            visited.insert(p-p);
            q.push(make_pair(p-p,op+"-"));
        }
        
        if((p != 0 && 0 <= p / p && p / p <= max) && visited.find(p/p) == visited.end()){ //p/p 방문안한경우
            visited.insert(p/p);
            q.push(make_pair(p/p,op+"/"));
        }
    }
    cout << -1;
}

void solve(){
    long long s, t;
    vector<string> ops;
    
    cin >> s >> t;
    
    if (s==t) {
        cout << 0;
        return;
    }
    
    bfs(s,t);
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    solve();
    
    return 0;
}