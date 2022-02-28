#include <iostream>
#include <string>
#include <vector>

using namespace std;

char s[11][11];

int n;
int a[11];

bool check(int index){
	int tmp = 0;
	
	for(int i=index;i>-1;i--){
		tmp += a[i];
		if(s[i][index] == '+' && tmp <= 0) return false;
		if(s[i][index] == '-' && tmp >= 0) return false;
		if(s[i][index] == '0' && tmp != 0) return false;
	}
	return true;
}

void recursive(int index){
	if(index == n){
		for(int i=0;i<n;i++){
			cout << a[i] << ' ';
		}
		exit(0);
	}
	
	if (s[index][index] == '0'){
		a[index] = 0;
		recursive(index+1);
	}
	
	else {
		if (s[index][index] == '-'){
			for(int i=-10;i<0;i++){
				a[index] = i;
				if(check(index)) recursive(index+1);
			}
		}
		
		if (s[index][index] == '+'){
			for(int i=1;i<11;i++){
				a[index] = i;
				if(check(index)) recursive(index+1);
			}
		}
		
	}
}

int main(){
	
	ios_base::sync_with_stdio(false); cin.tie(0);
	
	string operators;
	
	cin >> n >> operators;
	
	int idx = 0;

    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            s[i][j] = operators[idx++];
        }
    }
    
    recursive(0);
	
	return 0;
}