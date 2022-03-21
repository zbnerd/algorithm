#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;

int n;

int bfs(pair<int, int> start, pair<int, int> end){
	int visited[201][201];
    for(int i=0;i<201;i++) memset(visited[i], -1, sizeof(int) * 201);
    
	visited[start.first][start.second] = 0;
	queue<pair<int, int> > q;
	
	int dr[6] = {-2,-2,0,0,2,2};
	int dc[6] = {-1,1,-2,2,-1,1};
	
	q.push(start);
	
	while(!q.empty()){
		pair<int, int> poped = q.front(); q.pop();
		int r = poped.first, c = poped.second;
		
		for(int k=0;k<6;k++){
			int nr = r+dr[k], nc = c+dc[k];
			
			if((0 <= nr && nr < n) && (0 <= nc && nc < n)){
				if(visited[nr][nc] == -1){
					visited[nr][nc] = visited[r][c] + 1;
					q.push(make_pair(nr, nc));
				}
			}
		}
	}
	
	return visited[end.first][end.second];
}

int main(){
	
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int r1, c1, r2, c2;
	cin >> n >> r1 >> c1 >> r2 >> c2;

	cout << bfs(make_pair(r1, c1), make_pair(r2, c2));
	return 0;
}