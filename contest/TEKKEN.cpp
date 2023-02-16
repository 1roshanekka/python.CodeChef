#include <iostream>
#include <cmath>

using namespace std;

#define MAX 1000;

int main(){

    int t ;
    cin >> t ;
    
    for ( int i = 0 ; i < t ; i++){ 
        int a, b, c;
        cin >> a >> b >> c;
        //b & c
        int fight1 = std::min(b, c);
        b = b -  fight1;
        c = c - fight1 ;
        // c & a
        int fight2 = std::min(c, a); 
        a = a - fight2 ;
        c = c - fight2 ;
        // a & b
        int fight3 = std::min(a, b); 
        a = a - fight3 ;
        c = c - fight3 ;            
        

        if(a>0){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
            

        }


    }

    return 0;
}