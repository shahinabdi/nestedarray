#include <iostream>
#include <vector>
#include <chrono>
#include <ctime>

void process_large_array(const size_t size) {
    // Create nested vector
    std::vector<std::vector<int>> nested_array;
    nested_array.reserve(size);
    
    for (size_t i = 0; i < size; ++i) {
        std::vector<int> inner(100);
        for (size_t j = 0; j < 100; ++j) {
            inner[j] = j;
        }
        nested_array.push_back(std::move(inner));
    }
    
    // Process the array
    long long total = 0;
    for (size_t i = 0; i < nested_array.size(); ++i) {
        for (size_t j = 0; j < nested_array[i].size(); ++j) {
            total += nested_array[i][j];
        }
    }
    
    std::cout << "Result: " << total << std::endl;
}

int main() {
    std::vector<size_t> sizes = {10000, 100000, 1000000};
    
    for (const auto& size : sizes) {
        std::cout << "\nTesting with array size: " << size << std::endl;
        
        // Start timing
        auto start = std::chrono::high_resolution_clock::now();
        
        process_large_array(size);
        
        // End timing
        auto end = std::chrono::high_resolution_clock::now();
        
        // Calculate duration
        std::chrono::duration<double> duration = end - start;
        std::cout << "Time taken: " << duration.count() << " seconds" << std::endl;
    }
    
    return 0;
}