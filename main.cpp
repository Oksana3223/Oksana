/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

int main()
{
    double a,b;
    cout << "Введите длину первой стороны параллелограмма (a):";
    cin >> a;
    
    cout << "Введите длину второй стороны параллелограмма (b):";
    cin >> b;
    
    if (a<=0 || b<=0) {
    cout << "Длины сторон должны быть положительными числами." << endl;
    return 1; 
    }
    
    double area = a*b;
    
    cout << "Площадь параллелограмма:" << area << endl;

    return 0;
}