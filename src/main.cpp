#include <iostream>

#include "api.hpp"

template<typename T>
void print_value(T value) {
    std::cout << value << std::endl;
}


int main() {
    std::cout << "Hello World!\n";
    print_value(5);
    int value = api::some_func(5);
    std::cout << "Value from function: " << value;
    return 0;
} 