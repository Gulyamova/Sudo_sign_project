#ifndef SIGN_H
#define SIGN_H

#include <string>
#include <unordered_map>
#include <stdexcept>
#include <vector>
#include <iostream>

struct Coordinates {
    double longitude;
    double latitude;
};

class Sign {
public:
    std::string name;     
    unsigned int id;      
    Coordinates coordinates;  

    Sign(std::string name, unsigned int id, Coordinates coordinates)
        : name(name), id(id), coordinates(coordinates) {}
};

class SignDatabase {
private:
    std::unordered_map<unsigned int, Sign> signs;  

public:
    void add_sign(const Sign& sign) {
        if (signs.find(sign.id) != signs.end()) {
            throw std::runtime_error("Sign with this ID already exists.");
        }
        signs.emplace(sign.id, Sign(sign.name, sign.id, sign.coordinates));
    }

    bool remove_sign(unsigned int id) {
        if (signs.find(id) == signs.end()) {
            std::cout << "Warning: Sign with ID " << id << " not found in the database." << std::endl;
            return false;
        }
        signs.erase(id);
        return true;
    }

    Sign find_sign(unsigned int id) const {
        auto it = signs.find(id);
        if (it == signs.end()) {
            throw std::runtime_error("Sign with this ID not found.");
        }
        return it->second;
    }

    std::pair<std::vector<Sign>, std::vector<Sign>> add_multiple_signs(const std::vector<Sign>& signs) {
        std::vector<Sign> successfully_added;
        std::vector<Sign> failed_to_add;

        for (const auto& sign : signs) {
            try {
                add_sign(sign);
                successfully_added.push_back(sign);
            } catch (const std::runtime_error& e) {
                std::cerr << "Failed to add sign with ID " << sign.id << ": " << e.what() << std::endl;
                failed_to_add.push_back(sign);
            }
        }
        return std::make_pair(successfully_added, failed_to_add);
    }
};

#endif 
