#include <iostream>

using namespace std;

int n;
int a[12];
int op[4]; // + - * /
int maxs = -2147483640;
int mins = 2147483640;

void solve(int index, int num){
	
	if(index == n) return;
	
	if(index == (n-1)){
		if(maxs < num) maxs = num;
		if(mins > num) mins = num;
	}
	
	for(int i=0;i<4;i++){
		
		if(op[i] > 0){
			op[i]--;
			switch(i){
				case 0:
					solve(index+1,num+a[index+1]);
					break;
				case 1:
					solve(index+1,num-a[index+1]);
					break;
				case 2:
					solve(index+1,num*a[index+1]);
					break;
				case 3:
					solve(index+1,num/a[index+1]);
					break;
			}
			op[i]++;
		}
	}
	
	
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	
	cin >> n;
	
	for(int i=0;i<n;i++)
		cin >> a[i];
	
	for(int i=0;i<4;i++)
		cin >> op[i];

	solve(0,a[0]);
	cout << maxs << '\n' << mins << '\n';
}