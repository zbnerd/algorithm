#include <iostream>

int n,m;
int wood_str[5][5];
bool used[5][5];
int ans;

using namespace std;

int max(int a, int b){
    return (a > b)? a : b;
}

bool in_bound(int i, int j){
    return (0 <= i && i < n) && (0 <= j && j < m) && !used[i][j];
}

int first(int i, int j){
    return 2*wood_str[i][j] + wood_str[i+1][j] + wood_str[i][j+1];
}

int second(int i, int j){
    return 2*wood_str[i][j] + wood_str[i-1][j] + wood_str[i][j+1];
}

int third(int i, int j){
    return 2*wood_str[i][j] + wood_str[i-1][j] + wood_str[i][j-1];
}

int fourth(int i, int j){
    return 2*wood_str[i][j] + wood_str[i+1][j] + wood_str[i][j-1];
}

void back_tracking(int i, int j, int str){
    
    if(j == m){
        j = 0;
        i++;
    }
    
    if(i == n){
        ans = max(ans, str);
        return;
    }
    
    int cur_str = 0;
    
    if(!used[i][j]){
        if(in_bound(i+1,j) && in_bound(i,j+1)){
            used[i][j] = true;
            used[i+1][j] = true;
            used[i][j+1] = true;
            
            cur_str = str+first(i,j);
            back_tracking(i,j+1,cur_str);
            
            used[i][j] = false;
            used[i+1][j] = false;
            used[i][j+1] = false;
        }
        
        if(in_bound(i-1,j) && in_bound(i,j+1)){
            used[i][j] = true;
            used[i-1][j] = true;
            used[i][j+1] = true;
            
            cur_str = str+second(i,j);
            back_tracking(i,j+1,cur_str);
            
            used[i][j] = false;
            used[i-1][j] = false;
            used[i][j+1] = false;
        }
        
        if(in_bound(i-1,j) && in_bound(i,j-1)){
            used[i][j] = true;
            used[i-1][j] = true;
            used[i][j-1] = true;
            
            cur_str = str+third(i,j);
            back_tracking(i,j+1,cur_str);
            
            used[i][j] = false;
            used[i-1][j] = false;
            used[i][j-1] = false;
        }
        
        if(in_bound(i+1,j) && in_bound(i,j-1)){
            used[i][j] = true;
            used[i+1][j] = true;
            used[i][j-1] = true;
            
            cur_str = str+fourth(i,j);
            back_tracking(i,j+1,cur_str);
            
            used[i][j] = false;
            used[i+1][j] = false;
            used[i][j-1] = false;
        }
    }
    
    back_tracking(i,j+1,str);
    return;
}

int main()
{
    cin >> n >> m;
    
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin >> wood_str[i][j];
        }
    }
    
    if(n == 1 || m == 1)
        cout << 0;

    else {
        back_tracking(0,0,0);
        cout << ans;
    }
    
    return 0;
}
