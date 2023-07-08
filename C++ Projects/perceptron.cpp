#include <iostream>
#include <random>
#include <iomanip>

class Perceptron{
    int in_features, out_features;
    bool bias_value;

    public:

    Perceptron(int a, int b, bool c);
    double** WGenerator(){
        std::random_device random;
        std::mt19937 rng(random());

        std::uniform_real_distribution<double> dist(-1.0, 1.0);
        
        //Generator
        double** weight = new double*[in_features];
        for (int i = 0; i < in_features; i++) {
            weight[i] = new double[out_features];
            for (int j = 0; j < out_features; j++) {
                weight[i][j] = dist(rng);
            }
        }

        return weight;
    }

    double* BGenerator(){
        std::random_device random;
        std::mt19937 rng(random());

        std::uniform_real_distribution<double> dist(-1.0, 1.0);

        double* bias = new double[out_features];

        for (int b = 0; b < out_features; b++){
            bias[b] = dist(rng);
        }
        return bias;
    }

    void Linear(){

        double** weight = WGenerator();
        double* bias = BGenerator();
        for (int i = 0; i < in_features; ++i) {
            for (int j = 0; j < out_features; ++j) {
              std::cout << "[" << std::fixed << std::setprecision(4) << weight[i][j] << "]";
            }
            std::cout << std::endl;
        }

        int c = 0;
        while (c < 60){
            std::cout << "-";
            ++c;
            if (c == 60){
                std::cout << std::endl;
            }
        }

        for (int b = 0; b < out_features; ++b){
            std::cout << bias[b] << std::endl;
        }
    }
};

Perceptron::Perceptron(int a, int b, bool c){
    in_features = a;
    out_features = b;
    bias_value = c;
}

int main(){
    Perceptron Perceptron1(5, 6, true);
    Perceptron1.Linear();
    // Perceptron1.Linear();
}