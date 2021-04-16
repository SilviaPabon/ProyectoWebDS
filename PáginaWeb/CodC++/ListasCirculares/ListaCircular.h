typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"
class ListaCircular
{
	private:
		Nodo* inicio;
	public:
		ListaCircular();
		bool isEmpty();
		int getSize();
		void clear();
		Dato getHead();
		Dato getTail();
		Nodo* search(Dato object);
		void insert(Dato object);
		void remove(Dato object);
		bool contains(Dato object);
		void visualizar();
		Nodo* cola();
	};

bool ListaCircular::isEmpty(){
	if (inicio == NULL){
		return true;
	}else{
		return false;
	}
}

int ListaCircular::getSize(){
		Nodo* ite = inicio;
		int size;
		size = 1;
		while (ite->siguiente() != inicio){
			ite = ite -> siguiente();
			size = size + 1;
		}
		return size;
	}

void ListaCircular::clear(){
		Nodo* ite;;
		if (inicio != NULL){
			ite = inicio;
			do{
				Nodo* temp;
				temp = ite;
				ite = ite ->siguiente();
				delete temp;
			}while (ite != inicio);
		}
		else cout<<"\n\t Lista Vacia."<<endl;
		inicio = NULL;
	}

Dato ListaCircular::getHead(){
		return inicio -> getObject();
	}
	
Dato ListaCircular::getTail(){
		Nodo* tail;
		tail = cola();
		return tail -> getObject();
	}

Nodo* ListaCircular::search(Dato object){
		Nodo* iterador;
		for (iterador = inicio->siguiente(); iterador != inicio; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return iterador;
			return NULL;
	}

void ListaCircular::insert(Dato object){
	Nodo* nuevo;
	nuevo = new Nodo(object);
	if (inicio != NULL){
		nuevo -> enlazar(inicio->siguiente());
		inicio->enlazar(nuevo);
	}
	inicio = nuevo;
}

void ListaCircular::remove(Dato object){
	Nodo* ite;
	bool encontrado = false;
	ite = inicio;
	while((ite -> siguiente() != inicio)&&(!encontrado)){
		encontrado = (ite ->siguiente()->getObject() == object);
		if (!encontrado){
			ite = ite->siguiente();
		}
	}
	encontrado = (ite->siguiente()->getObject() == object);
	if (encontrado){
		Nodo* temp;
		temp = ite->siguiente();
		if (inicio == inicio ->siguiente())
			inicio = NULL;
		else
		{
			if (temp == inicio)
				inicio = ite;
			ite -> enlazar(temp->siguiente());
		}
		delete temp;
	}
}

bool ListaCircular::contains(Dato object){
		Nodo* iterador;
		for (iterador = inicio -> siguiente(); iterador != inicio; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return true;
			return false;
	
	}

void ListaCircular::visualizar(){
		Nodo* ite;
		int i = 0;
		ite = inicio;
		while (ite->siguiente() != inicio){
			char c;
			i++; c = (i%15 != 0 ? ' ':'\n');
			cout << ite -> getObject() << c;
			ite = ite -> siguiente();
		}
	}

Nodo* ListaCircular::cola(){
		Nodo* ite = inicio;
		if (ite == NULL) throw "Lista vacía";
		while (ite->siguiente() != inicio) ite = ite->siguiente();
		return ite;
	}

ListaCircular::ListaCircular(){
		inicio = NULL;
	}
	
	
	
	
	
	
	
