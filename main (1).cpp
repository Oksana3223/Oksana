/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h></stdio.h>

int main (void)
{
    int a,b,c,d;
    scanf ("%d%d%d%d", &a,&b,&c,&d);
    int n=d-c;
    printf ("%s/n", (c-b != n || b-a != n )?
"False" : "True");
    

    return 0;
}