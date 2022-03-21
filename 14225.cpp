#include <iostream>
#include <bitset>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;

//부분수열의 합인지 아닌지 판별
bool sums[2000009];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // 부분수열의 합 여부 배열 초기화
    memset(sums, false, 2000009*sizeof(bool));
    
    // input
    int n;
    cin >> n;

    vector<int> s(n);
    
    for(int i=0; i<n; i++){
        cin >> s[i];
    }
    
    // 비트마스크를 위한 bitset
    bitset<20> bit;
    
    // 부분수열의 합 비트마스킹
    for(int i=0; i<(1<<n); i++){
        
        bit = bitset<20>(i);
        int sum = 0;
        for(int j=0; j<n; j++){
            sum += (s[j]*bit[j]);
        }
        
        //부분수열의 합이면 true
        sums[sum] = true;
    }
    
    //부분수열의 합이 아닌것중에 가장 작은 값 출력
    for(int i=1;i<2000009;i++){
        if(!sums[i]){
            cout << i;
            break;
        }
    }

    return 0;
}