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

    void remove_sign(unsigned int id) {
        if (signs.find(id) == signs.end()) {
            std::cout << "Предупреждение: Знак с ID " << id << " не найден в базе данных." << std::endl;
            return;
        }
        signs.erase(id);
    }

    Sign find_sign(unsigned int id) const {
        auto it = signs.find(id);
        if (it == signs.end()) {
            throw std::runtime_error("Sign with this ID not found.");
        }
        return it->second;
    }

    void add_multiple_signs(const std::vector<Sign>& sign_list) {
        for (const auto& sign : sign_list) {
            add_sign(sign);
        }
    }
};

#endif 
