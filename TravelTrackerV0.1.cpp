#include <iostream>
#include <string>
using namespace std;

int main(){
    int total_gasto = 0;
    int preco;
    string item;

    cout << "Qual item foi comprado: " << endl;
    getline(cin >> ws, item);
    cout << "Quanto custou: " << endl;
    cin >> preco;

    total_gasto += preco;
    cout << "Item: " << item << endl;
    cout << "Total Gasto: " << total_gasto << endl;

    return 0;
}