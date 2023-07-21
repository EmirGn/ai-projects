#include <iostream>
#include <string>
#include <vector>

using namespace std;

template <class typeof_vec, class typeof_cand>
vector<typeof_vec> vector_creator(typeof_cand candidate_number){
    vector<typeof_vec> candidates;
    for(int i = 0; i < candidate_number; ++i){
        typeof_vec name;
        cout << "Enter the number " << i+1 << " candidate's name: ";
        cin >> name;

        candidates.push_back(name);
    }

    return candidates;
}

void vector_shower(vector<string> myvec, int num_vec){
    for(int i = 0; i < num_vec; ++i){
        cout << myvec[i] << endl;
    }
}

int main(){
    int num_vec;
    string checker;

    goter:
    cout << "Enter the number of the vector: "; cin >> num_vec;

    vector<string> vec_array = vector_creator<string, int>(num_vec);

    quiter:
    cout << "Do you want to continue, show or end?: "; cin >> checker;

    if (checker == "continue"){
        goto goter;
    } else if (checker == "show"){
        vector_shower(vec_array, num_vec);
        goto quiter;
    } else{
        cout << "Program Finished";
    }

    return 0;
}