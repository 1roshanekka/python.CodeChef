#include <iostream>
#include <cmath>

using namespace std;

#define MAX 1000;

int main(){

    int t ;
    cin >> t ;

    for ( int i = 0 ; i < t ; i++){
        int x, y , z;
        cin >> x >> y >> z;

        int totalSeats = 10*x;
        int demand = y;
        if(totalSeats>=demand){
            cout << z*demand << endl;
        }
        else{
            cout << z*totalSeats << endl;
            

        }


    }

    return 0;
}