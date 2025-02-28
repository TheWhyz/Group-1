// Old refactored code
void crateCalculations()
{
    string line;
    //Gets the first line of the file
    getline(fin, line);
    //Int variable to keep track of the crate orders
    int crateOrder = 1;

    while(!fin.eof())
    {
        //The length, width, and height of the crate is stored in these double variables.
        double lengthCrate;
        double widthCrate;
        double heightCrate;

        //Formatting for the top of the table
        fout << endl;
        fout << setw(110) << setfill('-') << '-' << endl;

        fout << "\nCrate Order " << crateOrder << endl;
        crateOrder++;

        fout << '+' << setw(8) << setfill('-') << '+' << setw(10) << '+' << setw(9) << '+';
        fout << setw(9) << '+' << setw(13) << '+' << setw(15) << '+' << setw(11) << '+' << endl;

        fout << left << "| " << setfill(' ') << setw(6) << "TYPE" << "| "  
            << setw(8) << "LENGTH" << "| " << setw(7) << "WIDTH" << "| ";
        fout << setw(7) << "HEIGHT" << "| " << setw(11) << "VOLUME" << "| " << setw(13) 
            << "SURFACE AREA" << "| " << setw(9) << "DIAGONAL" << "|" << right << endl;

        fout << '+' << setw(8) << setfill('-') << '+' << setw(10) << '+' << setw(9) << '+';
        fout << setw(9) << '+' << setw(13) << '+' << setw(15) << '+' << setw(11) << '+' << endl;

        fin >> lengthCrate;
        /*
            If fin fails, or lengthCrate is less than minimum crate size,
             or lengthCrate is greater than maximum crate size, then output
             error message, clear and ignore fin then restart the loop.
            Else, display lengthCrate.
        */
        if(fin.fail() && !fin.eof())
        {
            fout << left << "| " << setfill(' ') << setw(6) << "Crate" << "| " 
             << fixed << setprecision(1) << setw(8) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((lengthCrate < CRATE_SIZE_MINIMUM) && !fin.eof())
        {
            fout << left << "| " << setfill(' ') << setw(6) << "Crate" << "| " 
             << fixed << setprecision(1) << setw(8) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((lengthCrate > CRATE_SIZE_MAXIMUM) && !fin.eof())
        {
            fout << left << "| " << setfill(' ') << setw(6) << "Crate" << "| " 
             << fixed << setprecision(1) << setw(8) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else
        {
            fout << left << "| " << setfill(' ') << setw(6) << "Crate" << "| " 
             << fixed << setprecision(1) << setw(8) << lengthCrate << "| ";
        }

        /*
            If fin fails, or widthCrate is less than minimum crate size,
             or widthCrate is greater than maximum crate size, then output
             error message, clear and ignore fin then restart the loop.
            Else, display widthCrate.
        */
        fin >> widthCrate;
        if(fin.fail() && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((widthCrate < CRATE_SIZE_MINIMUM) && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((widthCrate > CRATE_SIZE_MAXIMUM) && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else
        {
            fout << setw(7) << widthCrate << "| ";
        }

        /*
            If fin fails, or heightCrate is less than minimum crate size,
             or heightCrate is greater than maximum crate size, then output
             error message, clear and ignore fin then restart the loop.
            Else, display heightCrate.
        */
        fin >> heightCrate;
        if(fin.fail() && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((lengthCrate < CRATE_SIZE_MINIMUM) && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((lengthCrate > CRATE_SIZE_MAXIMUM) && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else
        {
           fout << setw(7) << heightCrate << "| ";
        }

        //Stores the volume, surface area, and diagonal space of 
        //the crate values and initialized with their respective formulas.
        double volumeCrate = widthCrate * heightCrate * lengthCrate;
        double surfaceAreaCrate = 2 * (widthCrate * lengthCrate + heightCrate
            * lengthCrate + heightCrate * widthCrate);
        double diagonalCrate = sqrt(pow(lengthCrate,2) + pow(widthCrate,2) + pow(heightCrate,2));

        fout << setw(11) << volumeCrate << "| ";
        fout << setw(13) << surfaceAreaCrate << "| " << setw(9) << diagonalCrate << "|" << endl;

        //The length, width, and height of the space is stored in these double variables.
        double lengthSpace;
        double widthSpace;
        double heightSpace;

        fin >> lengthSpace;
        /*
            If fin fails, or lengthSpace is less than minimum space size,
             or lengthSpace is greater than maximum space size, then output
             error message, clear and ignore fin then restart the loop.
            Else, display lengthSpace.
        */
        if(fin.fail() && !fin.eof())
        {
            fout << "| " << setfill(' ') << setw(6) << "Space" 
             << "| " << setw(8) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((lengthSpace < STORAGE_ROOM_SIZE_MINIMUM) && !fin.eof())
        {
            fout << "| " << setfill(' ') << setw(6) << "Space" 
             << "| " << setw(8) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((lengthSpace > STORAGE_ROOM_SIZE_MAXIMUM) && !fin.eof())
        {
            fout << "| " << setfill(' ') << setw(6) << "Space" 
             << "| " << setw(8) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else
        {
            fout << "| " << setfill(' ') << setw(6) << "Space" << "| " << setw(8) << lengthSpace << "| ";
        }

        fin >> widthSpace;
        /*
            If fin fails, or widthSpace is less than minimum space size,
             or widthSpace is greater than maximum space size, then output
             error message, clear and ignore fin then restart the loop.
            Else, display widthSpace.
        */
        if(fin.fail() && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((widthSpace < STORAGE_ROOM_SIZE_MINIMUM) && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if((widthSpace > STORAGE_ROOM_SIZE_MAXIMUM) && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else
        {
            fout << setw(7) << widthSpace << "| ";
        }

        fin >> heightSpace;
        /*
            If fin fails, or widthSpace is less than minimum space size,
             or widthSpace is greater than maximum space size, then output
             error message, clear and ignore fin then restart the loop.
            Else, display widthSpace.
        */
        if(fin.fail() && !fin.eof())
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if(heightSpace < STORAGE_ROOM_SIZE_MINIMUM)
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else if(heightSpace > STORAGE_ROOM_SIZE_MAXIMUM)
        {
            fout << setw(7) << "Error" << "| " << right << endl;
            fin.clear();
            fin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        else
        {
            fout << setw(7) << heightSpace << "| ";
        }

        //Stores the volume, surface area, and diagonal space of 
        //the space values and initialized with their respective formulas.
        double volumeSpace = widthSpace * heightSpace * lengthSpace;
        double surfaceAreaSpace = 2 * (widthSpace * lengthSpace + heightSpace 
            * lengthSpace + heightSpace * widthSpace);
        double diagonalSpace = sqrt(pow(lengthSpace,2) + pow(widthSpace,2) + pow(heightSpace,2));

        fout << setw(11) << volumeSpace << "| " << setw(13) 
         << surfaceAreaSpace << "| " << setw(9) << diagonalSpace << "| " << endl;

        fout << right << '+' << setw(8) << setfill('-') << '+' << setw(10) << '+' << setw(9) << '+';
        fout << setw(9) << '+' << setw(13) << '+' << setw(15) << '+' << setw(11) << '+' << endl;
        fout << endl;
        
        //Stores the total amount of crates that can fit the space and the results are floored.
        double totalCrates = floor(lengthSpace / lengthCrate) * floor(widthSpace / widthCrate) * floor(heightSpace / heightCrate);

        fout << totalCrates << " crates can fit in the storage space." << endl << endl;

        //Double variables to store the overall fee of the crates and the fee per crate
        double crateFee;
        double feePerCrate;

        /*
            If the volume of the crate inputted is less than or equal to 40 cubic feet the program will calculate
             the overall fee with CRATE_FEE_SMALL.
            Otherwise, if the volume of the crate is less than equal to 80 cubic feet the program will calculate the 
             overall fee with CRATE_FEE_MEDIUM.
            Otherwise, if the volume of the crate is greater than 80 cubic feet the program will calculate
             the overall fee with CRATE_FEE_LARGE.
        */
        if(volumeCrate <= 40.0)
        {
            crateFee = totalCrates * CRATE_FEE_SMALL;
            feePerCrate = CRATE_FEE_SMALL;
        }
        else if(volumeCrate <= 80.0)
        {
            crateFee = totalCrates * CRATE_FEE_MEDIUM;
            feePerCrate = CRATE_FEE_MEDIUM;
        }
        else if(volumeCrate > 80.0)
        {
            crateFee = totalCrates * CRATE_FEE_LARGE;
            feePerCrate = CRATE_FEE_LARGE;
        }

        //Display the volume, fee per crate, total crates, and crate fees
        fout << fixed << setprecision(6) << "Crate volume " << volumeCrate << " cost" << setw(25) << setfill('.');
        fout << setprecision(2) << "$" << feePerCrate << endl;
        fout << "Price to ship " << totalCrates << " crates" << setw(23) << setfill('.') << "$" << crateFee << endl << endl;
        
        //Double variables to store the fee per cubic feet of 
        //storage room space and the total cose of the space
        double shipStorageRoomFee;
        double feePerCubicFeetStorageRoom;

         /*
            If the volume of the storage room space inputted is less than 250,000 cubic feet the program will calculate
             the overall fee with STORAGE_ROOM_FEE_SMALL.
            Otherwise, if the volume of the storage room space is less than or equal to 500,000 cubic feet the program will calculate the 
             overall fee with STORAGE_ROOM_FEE_MEDIUM.
            Otherwise, if the volume of the crate is  less than or equal to 750,000 cubic feet the program will calculate
             the overall fee with STORAGE_ROOM_FEE_LARGE.
            Otherwise, if the volume of the crate is greater than 750,000 cubic feet the program will calculate the 
             overall fee with STORAGE_ROOM_FEE_EXTRA_LARGE.
        */
        if(volumeSpace < 250000.0)
        {
            shipStorageRoomFee = volumeSpace * STORAGE_ROOM_FEE_SMALL;
            feePerCubicFeetStorageRoom = STORAGE_ROOM_FEE_SMALL;
        }
        else if(volumeSpace <= 500000.0)
        {
            shipStorageRoomFee = volumeSpace * STORAGE_ROOM_FEE_MEDIUM;
            feePerCubicFeetStorageRoom = STORAGE_ROOM_FEE_MEDIUM;
        }
        else if(volumeSpace <= 750000.0)
        {
            shipStorageRoomFee = volumeSpace * STORAGE_ROOM_FEE_LARGE;
            feePerCubicFeetStorageRoom = STORAGE_ROOM_FEE_LARGE;
        }
        else if(volumeSpace > 750000.0)
        {
            shipStorageRoomFee = volumeSpace * STORAGE_ROOM_FEE_EXTRA_LARGE;
            feePerCubicFeetStorageRoom = STORAGE_ROOM_FEE_EXTRA_LARGE;
        }

        //Display volume space and fees for storage
        fout << "Storage rooms with volume " << setprecision(6) << volumeSpace << " cost" << setw(9) << setfill('.');
        fout << "$" << setprecision(2) << feePerCubicFeetStorageRoom << " per cubic foot" << endl;
        fout << setprecision(6) << volumeSpace << " cubic feet storage room cost" 
         << setw(11) << setfill('.') << "$" << setprecision(2) << shipStorageRoomFee;
        fout << endl << endl;

        //Double variable initialized to calculate the total cost
        double totalCost = crateFee + shipStorageRoomFee;

        //Displays the total cost
        fout << "Total cost" << setprecision(2) << setw(41) << setfill('.') << "$" << totalCost << endl;

    }
}


// New refactored code
void printTableHeader(int crateOrder) {
    fout << endl << setw(110) << setfill('-') << '-' << endl;
    fout << "\nCrate Order " << crateOrder << endl;
    fout << "+--------+----------+---------+---------+-------------+---------------+-----------+" << endl;
    fout << "| TYPE   | LENGTH   | WIDTH   | HEIGHT  | VOLUME      | SURFACE AREA  | DIAGONAL  |" << endl;
    fout << "+--------+----------+---------+---------+-------------+---------------+-----------+" << endl;
}

double readAndValidateDimension(const string& type, double minSize, double maxSize) {
    double value;
    fin >> value;
    if (fin.fail() || value < minSize || value > maxSize) {
        fout << "| " << setw(6) << type << " | " << setw(8) << "Error" << " |" << endl;
        fin.clear();
        fin.ignore(numeric_limits<streamsize>::max(), '\n');
        return -1; 
    }
    return value;
}

void processCrate() {
    static int crateOrder = 1;
    printTableHeader(crateOrder++);

    double lengthCrate = readAndValidateDimension("Crate", CRATE_SIZE_MINIMUM, CRATE_SIZE_MAXIMUM);
    if (lengthCrate == -1) return;
    double widthCrate = readAndValidateDimension("Crate", CRATE_SIZE_MINIMUM, CRATE_SIZE_MAXIMUM);
    if (widthCrate == -1) return;
    double heightCrate = readAndValidateDimension("Crate", CRATE_SIZE_MINIMUM, CRATE_SIZE_MAXIMUM);
    if (heightCrate == -1) return;

    double volumeCrate = lengthCrate * widthCrate * heightCrate;
    double surfaceAreaCrate = 2 * (lengthCrate * widthCrate + heightCrate * widthCrate + heightCrate * lengthCrate);
    double diagonalCrate = sqrt(pow(lengthCrate, 2) + pow(widthCrate, 2) + pow(heightCrate, 2));

    fout << "| Crate  | " << setw(8) << lengthCrate << " | " << setw(7) << widthCrate << " | " << setw(7) << heightCrate 
         << " | " << setw(11) << volumeCrate << " | " << setw(13) << surfaceAreaCrate 
         << " | " << setw(9) << diagonalCrate << " |" << endl;
    fout << "+--------+----------+---------+---------+-------------+---------------+-----------+" << endl;

    double lengthSpace = readAndValidateDimension("Space", STORAGE_ROOM_SIZE_MINIMUM, STORAGE_ROOM_SIZE_MAXIMUM);
    if (lengthSpace == -1) return;
    double widthSpace = readAndValidateDimension("Space", STORAGE_ROOM_SIZE_MINIMUM, STORAGE_ROOM_SIZE_MAXIMUM);
    if (widthSpace == -1) return;
    double heightSpace = readAndValidateDimension("Space", STORAGE_ROOM_SIZE_MINIMUM, STORAGE_ROOM_SIZE_MAXIMUM);
    if (heightSpace == -1) return;

    double volumeSpace = lengthSpace * widthSpace * heightSpace;
    double totalCrates = floor(lengthSpace / lengthCrate) * floor(widthSpace / widthCrate) * floor(heightSpace / heightCrate);
    fout << totalCrates << " crates can fit in the storage space." << endl;

    double crateFee = (volumeCrate <= 40.0) ? totalCrates * CRATE_FEE_SMALL :
                      (volumeCrate <= 80.0) ? totalCrates * CRATE_FEE_MEDIUM :
                                              totalCrates * CRATE_FEE_LARGE;

    fout << "Crate volume " << volumeCrate << " cost $" << crateFee / totalCrates << endl;
    fout << "Total crate shipping cost: $" << crateFee << endl;

    double storageFeePerCubicFoot = (volumeSpace < 250000.0) ? STORAGE_ROOM_FEE_SMALL :
                                    (volumeSpace <= 500000.0) ? STORAGE_ROOM_FEE_MEDIUM :
                                    (volumeSpace <= 750000.0) ? STORAGE_ROOM_FEE_LARGE :
                                                                STORAGE_ROOM_FEE_EXTRA_LARGE;
    double storageFee = volumeSpace * storageFeePerCubicFoot;
    fout << "Storage room cost: $" << storageFee << endl;
    fout << "Total cost: $" << crateFee + storageFee << endl;
}

void crateCalculations() {
    string line;
    getline(fin, line);
    while (!fin.eof()) {
        processCrate();
    }
}