#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define Renglones 4


int renglones = 4; /* sustituir el número de renglones en la tabla de conocimiento*/
float X[Renglones] [3] = {0,0,0,
			   0,1,1,
			   1,0,1,
			   1,1,0};/* Esta tabla contiene x1, x2 y D. Los valores deben ser asignados antes de ejecutar la Regla Delta, o leidos desde el teclado*/
float w0, w1, w2, v0, v1, v2, t0, t1, t2;
float Alfa = 0.01 ;     /* se puede variar el tamaño de paso */
float DeltaTotal, Delta, E1, E2;
int iteraciones, i;
int S,suma1, suma2;
int  f( float valor );

int main (){
	//srand(time(NULL));
	w0 = ((rand()%201)/100)-1;
	w1 = ((rand()%201)/100)-1;
	w2 = ((rand()%201)/100)-1;
	v0 = ((rand()%201)/100)-1;
	v1 = ((rand()%201)/100)-1;
	v2 = ((rand()%201)/100)-1;
	t0 = ((rand()%201)/100)-1;
	t1 = ((rand()%201)/100)-1;
	t2 = ((rand()%201)/100)-1;

	iteraciones = 0;
	do { 
		DeltaTotal = 0;
		for (i=0; i<Renglones;i++) {   
			suma1 = f(*X[i,0]*w1 + *X[i,1]*w2 +w0);	
			suma2 = f(*X[i,0]*v1 + *X[i,1]*v2 +v0);
			S= f(suma1*t1 + suma2*t2 + t0);
			Delta = *X[i,2] -S;
			E1 = Delta*t1;
			E2 = Delta*t2;
			
			w0 = w0 +Alfa* E1;
			w1 = w1 + Alfa* E1*(*X[i,0]);
			w2 = w2 + Alfa* E1*(*X[i,1]);

			v0 = v0 +Alfa* E2;
			v1 = v1 + Alfa* E2*(*X[i,0]);
			v2 = v2 + Alfa* E2*(*X[i,1]);

			t0 = t0 +Alfa * Delta;
			t1 = t1 + Alfa * Delta*suma1;
			t2 = t2 + Alfa * Delta*suma2;
		
			DeltaTotal = DeltaTotal + fabs(Delta);
		}
		iteraciones++;
	} while ((DeltaTotal==0)|| (iteraciones>=200));/* 200 puede ser cambiado */

	if (iteraciones < 200){ 
		printf ("SOLUCIÓN: W0: %f \n W1: %f \n W2: %f \n", w0,w1,w2);
		printf ("V0: %f \n V1: %f \n V2: %f \n", v0,v1,v2);
		printf ("T0: %f \n T1: %f \n T2: %f \n", t0,t1,t2);
	}else{
		printf ("NO SE ENCONTRÓ SOLUCIÓN.  Inténtelo nuevamente");
	}
		

}

/* Definición de la función escalón 0-1 */
int f ( float valor ){ 
	if (valor <0) 
		return (0);
	else 
		return(1);
}
