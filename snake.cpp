#include <iostream>
#include <string>
#include <conio.h> // функции нажатия

using namespace std;

bool gameOver;
const int width = 30;// растояние  по ширине и высоте
const int height = 20;
int x , y, fruitX , fruitY , score;

enum eDirection {
    STOP = 0,
    LEFT,
    RIGHT,
    UP,
    DOWN

}; //  задаём стороны

eDirection dir;

void Setup() {
    gameOver = false;
    dir = STOP;
    x = width / 2 - 1;  // расположение змейки
    y = height / 2 - 1;
    fruitX = rand () % width; // задаём рандомное расположение для фруктов ось X
    fruitY = rand () % height;// ocь Y
    score = 0;
}

void Draw() {
    system("cls");// на маке ("clear")
    for (int i = 0; i < width + 1; i++) // расположение стенок
        cout << "#";
    cout << endl; // верхние стенки

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
          if (j == 0 || j == width - 1)
            cout << "#";// обозначение стенок
          if (i == y && j == x) // змея
            cout << "0"; // вид змеи
          else if (i == fruitY && j == fruitX)
            cout << "$"; // фрукт
          else
            cout << " ";// пустота
        }
        cout << endl; // боковые
    }

    for (int i = 0; i < width + 1; i++)
         cout << "#";
        cout << endl; // нижние
}   // cout << endl; - конец строки

void Input() {
    if (_kbhit()) {
        switch (_getch()) {// проверка куда нажал пользователь
            case 'a': // движение по сторонам
                dir = LEFT;
                break; // конец
            case 'd':
                dir = RIGHT;
                break;
            case 'w':
                dir = UP;
                break;
            case 's':
                dir = DOWN;
                break;
            case 'x':
                gameOver = true; // конец игры
                break;
        }
    }


}

void Logic() { // проверка клавиш
    switch (dir) {
        case LEFT: // движение нажатием
           x--;
           break;
        case RIGHT:
           x++;
           break;
        case UP:
           y--;
           break;
        case DOWN:
           y++;
           break;
    }

    if (x > width  || x < 0 || y > height || y < 0); // конец игры при столкновении
        gameOver = true;
}
int main() {
    Setup();
    while (!gameOver) {
        Draw();
        Input();
        Logic();
    }
    return 0;
}
