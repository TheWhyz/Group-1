/*
Select a Code Snippet: 
Choose a code snippet from your current project, 
an open-source repository, or a past assignment 
from your previous programming classes. Open an 
issue on the team repository identifying specific 
problems (e.g., duplication, inefficiency, poor readability).
*/

#include "knightType.h"
#include <iostream>
#include <cmath>

using namespace std;

/*
* function_identifier: knight constructor
* parameters: color
* return value: none
*/

knightType::knightType(bool color): chessPiece(color) {}

/*
Implement Refactorings: Apply ChatGPT’s suggestions to
improve the code’s quality and readability. Ensure that
the functionality of the code remains intact after refactoring.
*/
	
bool knightType::move(char startRow, int startCol, char endRow,
 int endCol, chessPiece*** board)
{

    // 8 checks 
    int horizontal_move = static_cast<int>(endCol - startCol);
    int vertical_move = endRow - startRow;

//First check: up two and left one
    if (horizontal_move == -1 && (vertical_move == -2)){
        // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }
    //Second check: up two and right one
    else if (horizontal_move == 1 && (vertical_move == -2)){
        // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }

    //Third check: down two and to the left one
    else if (horizontal_move == -1 && (vertical_move == 2)){
             // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }

    //Fourth check: down two and to the right one
    else if (horizontal_move == 1 && (vertical_move == 2)){
             // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr){
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }

    //Fifth Check: left two and up one
    else if (horizontal_move == -2 && (vertical_move == -1)){
             // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }

    //Sixth Check: left two and down one
    else if (horizontal_move == -2 && (vertical_move == 1)){
             // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }

    //Seven Check: right two and up one
    else if (horizontal_move == 2 && (vertical_move == -1)){
             // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }

    //eight Check: right two and down one
    else if (horizontal_move == 2 && (vertical_move == 1)){
             // checks if end position has a piece
        if(board[endRow - 'A'][endCol] != nullptr) {
            // if there is a piece // check the colors
            if (board[endRow - 'A'][endCol]-> getPlayerType() != getPlayerType()){
                return true;
            }
            return false;
        }
        // checks if there is no piece at the end position
        else if(board[endRow - 'A'][endCol] == nullptr) {
            return true;
        }
        return true;
    }
}
/*
* function_identifier: knight destructor
* parameters: none
* return value: none
*/

knightType::~knightType(){
	cout << "Knight Taken.";
}


/*
Consult ChatGPT: Provide ChatGPT with the code 
and highlight specific areas where you need clarity or improvements.
Ask for suggestions on how to simplify, optimize, or improve the code.
*/

#include "knightType.h"
#include <iostream>
#include <cmath>

using namespace std;

knightType::knightType(bool color): chessPiece(color) {}

bool knightType::move(char startRow, int startCol, char endRow,
                      int endCol, chessPiece*** board) {

    // Calculate horizontal and vertical moves
    int horizontal_move = static_cast<int>(endCol - startCol);
    int vertical_move = endRow - startRow;

    // List of possible knight moves (up, down, left, right)
    int validMoves[8][2] = {
        {-1, -2}, {1, -2}, {-1, 2}, {1, 2},  // up/down and left/right combos
        {-2, -1}, {-2, 1}, {2, -1}, {2, 1}   // further combinations
    };

    // Check if the move is one of the valid knight moves
    for (int i = 0; i < 8; i++) {
        if (horizontal_move == validMoves[i][0] && vertical_move == validMoves[i][1]) {
            // Check if end position has a piece
            if (board[endRow - 'A'][endCol] != nullptr) {
                // Check the color of the piece at the end position
                if (board[endRow - 'A'][endCol]->getPlayerType() != getPlayerType()) {
                    return true;
                }
                return false; // It's the same color
            } else {
                // No piece at the end position, valid move
                return true;
            }
        }
    }

    return false;  // Not a valid knight move
}

knightType::~knightType() {
    cout << "Knight Taken.";
}
