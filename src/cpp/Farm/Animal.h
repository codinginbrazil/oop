#ifndef ANIMAL_H
    #define ANIMAL_H

    #include <cstdio>
    #include <cstdlib>
    #include <cstring>
    #include <iostream>
    #include <sstream>


    #define DEATH_CHICKEN 20
    #define DEATH_COW 30
    #define DEATH_PORK 15

    #define ADULT 2
    #define ADULT_CHICKEN 2
    #define ADULT_COW 10
    #define ADULT_PORK 5


    enum Tspecies{ UNKNOWN , CHICKEN , COW , PORK };


    class Animal {
        private:
            bool sex;
            std::string food;
            std::string name;
            std::string product;
            std::string skin;
            std::string sound;
            Tspecies specie;
            unsigned age;
            unsigned paws;

        protected:
            void setPaws( unsigned int paws );
            void setProduct( std::string product );
            void setSpecie( Tspecies specie );
            void setSkin( std::string skin );
            void setSound( std::string sound );
        
        public:
            Animal();

            bool getSex();
            std::string getFood();
            std::string getName();
            std::string getProduct();
            std::string getSound();
            std::string getSkin();
            Tspecies getSpecie();
            unsigned int getAge();
            unsigned int getPaws();

            void setAge(unsigned int age );
            void setFood( std::string food );
            void setName( std::string name );
            void setSex( bool sex );

            virtual bool timeDie();
            std::string specieToString();
            std::string summaryToString();
            std::string toString();
            //virtual const double ageOfDeath()=0;
    };
#endif // ANIMAL_H