// Hard 3: Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
// C++ Solution 
#include <iostream>

using namespace std;

int main()
{
   int n,temp, c=0;
   cin>>n;
   for(int i=0;i<=n;i++){
       temp=i;
       while(temp!=0){
           int a=temp%10;
           temp=temp/10;
           if(a==1){
             c++;  
           }
       }
   }
   cout<<c;

    return 0;
}