#ifndef CHICKEN_H
    #define CHICKEN_H

    #include <Animal.h>

    class Chicken : public Animal {
        public:
            Chicken();
            Chicken(std::string name);
            Chicken(std::string name, bool sex);
            Chicken(std::string name, unsigned int age, bool sex);
            
            bool timeDie();
            unsigned int getAge();
            //const double ageOfDeath();
    };

#endif // CHICKEN_H
