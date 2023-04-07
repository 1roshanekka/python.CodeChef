#include <iostream>
#include <string>
#include <cmath>

#define MAX 1000

using namespace std;

int main(){
    int t ;
    cin >> t ;
    string arr[MAX];

    int a, b ;

    for ( int i = 0 ; i < t ; i++ ){
        cin >> a >> b ;
        if( (a+b)%2==0 ){
            arr[i] = "YES" ;
        }
        else{
            arr[i] = "NO" ;
        }
    }

    for (int j = 0; j < t; j++){
        cout << arr[j] << endl ;
    }
    
    return 0 ;
}