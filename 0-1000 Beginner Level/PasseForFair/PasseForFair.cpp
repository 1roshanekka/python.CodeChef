#include <iostream>
#include <cmath>
#include <string>
#define MAX 100
using namespace std;



int main(){
    int t,n,k;
    string l[MAX];
    cin >> t ;
    for (int i = 0; i < t ; i++){
        cin >> n >> k ;
        if(k>=n+1){
            l[i] = "YES";
        }
        else{
            l[i] = "NO";
        }
    }

    for (int j = 0 ; j < t ; j++){
        cout << l[j] << endl;
    }
    
    return 0;
}
