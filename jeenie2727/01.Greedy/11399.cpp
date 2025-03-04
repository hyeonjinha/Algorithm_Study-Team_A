#include <iostream>
#include <algorithm>

using namespace std;

int arr[1003];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin>>n;
    
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    
    sort(arr, arr+n);
    
    int res=0;
    
    for(int i=0; i<n; i++){
        res+=arr[i]*(n-i);
    }
    
    cout<<res;
}