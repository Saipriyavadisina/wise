#include "bits/stdc++.h"
using namespace std;
int t,n,m,x;
int main(){
	scanf("%d",&t);
	while(t--){
		vector <vector <int>> a;
		vector <vector <long long>> dp;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",&m);
			a.push_back({});
			dp.push_back({});
			while(m--){
				scanf("%d",&x);
				a.back().push_back(x);
				dp.back().push_back(0);
			}
		}
		for(int i=1;i<n;i++){
			m=a[i-1].size();
			long long mx0=LLONG_MIN,mx1=LLONG_MIN;
			for(int j=0;j<m;j++){
				mx0=max(mx0,dp[i-1][(j+1)%m]+1ll*i*a[i-1][j]);
				mx1=max(mx1,dp[i-1][(j+1)%m]-1ll*i*a[i-1][j]);
			}
			m=a[i].size();
			for(int j=0;j<m;j++) 
			    dp[i][j]=max(mx0-1ll*i*a[i][j],mx1+1ll*i*a[i][j]);
		}
		printf("%lld\n",*max_element(dp.back().begin(),dp.back().end()));
	}
}
