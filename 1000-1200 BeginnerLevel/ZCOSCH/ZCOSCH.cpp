#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int x;
	cin >> x ;
	if( (1<=x) && (x<=50) ){
	  cout << 100 << endl;
  }
  else if ( (51<=x) && (x<=100) ){
	  cout << 50 << endl;
  }
  else{
    cout << 0 << endl;
  }
	return 0;
}

