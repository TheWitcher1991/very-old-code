/**************************************************
                  ЗАДАЧИ

 1) ДОБАВИТЬ КОНЯ

 2) УЗНАТЬ ВСЕ ВОЗМОЖНЫЕ ХОДЫ КОНЯ С ПОМОЩЬЮ МАССИВА

 3) ДОБАВИТЬ ФЕРЗЯ

 4) С ПОМОЩЬЮ УСЛОВИЯ УЗНАТЬ БЬЁТ-ЛИ ФЕРЗЬ КОНЯ

 5) С ПОМОЩЬЮ УСЛОВИЯ УЗНАТЬ БЬЁТ-ЛИ КОНЬ ФЕРЗЯ

 P.S. работает пока криво, советую компелировать в нормальном редакторе(codeblock, qt creator, vs code и т.д.)

***************************************************/
#include <iostream>
#include <Windows.h>

using namespace std;

int main()
{
    system("color a");//меняем цвет фона и текста
    setlocale(LC_ALL,"");

    int x,y,fx,fy;
    //создаём массивы для координат коня
    int arrayX[8], arrayY[8];

    //добавлям коня
    cout << "Введите координаты на которых будет конь" << endl;
    Sleep(1000);//задержка

    cout << " Введите координату X:" << endl;
    cout << "  ";
    cin >> x;
    cout << "  x: " << x << endl << endl;

    cout << " Введите координату Y:" << endl;
    cout << "  ";
    cin >> y;
    cout << "  y: " << y << "\n\n" << endl;


    if ( ( x > 0 ) && ( x <= 8 ) && ( y > 0 ) && ( y <= 8 ) ) {//условие проверки координат
        cout << " Конь стоит на: " << x << " | " << y << endl << endl;

        //находим как ходит конь (буквой "Г")
        arrayX[1] = x - 2;arrayY[1] = y - 1;
        arrayX[2] = x - 2;arrayY[2] = y + 1;
        arrayX[3] = x - 1;arrayY[3] = y - 2;
        arrayX[4] = x - 1;arrayY[4] = y + 2;
        arrayX[5] = x + 1;arrayY[5] = y - 2;
        arrayX[6] = x + 1;arrayY[6] = y + 2;
        arrayX[7] = x + 2;arrayY[7] = y - 1;
        arrayX[8] = x + 2;arrayY[8] = y + 1;


        //добавляем ферзя
        cout << " Введите координату ферзя по X" << endl;
        cout << "  ";
        cin >> fx;
        cout << "  x: " << fx << endl << endl;

        cout << " Введите координату Y:" << endl;
        cout << "  ";
        cin >> fy;
        cout << "  y: " << fy << endl << endl;

        //битие ферзя
        if ( ( fx == x ) || ( fy = y ) ) {
            cout << " Ферзь бьёт коня :D !" << endl;
        } else {
            cout << " Ферзь не бьёт коня :P !";
        }

        //битие коня
        if ( ( fx == arrayX[x] ) || ( fy == arrayY[y] ) ) {
            cout << " Конь бьёт ферзя :D !" << endl;
        } else {
            cout << " Конь не бьёт ферзя :P !" << endl;
        }

    } else {
        system("color c");
        cout << " ТАКИХ КООРДИНАТ НЕТ" << endl;
        Sleep(3000);
        system("cls");//перезагружаем main()
        main();
    }


    system("pause");
    return 0;
}
