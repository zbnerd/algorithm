#include <iostream>

using namespace std;

int r,c;
char board[20][20];
bool visited[26];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int ans = 0;

int max(int a, int b){
    return (a > b)? a : b;
}

void dfs(int x, int y, int depth){
    
    ans = max(ans, depth);
    
    // 4방향 dfs
    for(int i=0;i<4;i++){
        int nx = x+dx[i]; int ny = y+dy[i];
        if ((0 <= nx && nx < r) && (0 <= ny && ny < c)){
            if (visited[board[nx][ny] - 'A'] == false){
                visited[board[nx][ny] - 'A'] = true;
                dfs(nx, ny, depth+1);
                visited[board[nx][ny] - 'A'] = false;
            }
        }
        
        
    }
    
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    
    cin >> r >> c;
    
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin >> board[i][j];
        }
    }
    
    visited[board[0][0] - 'A'] = true;
    dfs(0,0,1);
    
    cout << ans;
    
    return 0;
}
