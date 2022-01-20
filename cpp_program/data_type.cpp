#include <iostream>

using namespace std;

int main(){
    short int   a   = 0;
    int         b   = 0;
    long int    c   = 0;
    char        d[] = "abc";
    char        e   = 'a';
    bool        f   = true;
    size_t      g   = 0;
    string      h   = "abc";
    float       i   = 1.0;
    double      j   = 1.0;
    long double k   = 1.0;
    long        l   = 0;
    long long   m   = 0;

	cout<<"sizeof(short int):"  <<sizeof(a)<<endl;
	cout<<"sizeof(int):"        <<sizeof(b)<<endl;
	cout<<"sizeof(long int):"   <<sizeof(c)<<endl;
	cout<<"sizeof(char[]):"     <<sizeof(d)<<endl;
	cout<<"sizeof(char):"       <<sizeof(e)<<endl;
	cout<<"sizeof(bool):"       <<sizeof(f)<<endl;
	cout<<"sizeof(size_t):"     <<sizeof(g)<<endl;
	cout<<"sizeof(string):"     <<sizeof(h)<<endl;
	cout<<"sizeof(float):"      <<sizeof(i)<<endl;
	cout<<"sizeof(double):"     <<sizeof(j)<<endl;
	cout<<"sizeof(long double):"<<sizeof(k)<<endl;
	cout<<"sizeof(long):"       <<sizeof(l)<<endl;
	cout<<"sizeof(long long):"  <<sizeof(m)<<endl;

}
