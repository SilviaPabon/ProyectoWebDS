typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"
class ListaCircularDoble
{
	private:
		Nodo* inicio;
	public:
		ListaCircularDoble();
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

bool ListaCircularDoble::isEmpty(){
	if (inicio == NULL){
		return true;
	}else{
		return false;
	}
}

int ListaCircularDoble::getSize(){
		Nodo* ite = inicio;
		int size;
		size = 1;
		while (ite->siguiente() != inicio){
			ite = ite -> siguiente();
			size = size + 1;
		}
		return size;
	}

void ListaCircularDoble::clear(){
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

Dato ListaCircularDoble::getHead(){
		return inicio -> getObject();
	}
	
Dato ListaCircularDoble::getTail(){
		Nodo* tail;
		tail = cola();
		return tail -> getObject();
	}

Nodo* ListaCircularDoble::search(Dato object){
		Nodo* iterador;
		for (iterador = inicio->siguiente(); iterador != inicio; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return iterador;
			return NULL;
	}

void ListaCircularDoble::insert(Dato object){
	Nodo* nuevo;
	nuevo = new Nodo(object);
	if (inicio != NULL){
		nuevo->enlaceSiguiente(inicio->siguiente());
		nuevo->enlaceAnterior(inicio);
		inicio->enlaceSiguiente(nuevo);
	}
	inicio = nuevo;
}

void ListaCircularDoble::remove(Dato object){
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
			ite -> enlaceSiguiente(temp->siguiente());
			
		}
		delete temp;
	}
}

bool ListaCircularDoble::contains(Dato object){
		Nodo* iterador;
		for (iterador = inicio -> siguiente(); iterador != inicio; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return true;
			return false;
	
	}

void ListaCircularDoble::visualizar(){
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

Nodo* ListaCircularDoble::cola(){
		Nodo* ite = inicio;
		if (ite == NULL) throw "Lista vacía";
		while (ite->siguiente() != inicio) ite = ite->siguiente();
		return ite;
	}

ListaCircularDoble::ListaCircularDoble(){
		inicio = NULL;
	}	
