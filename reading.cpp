#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
	
/*********Opening the files and Reading
 using constructor Methods*/

//	cout<<"ilyas bugti baloch";
//	string il;
//	ifstream in("waqar.txt");
//	getline(in,il );
//	cout<<il<<"\n";
//	getline(in,il );
//	cout<<il;
	
	
	
	/*********Opening the files and Reading
 using Open() function Methods*/
	
	
	string st1;
	ifstream il;
	il.open("waqar.txt");
//	il>>st1;
//	cout<<st1;
	getline(il, st1);
	cout<<st1<<"\n";
	getline(il, st1);
	
	cout<<st1;
////	get ch();
	return 0;
}
