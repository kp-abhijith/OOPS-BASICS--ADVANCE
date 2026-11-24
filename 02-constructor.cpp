#include <iostream>
using namespace std;
class Student
{
public:
    string name;
    int rno;
    float gpa;
    Student(string name,int rno,float gpa){
        this->gpa = gpa;
        this->name = name;
        this->rno = rno;
    }
    void print(Student obj){
        cout << obj.name << " " << obj.gpa << endl;
    }
};
int main(){
    Student s("hari", 77, 7.1);
    s.print(s);
}