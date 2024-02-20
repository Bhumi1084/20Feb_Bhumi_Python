//Addition, Substraction, Multiplication, Division using Hybride Inheritance
//#include<iostream>
//using namespace std;
//class Variable{
//public:
//	float a, b, add, sub, mul, div;
//};
//
//class Add : public virtual Variable{
//public:
//	int addition(){
//		add = a + b;
//		return add;
//	}
//};
//
//class Sub : public virtual Variable{
//public:
//	int substraction(){
//		sub = a - b;
//		return sub;
//	} 
//};
//
//class Mul : public virtual Variable{
//public:
//	int multiplication(){
//		mul = a * b;
//		return mul;
//	}
//};
//
//class Div : public virtual Variable{
//public:
//	int division(){
//		if(b != 0){
//			div = a / b;
//			return div;
//		}
//		else{
//			cout<<"\nCan not divide by zero.";
//			return 0;
//		}
//	}
//};
//
//class D : public Add, public Sub, public Mul, public Div{
//public:
//	void disp(){
//		cout<<"\nAdd = "<<addition();
//		cout<<"\nSub = "<<substraction();
//		cout<<"\nMul = "<<multiplication();
//		cout<<"\nDiv = "<<division();
//	}
//};
//
//int main(){
//	D d1;
//	float n1, n2;
//	cout<<"\nEnter first value : ";
//	cin>>n1;
//	cout<<"\nEnter second value : ";
//	cin>>n2;
//	//Set the values of a and b before calling disp()
//	d1.a = n1;
//    d1.b = n2;
//	d1.disp();
//	return 0;
//}

#include<iostream>
using namespace std;

class Variable {
public:
    float a, b, add, sub, mul, div;
};

class Add : public virtual Variable {
public:
    int addition() {
        add = a + b;
        return add;
    }
};

class Sub : public virtual Variable {
public:
    int substraction() {
        sub = a - b;
        return sub;
    } 
};

class Mul : public virtual Variable {
public:
    int multiplication() {
        mul = a * b;
        return mul;
    }
};

class Div : public virtual Variable {
public:
    int division() {
        if(b != 0) {
            div = a / b;
            return div;
        } else {
            cout << "\nCan not divide by zero.";
            return 0;
        }
    }
};

class D : public Add, public Sub, public Mul, public Div {
public:
    // Constructor to set the values of a and b
    D(float n1, float n2) {
        a = n1;
        b = n2;
    }

    void disp() {
        cout << "\nAdd = " << addition();
        cout << "\nSub = " << substraction();
        cout << "\nMul = " << multiplication();
        cout << "\nDiv = " << division();
    }
};

int main() {
    float n1, n2;
    cout << "\nEnter first value : ";
    cin >> n1;
    cout << "\nEnter second value : ";
    cin >> n2;

    // Create an instance of D and set the values using the constructor
    D d1(n1, n2);

    d1.disp();
    return 0;
}

