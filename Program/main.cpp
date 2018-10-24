#include <iostream>
#include <fstream>>
using namespace std;

void trainingchatbot(); //calls for the procedure trainingchatbot
void startchatbot(); //calls for the procedure startchatbot

int main() //begins the program
{
    int menuchoice, quit; // call the int variables
    quit = 0; //variable to check if the user wants to quit
    do{ //main menu
        cout << "Welcome to my Chatbot Program" << endl;
        cout << "What would you like to do:" << endl;
        cout << "Press 1 for: Teach the Chatbot" << endl;
        cout << "Press 2 for: Start the Chatbot" << endl;
        cout << "Press 3 to quit" << endl;
        cin >> menuchoice; //user enters choice
        switch(menuchoice){
            case 1: trainingchatbot(); break; //directs the user to the bot training
            case 2: startchatbot(); break; //directs the user to the conversation with the bot
            case 3: quit = quit + 20; break; // will make the program quit
            default: cout << "Invalid choice." << endl << endl;
            //if non of the case statements are met then the default statement will execute
        }
    } while(quit < 20); //the program will restart 20 times before finally stopping
    return 0;
}

void addthedata(string questions[], string answers[], string trash[]){
    //gets data from the trainingchatbot function
    ofstream myFile; // creates a variable where data is going to be output
    myFile.open("database.csv"); //the variable is attached to the database file
    for(int a = 0; a < 4; a = a + 1){ //'a' may change depending on the number of questions in the database
        myFile << questions[a] << "," << trash[a] << "," <<  answers[a] << endl;
        //the question, the other answers and the new answer are stored in order.
    }
}

void trainingchatbot(){ //beginning of the chatbot training function
    cout << endl << "You chose train the Chatbot" << endl;
    string questions[4]; //the number represents the questions in the database
    string answers[4];  //the number represents the questions in the database
    string trash[100]; //stores the answers that are already existing within the database
    ifstream ip("database.csv"); //opens the file to read it

    if(!ip.is_open()) std::cout << "ERROR: File Open" << '\n'; //checks if the file is open
    for(int a = 0; a < 4; a = a + 1){ //'a' may change depending on the number of questions in the database
        getline(ip,questions[a],','); //pulls the question and stores it
        getline(ip,trash[a], '\n'); //pulls all the other answers for that question and stores it
    }
    for(int b = 0; b < 4; b = b + 1){//'a' may change depending on the number of questions in the database
        cout << questions[b] << endl; //asks  the question to the user
        cin >> answers[b]; //The answer to the question is stored
    }
    ip.close(); //The document is closed. Cant read from it after this.
    addthedata(questions, answers, trash); //Calls for the function addthedata
}

void startchatbot(){
    cout << endl << "You chose to chat to the bot" << endl;
}
















