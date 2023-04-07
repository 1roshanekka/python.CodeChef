#include <iostream>
#include <string>
#include <cmath>

#define max 1000
using namespace std;

int main() {
  int t ;
  cin >> t ;
  for( int i = 0 ; i < t ; i++ ) {
     int arr[max];
     int n ;
     int b ;
     cin >> n >> b ;
     int area = 0;
     int flag = 0;
     int price = 0;
     int count = 0;
     for ( int j = 0 ; j < n ; j++ ) {
        int w;
        int h;
        int p;
        // first check if the price comes under budget
        if ( !( p > b ) ) {
          // its under budget
          // now check for larger area
          
          if( (w*h) > area ) {
            area = w*h ;
            // now output this larger screen price 
            price = p;
            // this will save the latest largest screen price
          }
        }
        else {
          cout << "no tablet" << endl;
        }
     }
     cout << price << endl;
  }
}


