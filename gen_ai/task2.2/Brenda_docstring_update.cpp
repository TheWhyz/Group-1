/*
Select a Code Snippet: 
Choose a code snippet from your current project, 
an open-source repository, or a past assignment 
from your previous programming classes that lacks 
proper documentation. Open an issue on the team 
repository to take ownership of the task.
*/
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;
ouble getDoubleInput(string prompt, double min, double max);
bool checkFailure(double input, float min, float max);
double circumference(double radius);
double area(double radius);


 double const PI = 3.14159;
int main() {

    double radius = 0;
    double ComputingArea = 0;
    double Computcircumference = 0;
    //constants
    const double MIN = 0.500000;
    const double MAX = 20.500000;
   

   
   string prompt = "Enter a circle radius between " +
   to_string(MIN) + " and " + to_string(MAX) + "\n**";


   radius = getDoubleInput(prompt,MIN,MAX);

    
  
    Computcircumference = circumference(radius);


  
    ComputingArea = area(radius);


    cout << fixed << setprecision(2);
    cout << "\nRadius: " << radius << endl;
    cout << "Circumference: " <<  Computcircumference << endl;
    cout << "Area: " << ComputingArea << endl;


    return 0; 
}

double getDoubleInput(string prompt, double min, double max) 
{
    bool isFail = false;
    double input = 0;
     
    do
    {
        cout << prompt;
        cin >> input;

        isFail = checkFailure(input, min, max);


       
    }while (isFail);
   

    return input; 
   
}

bool checkFailure (double input, float min, float max)
{
    
    if(cin.fail()||input < min || input > max)
    {
        cin.clear();
        cin.ignore(100,'\n');
        cout << "\nError: Invalid radius!";
        cout << endl;
        return true;
    }
    {
        return false;
    }
}

double circumference(double radius)
{

return  2 * PI * radius;

}

double area(double radius)
{

return PI * pow(radius, 2.0);

}


/*
Update Documentation: 
Based on ChatGPT’s suggestions, improve the code documentation 
to ensure it is clear, complete, and easy to understand.
*/


#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Function prototypes
double getDoubleInput(string prompt, double min, double max);
bool checkFailure(double input, float min, float max);
double circumference(double radius);
double area(double radius);

// Define the constant PI for the calculations
double const PI = 3.14159;

int main() {
    // Declare variables for radius, area, and circumference
    double radius = 0;
    double ComputingArea = 0;
    double Computcircumference = 0;
    
    // Constants for the valid input range
    const double MIN = 0.500000;   // Minimum valid radius
    const double MAX = 20.500000;  // Maximum valid radius

    // Prompt string for user input
    string prompt = "Enter a circle radius between " +
                   to_string(MIN) + " and " + to_string(MAX) + "\n**";

    // Get valid user input for the radius
    radius = getDoubleInput(prompt, MIN, MAX);

    // Calculate the circumference using the valid radius
    Computcircumference = circumference(radius);

    // Calculate the area using the valid radius
    ComputingArea = area(radius);

    // Display the results with two decimal points precision
    cout << fixed << setprecision(2);
    cout << "\nRadius: " << radius << endl;
    cout << "Circumference: " << Computcircumference << endl;
    cout << "Area: " << ComputingArea << endl;

    return 0; 
}

// Function to get a valid double input from the user
// Parameters:
//   prompt: the message to display to the user
//   min: the minimum valid value for the input
//   max: the maximum valid value for the input
// Returns:
//   A valid double input from the user that falls within the specified range
double getDoubleInput(string prompt, double min, double max) {
    bool isFail = false;
    double input = 0;
     
    // Keep prompting the user until valid input is provided
    do {
        cout << prompt;  // Display the input prompt
        cin >> input;    // Get the user input

        // Check if the input is within the valid range and not a failure
        isFail = checkFailure(input, min, max);
    } while (isFail);  // Repeat if the input is invalid

    return input;  // Return the valid input
}

// Function to check if the input is valid
// Parameters:
//   input: the value entered by the user
//   min: the minimum valid value
//   max: the maximum valid value
// Returns:
//   true if the input is invalid (either out of range or a failure), false otherwise
bool checkFailure(double input, float min, float max) {
    // Check if the input is not a number or outside the valid range
    if(cin.fail() || input < min || input > max) {
        cin.clear();               // Clear the error flag
        cin.ignore(100, '\n');      // Ignore invalid input
        cout << "\nError: Invalid radius!";
        cout << endl;
        return true;  // Return true to indicate failure
    }
    return false;  // Return false if the input is valid
}

// Function to calculate the circumference of a circle
// Parameters:
//   radius: the radius of the circle
// Returns:
//   The calculated circumference of the circle
double circumference(double radius) {
    return 2 * PI * radius;  // Formula: C = 2 * π * radius
}

// Function to calculate the area of a circle
// Parameters:
//   radius: the radius of the circle
// Returns:
//   The calculated area of the circle
double area(double radius) {
    return PI * pow(radius, 2.0);  // Formula: A = π * radius^2
}
