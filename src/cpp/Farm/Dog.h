#ifndef DOG_H
    #define DOG_H

    #include "Animal.h"

    class Dog : public Animal {
        public:
            Dog();
            Dog(unsigned int age);

            bool timeDie();
    };

#endif // DOG_H
