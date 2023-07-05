#include <iostream>
#include <random>
#include <iomanip>

class Perceptron{
    int in_features, out_features;
    bool bias;

    public:

    Perceptron (int, int, bool);

    double** Generator(){
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

    void Linear(double** weight){
        for (int i = 0; i < in_features; ++i) {
            for (int j = 0; j < out_features; ++j) {
              std::cout << "[" << std::fixed << std::setprecision(4) << weight[i][j] << "]";
            }
            std::cout << std::endl;
        }
    }
};

Perceptron::Perceptron(int a, int b, bool c){
    in_features = a;
    out_features = b;
    bias = c;
}

int main(){
    double** weight;
    Perceptron perceptron_1(5, 10, true);
    weight = perceptron_1.Generator();
    perceptron_1.Linear(weight);

}