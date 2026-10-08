// #include<iostream>
// using namespace std;
// int main(){
//     cout<<"Hello world!"<<endl;
//     return 0;
// }


#include<iostream>
#include<ctime>
using namespace std;
int main (){
srand((unsigned)time(NULL));
int num = rand()%100+1;
while(1){
int x;
cout<<"请输入数字："<<endl;
cin>>x;
if(x>num){
    cout<<"猜大了"<<endl;   
}

else if(x<num){
    cout<<"猜小了"<<endl;
}
else{
    cout<<"恭喜你，猜对了"<<endl;
    break;
}
}
}
