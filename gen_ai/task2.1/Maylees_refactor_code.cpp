/// @author Maylee Del Rio

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// ORIGINAL CODE
//int main() {
//    const double COMMISSION = 0.06;  //constant for the 6% Home commision
//    const double AGENT      = 0.015; //constant for the 3% agencies
//
//    string name;               //integer for homeowners last name
//    double sales_price;        //doublr for sale price
//    double agency_commission;  //double for agency price
//    double agent_commission;   //double for agent price
//
//    //user input for sales price and owners last name
//    cout << "Enter sales price of home and owner's last name: ";
//    cin >> sales_price
//        >> name;
//
//    //conversions to find agency/agent commisson from sales price
//    agency_commission = sales_price * COMMISSION;
//    agent_commission  = sales_price * AGENT;
//
//    //output of home owner, price of home, seller's cost and agent commision
//    cout << fixed
//         << showpoint
//         << setprecision(2);
//    cout << endl;
//    cout << left
//         << setw(20)
//         << "Home Owner"
//         << right
//         << setw(20)
//         << "Price of Home"
//         << setw(20)
//         << "Seller's Cost"
//         << setw(20)
//         << "Agent's Commission"
//         << endl;
//
//    cout << setw(80)
//         << setfill('-')
//         << '-';
//    cout << setfill(' ')
//         << ' '
//         << endl;
//
//    cout << setw(20)
//         << left
//         << setw(20)
//         << name
//         << right
//         << setfill('*')
//         << setw(20)
//         << sales_price
//         << setw(20)
//         << agency_commission
//         << setw(20)
//         << agent_commission
//         << endl;
//
//    // return statement
//    return 0;
//}


// refactored code by ChatGPT

int main() {
    constexpr double COMMISSION_RATE = 0.06;  // 6% commission rate
    constexpr double AGENT_RATE = 0.015;      // 1.5% agent commission rate

    string homeowner;
    double sales_price, agency_commission, agent_commission;

    // User input
    cout << "Enter sales price of home: ";
    cin >> sales_price;
    cin.ignore();  // Ignore newline character left in buffer

    cout << "Enter homeowner's last name: ";
    getline(cin, homeowner);  // Allows spaces in the name

    // Compute commissions
    agency_commission = sales_price * COMMISSION_RATE;
    agent_commission = sales_price * AGENT_RATE;

    // Output formatting
    cout << fixed << showpoint << setprecision(2) << endl;
    cout << left << setw(20) << "Home Owner"
         << right << setw(20) << "Price of Home"
         << setw(20) << "Seller's Cost"
         << setw(20) << "Agent's Commission" << endl;

    cout << string(80, '-') << endl; // Creates a divider line

    cout << left << setw(20) << homeowner
         << right << setw(20) << sales_price
         << setw(20) << agency_commission
         << setw(20) << agent_commission << endl;

    return 0;
}
