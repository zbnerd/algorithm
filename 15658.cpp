#include <iostream>
#include <vector>

using namespace std;

int n;
int nums[12];
int operators[4];

int max_value = -2147483647;
int min_value = 2147483647;

void calculate(int i, int cur_value){
    if(i == (n-1)){
        if(max_value < cur_value) max_value = cur_value;
        if(min_value > cur_value) min_value = cur_value;
        return;
    }
    
    if(operators[0] > 0){ // +
        operators[0]--;
        calculate(i+1, cur_value+nums[i+1]);
        operators[0]++;
    }
    
    if(operators[1] > 0){ // -
        operators[1]--;
        calculate(i+1, cur_value-nums[i+1]);
        operators[1]++;
    }
    
    if(operators[2] > 0){ // *
        operators[2]--;
        calculate(i+1, cur_value*nums[i+1]);
        operators[2]++;
    }
    
    if(operators[3] > 0){ // /
        operators[3]--;
        calculate(i+1, cur_value/nums[i+1]);
        operators[3]++;
    }
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    
    cin >> n;
    
    for(int i=0; i<n; i++) cin >> nums[i];
    for(int i=0; i<4; i++) cin >> operators[i];
    
    calculate(0, nums[0]);

    cout << max_value << '\n' << min_value;

    return 0;
}
