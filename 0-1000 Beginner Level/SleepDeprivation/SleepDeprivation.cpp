#include <iostream>
#include <string>
using namespace std;

#define MAX 100

int main() {
    string store[MAX];
    int t;
    cin >> t;
    for ( int i = 0 ; i < t ; i++){
        int x;
        cin >> x;
        if( x < 7 ){
            store[i] = "YES";
        }
        else{
            store[i] = "NO";
        }
    }
    
    for ( int i = 0 ; i < t ; i++){
        cout << store[i] << endl;
    }
	// your code goes here
	return 0;
}
