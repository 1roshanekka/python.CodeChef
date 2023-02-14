#include <iostream>
#include <cmath>
#include <string>

#define MAX 100

using namespace std;

int main(){
    int t ;
    cin >> t ;
    int output[MAX];
    for ( int i = 0 ; i < t ; i++){
        int n ;

        cin >> n ;
        int arr[MAX] = { 0 };
        int arx[MAX];
        // cout<<arr[0];
        int flag = 0;
        int buff = 0;
        for ( int j = 0 ; j < n ; j++){
            int x;
            cin >> x;
            // arr[x]++ ;
            arr[j] = x;    
        }
        
        int top2 = 0;

        for (int s = 0 ; s < n ; s++){
            int top = 0;
            for (int d = 0 ; d < n ; d++){
                if(arr[d]==arr[s]){
                    top = top +1;
                }
            }
            if( top >= top2){
                top2 = top;
            }
        }

        // for ( int l = 0 ; l < n ; l ++){
        //     cout << arr[l] << endl;
        // }
        // cout << "\n lol" << endl;
        
        // int jyada = 0;
        // for (int k = 0; k < MAX; k++){
        //     if(arx[k]>=jyada){
        //         jyada = arr[k];
        //     }
        // }
        // cout << jyada << "this\n" << endl;
        // cout << n-jyada << endl ;
        // output[i] = n - jyada;
        output[i] = n-top2 ;

        //roshan bhai suggested this as judge can identify itseld
        // cout << n-top2 << endl;

    }
    for (int q = 0; q < t; q++){
        cout << output[q] << endl ;
    }
    
    return 0 ;
}