#include<bits/stdc++.h>
using namespace std;
int main() {
	//code
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
	    int k,n;
	    cin>>k>>n;
	    int a[n];
	    for(int i=0;i<n;i++)
	        cin>>a[i];
	    cout<<n<<k<<endl;
	    int dp[n+1][k+1]={0};
	    for(int i=0;i<=k;i++)
	    {
	    	
	        int dif=INT_MIN;
	        cout<<"f1";
	        for(int l=0;l<n;l++)
	        {
	        	cout<<"#"<<l<<"#";
	        	cout<<"f2";
	            if(i==0 || l==0)
	                dp[i][l]=0;
	            else
				{
	            	cout<<"f3";
	            dif=max(dif,dp[i-1][l-1]-a[l-1]);
	            dp[i][l]=max(dif+a[l],dp[i][l-1]);
	            }
	        }
	    }
	    cout<<"f4";
	    cout<<dp[k][n-1]<<endl;
	}
	return 0;
}
