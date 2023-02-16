#include <iostream>
#include <cmath>
#include <string>

using namespace std;

#define MAX 1000;

int main(){

    int t ;
    cin >> t ;

    for ( int i = 0 ; i < t ; i++){
        int n, m;
        cin >> n >> m;

        string a;
        string b;
        cin>>a>>b;
        string ab=a+b;
        int arr[26]={0};
        for(int i=0;i<n+m;i++)
        {
            arr[(int)ab[i]-97]++;
        }
        // for(int i=0;i<26;i++)
        // {
        //     cout<<arr[i]<<" ";
        // }
        int c=0;
        for(int i=0;i<26;i++)
        {
            if(arr[i]%2!=0)
            {
                c++;
            }
        }
        if(c>1)
            cout<<"NO\n";
        if(c==1)
                cout<<"YES\n";
        if(c==0)
            cout<<"YES\n";
    }
    return 0;
}