#include <iostream>
#include <string>
#include <sstream>

using namespace std;

#define None 0

int main(){
    int i;
    int* an_array;
    std::cout << "How many value will be in the array?: ";
    cin >> i;

    an_array = new int[i];
    for (int value = 0; value < i; ++value){
        int garbage;
        std::cout << "Write the " << value+1 << "th " << "element of the array: "; cin >> garbage;
        an_array[value] = garbage;
    }

    std::cout << "You have entered: ";
    for (int value = 0; value < i; ++value){
        if (value != (i - 1)){
            std::cout << an_array[value] << ", ";
        }else {
            std::cout << an_array[value];
        }
    }

    delete[] an_array;
}