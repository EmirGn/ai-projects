#include <iostream>
#include <random>
#include <iomanip>

class Perceptron{
    int in_features, out_features;
    bool bias_value;

    public:

    Perceptron(int a, int b, bool c);
    double** WGenerator(){
        //Random double generator
        std::random_device random;
        std::mt19937 rng(random());

        std::uniform_real_distribution<double> dist(-1.0, 1.0);
        
        //Weight Generator (mutlidimensional array so dynamic memmory allocation is used)
        double** weight = new double*[in_features];
        for (int i = 0; i < in_features; i++) {
            weight[i] = new double[out_features];
            for (int j = 0; j < out_features; j++) {
                weight[i][j] = dist(rng);
            }
        }
        //Return the first member's adress in the weight array
        return weight;
    }

    double* BGenerator(){
        //Random double generator
        std::random_device random;
        std::mt19937 rng(random());

        std::uniform_real_distribution<double> dist(-1.0, 1.0);

        //Bias generator
        double* bias = new double[out_features];
        for (int b = 0; b < out_features; b++){
            bias[b] = dist(rng);
        }
        return bias;
    }

    void Linear(){
        double** weight = WGenerator();
        double* bias = BGenerator();

        //Weights and biases
        for (int i = 0; i < in_features; ++i) {
            std::cout << "[";
            for (int j = 0; j < out_features; ++j) {
                if (j != (out_features - 1)){
                    std::cout << std::fixed << std::setprecision(4) << weight[i][j] << ", ";
                } else{
                    std::cout << std::fixed << std::setprecision(4) << weight[i][j];
                }
            }
            std::cout << "]" << std::endl;
        }

        // for (int b = 0; b < out_features; ++b){
        //     std::cout << bias[b] << std::endl;
        // }
    }
};

Perceptron::Perceptron(int in_features, int out_features, bool c){
    in_features = in_features;
    out_features = out_features;
    bias_value = c;
}

int main(){
    Perceptron Perceptron1(5, 6, true);
    Perceptron1.Linear();

}