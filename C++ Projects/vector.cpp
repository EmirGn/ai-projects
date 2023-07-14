#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    vector<int> vec = {1, 2, 3, 4, 6, 7};

    //Access vector elements
    cout << vec.back() << endl; //Returns the last element
    cout << vec.front() << endl; //Returns the first element
    cout << vec.size() << endl; //Returns the size of the array

    //Common vector methods
    cout << vec.capacity() << endl; //Returns the capacity of the array (may be different from the size)
    vec.push_back(9); //Push the input to the back of the array

    for (int i = 0; i < vec.size(); ++i){
        cout << vec[i] << " ";
    }

    vec.pop_back(); //Deletes last added item
    for (int i = 0; i < vec.size(); ++i){
        cout << vec[i] << " ";
    }

    vec.shrink_to_fit(); //Makes the capacity of the array the same as the size

    return 0;
}