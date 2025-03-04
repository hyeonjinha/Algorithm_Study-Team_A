#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin>>n;

    int res=-1;
    int a=n/5;

    for(int i=a; i>=0; i--){
        int x=n-i*5;
        if(x%3==0){
            res=i+x/3;
            break;
        }
    }

    cout<<res;
}