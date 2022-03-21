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
    pair<long long, string> num_op_pair = make_pair(s, "");
    
    q.push(num_op_pair);
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
            pair<long long, string> multiple = make_pair(p*p,op+"*");
            q.push(multiple);
        }
        
        if((0 <= p+p && p+p <= max) && (visited.find(p+p) == visited.end())){ //p+p 방문안한경우
            visited.insert(p+p);
            pair<long long, string> addition = make_pair(p+p,op+"+");
            q.push(addition);
        }
        
        if((0 <= p-p && p-p <= max) && (visited.find(p-p) == visited.end())){ //p-p 방문안한경우
            visited.insert(p-p);
            pair<long long, string> substract = make_pair(p-p,op+"-");
            q.push(substract);
        }
        
        if((p != 0 && 0 <= p / p && p / p <= max) && visited.find(p/p) == visited.end()){ //p/p 방문안한경우
            visited.insert(p/p);
            pair<long long, string> divide = make_pair(p/p,op+"/");
            q.push(divide);
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