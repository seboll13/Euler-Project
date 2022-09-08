#include <stdlib.h>
#include <time.h>
//#include <pthread.h>

#define NB_ITERATIONS 10e6

/**
 * @brief single threaded sum function
 * 
 * @param n upper bound
 * @return int sum of all integers smaller than n that are multiples of either 3 or 5
 */
double sum_multiples_3_or_5(double n) {
    double s = 0;
    clock_t start = clock();
    for (int i = 0; i < n; ++i)
        if (i % 3 == 0 || i % 5 == 0)
            s += i;
    clock_t end = clock();
    printf("Time of execution: %f [s]", (float)(end-start) / CLOCKS_PER_SEC);
    return s;
}



int main() {
    sum_multiples_3_or_5(NB_ITERATIONS);
    return 0;
}