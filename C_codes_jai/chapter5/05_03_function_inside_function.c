#include <stdio.h>

    void goodMorning();
    void goodAfternoon();
    void goodNight();

    int main(){
         goodMorning();  //goodmorning ko directly call kiya aur good-afternoon, night ko indirectly
        
    return 0;
}

void goodMorning(){
    printf("Good Morning Jai\n");
    goodAfternoon();
}

void goodAfternoon(){
    printf("Good Afternoon Jai\n");
    goodNight();
}

void goodNight(){
    printf("Good Night Jai\n");
}