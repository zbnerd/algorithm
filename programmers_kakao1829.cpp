#include <vector>
#include <queue>

using namespace std;

int number_of_area = 0;
int max_size_of_one_area = 0;

vector<vector<int>> bfs(vector<vector<int>> picture, pair<int, int> starting_point, int color, int m, int n){
    int si = starting_point.first; int sj = starting_point.second;
    int di[4] = {1,-1,0,0}; int dj[4] = {0,0,1,-1}; 
    
    queue<pair<int, int>> q;
    
    q.push(starting_point);
    picture[si][sj] = 0;
    int size_of_area = 1;
    
    
    while(!q.empty()){
        pair<int, int> poped = q.front(); q.pop();
        int i = poped.first; int j = poped.second;
        
        for(int k=0;k<4;k++){
            int ni = i+di[k]; int nj = j+dj[k];
            if(!(0 <= ni && ni < m && 0 <= nj && nj < n)) continue;
            if(picture[ni][nj] != 0 && picture[ni][nj] == color){
                size_of_area++;
                pair<int,int> adj_point = make_pair(ni,nj);
                picture[ni][nj] = 0;
                q.push(adj_point);
            }
        }
    }
    if(size_of_area > max_size_of_one_area) max_size_of_one_area = size_of_area;
    
    return picture;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    
    number_of_area = 0;
    max_size_of_one_area = 0;
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(picture[i][j] != 0){
                number_of_area++;
                pair<int, int> starting_point = make_pair(i,j);
                picture = bfs(picture, starting_point, picture[i][j], m, n);
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}