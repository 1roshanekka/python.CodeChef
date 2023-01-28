#include <stdio.h>

int main(){
    int T, N, M;
    scanf("%d", &T);
    int arr[T];

    for(int i = 0; i<T; i++){
        scanf("%d %d", &N, &M);
        arr[i] = N*M;
    }

    for(int j = 0; j<T; j++){
        printf("%d\n", arr[j]);
    }
}