#include <iostream>
#include <string>

#include <cmath>
#define MAX 1000

using namespace std;

int main(){
    int t;
    cin >> t;
    
    for ( int i = 0 ; i < t ; i++){
        int n;
        string s;

        cin >> n >> s;

        int count = 0; int arr[n]; int arrCount = 0;
        /*
        while(cut>0){//back count
            // char check = s.substr(0,1);
            char check = s.at(cut);

            // if 4 or more consonant in a row then its NO
            if((check=='a' || check=='e' || check=='i' || check=='o' || check=='u') == 0){ //if false
                arr[arrCount] = cut;
                arrCount += 1;
            }
            s = s.substr(0,n-1); //cut string

            cut -= 1; //update of loop
            // s = s.substr(0,cut);
        }
        */
        while(count<n){ // FUCK here I did was count<t and wasted my fucking 1 hour
            char check = s.at(count);
            // cout << check << endl;
            // if 4 or more consonant in a row then its NO
            if((check=='a' || check=='e' || check=='i' || check=='o' || check=='u') == false){ //if false
                arr[arrCount] = count;
                arrCount += 1;
                // cout << count << endl;
            }
            count ++;
        }
        // cout << "good" << endl;
        //correct tille here

        int size = sizeof(arr);
        /*
        
        cout << size << endl;
        cout << sizeof(arr[0]) << endl;

        */

        
        
        int flag = 0;
        arr[n] = 0; //correct exception
        // cout << "good" << endl;
        int perfect = 0;
        //print array
        // for (int j = 0 ; j < n /*problem here i guess*/ ; j++){
        //     cout << arr[j] ;
        // }
        for ( int j = 0 ; j < n /*problem here i guess*/ ; j++){
            if( ( (arr[j+1]-arr[j])==1) == 0){//if false
                perfect = 0;
            }
            else{
                perfect += 1;
                if(perfect==4){//all 4 consonant in a row
                    flag = 1;
                    break;
                }
            }
            // cout << perfect << endl;
        }
        // cout << "good" << endl;
        //correct till here

        if(flag==1){//all consonant and not speakable
            cout << "NO" << endl;
        }
        else{//speakable
            cout << "YES" << endl;
        }
    }

    return 0;

}