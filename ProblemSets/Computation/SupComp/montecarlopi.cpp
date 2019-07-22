#include <stdio.h>
#include <random>
#include <iostream>
using namespace std;

int main()
{
	long count_s = 0;
	long count_c = 0;
	long i;
	long N;
	double x;
	double y;
	double pi;

	cout << "Enter the number of random nos N: ";
	cin >> N;
	for (i=0; i<N; i++) {
		x = ((double) rand()/RAND_MAX);
		y = ((double) rand()/RAND_MAX);
		count_s++;
		if ((x*x + y*y)<=1.0) {
			count_c++;
		}	
	}
	cout << " Sq= " << count_s << " Ci= " << count_c << "\n";
	pi = ((double) count_c / count_s) * 4.0;
	cout << "Simulated for " << N << " random numbers.\n Pi = " << pi << "\n";
	return 0;
}
