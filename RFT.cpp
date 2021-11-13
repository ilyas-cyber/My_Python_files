#include <iostream>
#include <iomanip>
#include <fstream>
//Rules for Trade (RFT):
using namespace std;
	
class Punish{
	public:
		int voil1 ;
		
		
	void setPunish(){
			int voil1 ;
			
			
	}	
	void showPunish(){
	cout<<"\n\n"<<endl;
	 cout<<"Note: ***Voilation of any trade rule will \n     led Bonus Trade suspend for a month"; 
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


int main() {
//Stoploss Plan:
   cout<<"\t**** Rules for Trade (RFT)****"<<endl;
	cout<<"1:Always use Stoploss!"<<endl;
   cout<<"2:Your fixed Stoploss is 2.5 USDT"
	    <<endl;
	float stop_loss = 2.5;
//Take profit plan:
   float T_K_P = 5;
	char Take_Profit[50]="3:Set your Take Profit in USDT";
   cout<<Take_Profit<<"\t"<<"Maximum"<<"\t"<<T_K_P<<endl;
//No Of Trades plan:
   cout<<"4:Always do one Trade!"<<endl;
   int Bonus_Trade = 1;
   cout<<"5:IF your trade went on your side then  "
	    <<"You will get"<<setw(2)
	    <<setw(2)<<Bonus_Trade<<"\n"<<"\tBonus_Trade"
	    <<setw(2)<<endl;
//Reason of Hitting stoploss:
   char reson_hit_stoploss[50] = "6:Reason of stoploss hitting?";	    
   cout<<reson_hit_stoploss<<endl;
//Logic of Taking profit:
   char lg_of_tp[50] ="7:Logic of Taking Profit?";
	cout<<lg_of_tp<<endl;
	cout<<"\n"<<endl;
//--------------------------------------------------------------	

//*******Rules for Bonus Trade(RFBT)******	
	char RFBT[50] = "\t****Rules for Bonus Trade(RFBT)***";
	cout<<RFBT<<endl;
	cout<<"->All The Rules for Trade (RFT) are applied"
	<<endl;
	cout<<"\tEXECPET"<<endl;
   cout<<""<<Take_Profit<<"\t"<<T_K_P
	<<"\t (Optional)"
	<<endl;
	cout<<"\n"<<endl;
	

//***************Repeatcal.cpp****** Data****
   Log d;
	d.setLog();
	d.showLog();
	Punish p;
	p.setPunish();
	p.showPunish();

//*****Using of If Else Satetments
//if()
	
	
	return 0;
}
