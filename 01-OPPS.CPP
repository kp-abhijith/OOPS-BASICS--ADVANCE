#include<iostream>
using namespace std;
class Student{
    public:
        string name;
        int rno;
        float gpa;
};
void print(Student s){
    cout << s.name
         << s.rno << s.gpa<<endl;
}

int main(){
    Student s1;
    s1.name = "kp abhijith";
    s1.rno = 37;
    s1.gpa = 7.8;
    Student s2;
    s2.name = "NIKHIL";
    s2.rno = 37;
    s2.gpa = 7.8;
    print(s1);
    print(s2);
}