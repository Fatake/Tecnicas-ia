#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define Renglones 2

//int Renglones = 2; /* sustituir el número de renglones en la tabla de conocimiento*/
float X[Renglones][5] = { 0,1,0,1,0,1,0,1,0,1};/* Esta tabla contiene x1, x2 y D. Los valores deben ser asignados antes de ejecutar la Regla Delta, o leidos desde el teclado*/
float w0, w1, w2, w3, w4, v0, v1, v2, v3,  t0, t1, t2, t3, n0,n1, n2;
float m0, m1, m2, m3, p0, p1, p2, q0, q1, q2, r0, r1, r2, r3;
float k0, k1, k2;

int S,suma1, suma2;
int suma3,suma4, suma5, suma6, suma7, suma8;
float Alfa = 0.01;       /* se puede variar el tamaño de paso */
float DeltaTotal, Delta, E1, E2;
float E3, E4, E5, E6, E7, E8;
int iteraciones, i;
float aux1;

int  f( float valor );

int main (){
//srand(time(NULL));
w0=((rand()%201)/100)-1;
w1=((rand()%201)/100)-1;
w2=((rand()%201)/100)-1;
w3=((rand()%201)/100)-1;
w4=((rand()%201)/100)-1;
v0=((rand()%201)/100)-1;
v1=((rand()%201)/100)-1;
v2=((rand()%201)/100)-1;
v3=((rand()%201)/100)-1;
t0=((rand()%201)/100)-1;
t1=((rand()%201)/100)-1;
t2=((rand()%201)/100)-1;
t3=((rand()%201)/100)-1;
n0=((rand()%201)/100)-1;
n1=((rand()%201)/100)-1;
n2=((rand()%201)/100)-1;
m0=((rand()%201)/100)-1;
m1=((rand()%201)/100)-1;
m2=((rand()%201)/100)-1;
m3=((rand()%201)/100)-1;
p0=((rand()%201)/100)-1;
p1=((rand()%201)/100)-1;
p2=((rand()%201)/100)-1;
q0=((rand()%201)/100)-1;
q1=((rand()%201)/100)-1;
q2=((rand()%201)/100)-1;
r0=((rand()%201)/100)-1;
r1=((rand()%201)/100)-1;
r2=((rand()%201)/100)-1;
r3=((rand()%201)/100)-1;
k0=((rand()%201)/100)-1;
k1=((rand()%201)/100)-1;
k2=((rand()%201)/100)-1;

iteraciones=0;
do{ 
	DeltaTotal = 0;
	for (i=0; i<Renglones;i++)                 /* Usa todos los renglones de la tabla*/
	{ 
		 	
		suma1 = f(w0+*X[i,0]*w1+*X[i,3]*w2+*X[i,1]+w3);	
		suma2 = f(v0+*X[i,2]*v1 + *X[i,1]*v2 + *X[i,3]*v3);
		suma3 = f (t0 +*X[i,2]*t1 + *X[i,3]*t2 + *X[i,4]*t3);	
		suma4 = f(n0 +suma1*n1 + suma3*n2);
		suma5 = f(m0 + suma1*m1 + suma2*m2 + suma3*m3);	
		suma6 = f(p0 + suma1*p1 + suma3*p2);
		suma7 = f(q0 + suma4*q1 + suma5*q2);	
		suma8 = f(r0 + suma5*r1 + suma4*r2 + suma6*r3);
		
		S = f(k0 + suma7*k1 + suma8*k2);

		Delta = *X[i,5]-S;
		E1 = E4*n2 + E5*m3 + E6*p2;
		E2 = E5*m2;
		E3 = E4*n2 + E5*m3 + E6*p2;
		E4 = E7*q1 + E8 * r2;
		E5 = E7*q2 + E8*r1;
		E6 = E6*r3;
		E8 = Delta*k1;
		E7 = Delta*k2;
		
		w0 = w0 + E1;
		w1 = w1 + E1*(*X[i,0]);
		w2 = w2 + E1*(*X[i,3]);
		w3 = w3 + E1*(*X[i,1]);
	
		v0 = v0 + E2;
		v1 = v1 + E2*(*X[i,2]);
		v2 = v2 + E2*(*X[i,1]);
		v3 = v3 + E2*(*X[i,3]);

		t0 = t0 + E3;
		t1 = t1 + E3*(*X[i,2]);
		t2 = t2 + E3*(*X[i,3]);
		t3 = t3 + E3*(*X[i,4]);

		n0 = n0 + E4;
		n1 = n1 + E4*suma1;
		n2 = n2 + E4*suma3;

		m0 = m0 + E5;
		m1 = m1 + E5*suma1;
		m2 = m2 + E5*suma2;
		m3 = m3 + E5*suma3;

		p0 = p0 + E6;
		p1 = p1 + E6*suma1;
		p2 = p2 + E6*suma3;
		
		q0 = q0 + E7;
		q1 = q1 + E7*suma4;
		q2 = q2 + E7*suma5;

		r0 = r0 + E8;
		r1 = r1 + E8*suma5;
		r2 = r2 + E8*suma4;
		r3 = r3 + E8*suma6;
		
		k0 = k0 + Delta;
		k1 = k1 + Delta*suma7;
		k2 = k2 + Delta*suma8;
	
		DeltaTotal = DeltaTotal + fabs(Delta);
	}
	iteraciones++;
} while ((DeltaTotal==0)|| (iteraciones>=50));/* 200 puede ser cambiado */

if (iteraciones < 50){
	printf ("SOLUCIÓN: W0: %f \n W1: %f \n W2: %f \n W3: %f  \n", w0,w1,w2,w3);
	printf ("V0: %f \n V1: %f \n V2: %f \n V3: %f  \n", v0,v1,v2,v3);
	printf ("T0: %f \n T1: %f \n T2: %f \n T3: %f  \n", t0,t1,t2,t3);
	printf ("N0: %f \n N1: %f \n N2: %f  \n", n0,n1,n2);
	printf ("M0: %f \n M1: %f \n M2: %f \n M3: %f  \n", m0,m1,m2,m3);
	printf ("P0: %f \n P1: %f \n P2: %f   \n", p0,p1,p2);
	printf ("Q0: %f \n Q1: %f \n Q2: %f   \n", q0,q1,q2);
	printf ("R0: %f \n R1: %f \n R2: %f \n R3: %f  \n ", r0,r1,r2,r3);
	printf ("K0: %f \n K1: %f \n K2: %f  \n ", k0,k1,k2);
	
}	
else
	printf ("NO SE ENCONTRÓ SOLUCIÓN.  Inténtelo nuevamente");

}/*  FIN  DE LA REGLA DELTA GENERALIZADA */

/* Definición de la función escalón 0-1 */
int f ( float valor ){ 
	if (valor <0) 
		return (0); 
	else 
		return(1);
}

