#include <iostream>
#include <cmath>
#include <string>
using namespace std;
#define MAX 1000

int main(){
    int t;
    int arr[MAX];

    cin >> t ;

    string result[MAX];

    for ( int i = 0 ; i < t ; i++){
        cin >> arr[i];
        if(arr[i]>30){
            result[i] = "YES";
        }
        else{
            result[i] = "NO";
        }

    }

    for ( int j = 0 ; j < t; j++){
        cout << result[j] << endl;
    }
    return 0;
}