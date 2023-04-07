#include <iostream>
#include <cmath>
#include <string>

#define MAX 100

using namespace std;

int main(){
    int t;
    cin >> t;  
    int arr[MAX];  
    
    for( int i = 0 ; i < t ; i++){
        int x, y;
        cin >> x >> y;
        int choc = 2 * x;
        int cand = 5 * y;
        
        if( choc > cand ){
            arr[i] = 1;
        }
        else if( choc < cand ){
            arr[i] = -1;
        }
        else{
            arr[i] = 0;
        }
    }

    for( int j = 0 ; j < t ; j++){
        if(arr[j]==1){
           cout << "Chocolate" << endl; 
        }
        else if (arr[j]==-1){
            cout << "Candy" << endl;
        }
        else{
            cout << "Either" << endl;
        }
        
    }
}
