#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int calculaSuma(int num1, int num2) 
{
	int resultado;
	resultado = num1 + num2;
	return resultado;
}

int main() {
	
	int num1, num2;
	printf("Coloca numero a sumar: ");
	scanf("%d", &num1);
	printf("Coloca segundo numero a sumar: ");
	scanf("%d", &num2);	
	calculaSuma(num1, num2);	
	return 0;
}
