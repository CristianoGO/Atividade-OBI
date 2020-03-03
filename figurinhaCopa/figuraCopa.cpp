#include<locale.h>
#include<stdlib.h>
#include<stdio.h>

/* Autor Cristiano */

int main(){
	setlocale(LC_ALL, "Portuguese_Brazil");
	
	int n, c, m, x, y;
    int album[100], carimbada[100];
    int res = 0;
    
    scanf("%d", &n);
    scanf("%d", &c);
    scanf("%d", &m);
    
    for(int i = 1; i <= n; i++){
    	carimbada[i] = album[i] = 0;
	}
	for(int j = 0; j < c; j++){
		scanf("%d", &x);
		carimbada[x] = 1;
	}
	for(int k = 0; k < m; k++){
		scanf("%d", &y);
		album[y] = 1;
	}
	for(int l = 1; l <= n; l++){
		if(album[l] == 0 && carimbada[l] == 1){
			res++;
		}
	}
	printf("%d", res);

	return 0;
}

