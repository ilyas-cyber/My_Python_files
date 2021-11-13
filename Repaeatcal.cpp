#include <iostream>
#include <fstream>
#include <conio.h>
using namespace std;

class Punish{
	public:
		int voil1 ;
//		int voil3;
//		int voil4;
//		int voil5;
//		int voil6;
//		int voil7;
//		int voil8;
//		int voil9;
		
	void setPunish(){
			int voil1 ;
//		int voil3;
//		int voil4;
//		int voil5;
//		int voil6;
//		int voil7;
//		int voil8;
//		int voil9;
	}	
	void showPunish()
	{
	 cout<<"Pree any button to Show Rules for Trade:"
	 <<endl;
	 cin>>voil1;
	 
	 //Reading the file of "exam.txt"
	 
	 ifstream il;
	 string st, st2;
	 il.open("exam.txt");
//	 il>>st>>st2;
//	 cout<<st<<st2;
while(il.eof()==0){
	getline(il,st);
	cout<<st<<endl;
}

	 
	 
	}
};
class Log{
	public:
		int Profit;
		int Loss;
		
void setLog(){
	int Profit ;
	int Loss ;
}		
void showLog(){
	cout<<"Enter Your Profit Here: "<<endl;
	cin>>Profit;
	cout<<"Enter Your Loss Here "<<endl;
	cin>>Loss;
	cout<<"Your Profit and Loss Have Been Saved"<<endl;
	
	//Logging the Profit into the File
	int pr =Profit;
	int ls =Loss;
	ofstream in ("Newcal.cpp");
	in<<"\nThe Profit of Trade is:\t"<<pr
	  <<"\nThe Loss of Trade is:\t"<<ls;
	
}
		
		
};

class Date{
	public:
		int Day;
		int Month;
		int Year;

void setDate(){
	int Day;
	int Month;
	int Year;
}
void showDate(){
	cout<<"Enter the todays Day First"<<endl;
	cin>>Day;
	cout<<"Enter the current Month"<<endl;
	cin>>Month;
	cout<<"Enter the current Year"<<endl;
	cin>>Year;
	//Logging Date of the Trade
	int dy =Day;
	int mn =Month;
	int yr =Year;
	ofstream in ("Newcal.cpp");
	in<<"\nDay:\t"<<dy
	  <<"\nMonth:\t"<<mn
	  <<"\nYear:\t"<<yr<<endl;
}
	
//void showDate(){
//	cout<<"The Day in which you Traded:"<<Day
//	    <<endl; 
//	cout<<"The Month in which you Traded:"<<Month
//	    <<endl;
//	cout<<"The Year in which you Traded:"<<Year
//	    <<endl;	     
//}

};
int main() {
	Log d;
	d.setLog();
	d.showLog();
	Date d1;         //Creation of objects
	d1.setDate();
	Punish p;
	p.setPunish();
	p.showPunish();
//	d1.showDate();
	
//	string st = "Love You Harry Bahi";
//	ofstream in ("Newcal.cpp");
//	in<<st;
	
//	getch();
	return 0;
}
