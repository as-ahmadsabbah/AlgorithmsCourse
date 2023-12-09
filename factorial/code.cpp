#include <iostream>
#include <iomanip>
#include <chrono>

using namespace std;

    long long it_fac(int n) {
    long long f = 1;
    for (int i = 1; i <= n; ++i) {
        f *= i;
    }
    return f;
}

    long long rec_fac(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * rec_fac(n - 1);
}


template<typename Func>
double measureExecutionTime(Func func, int n) {
    auto start = chrono::high_resolution_clock::now();


    func(n);

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;

    return duration.count();
}

int main() {
    int n;
    cin>>n;


    double iterativeTime = measureExecutionTime(it_fac, n);
    cout << fixed << setprecision(6) << iterativeTime *1000000 << " seconds" << endl;


    double recursiveTime = measureExecutionTime(rec_fac, n);
    cout << fixed << setprecision(6) << recursiveTime*1000000 << " seconds" << endl;

    return 0;
}