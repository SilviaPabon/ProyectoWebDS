typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"

class ListaDoble
{
	protected:
	Nodo* head;
	public:
		ListaDoble();
		bool isEmpty();
		int getSize();
		void clear();
		Dato getHead();
		Dato getTail();
		Nodo* search(Dato object);
		void add(Dato object);
		void insert(Nodo* nodo, Dato object);
		void insert(Dato ref, Dato object);
		void insertHead(Dato object);
		void insertTail(Dato object);
		void remove(Dato object);
		void remove(Nodo* nodo);
		bool contains(Dato object);
		void visualizar();
		Nodo* cola();
};

bool ListaDoble::isEmpty(){
		if (head == NULL){
			return true;
		}else{
			return false;
		}
	}

int ListaDoble::getSize(){
		Nodo* ite = head;
		int size;
		size = 1;
		while (ite->siguiente() != NULL){
			ite = ite -> siguiente();
			size = size + 1;
		}
		return size;
	}

void ListaDoble::clear(){
		head = NULL;
		head -> enlaceSiguiente(NULL);
	}

Dato ListaDoble::getHead(){
		return head -> getObject();
	}

Dato ListaDoble::getTail(){
		Nodo* tail;
		tail = cola();
		return tail -> getObject();
	}

Nodo* ListaDoble::search(Dato object){
		Nodo* iterador;
		for (iterador = head; iterador != NULL; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return iterador;
			return NULL;
	}

void ListaDoble::add(Dato object){
		insertHead(object);
	}

void ListaDoble::insert(Nodo* prev ,Dato object){
	Nodo* nuevo;
	nuevo = new Nodo(object);
	nuevo -> enlaceSiguiente(prev -> siguiente());
	if (prev -> siguiente() != NULL)
	 prev -> siguiente() ->enlaceAnterior(nuevo);
	prev -> enlaceSiguiente(nuevo);
	nuevo -> enlaceAnterior(prev);
}

void ListaDoble::insert(Dato obj,Dato object){
	Nodo* ref = search(obj);
	insert (ref,object);
}

void ListaDoble::insertHead(Dato object)
{
	Nodo* nuevo;
	nuevo = new Nodo(object);
	nuevo -> enlaceSiguiente(head);
	if (head != NULL)
	 head -> enlaceAnterior(nuevo);
	 head = nuevo;
}

void ListaDoble::insertTail(Dato object){
	Nodo* nuevo;
	Nodo* tail = this -> cola();
	nuevo = new Nodo(object);
	nuevo -> enlaceAnterior(tail);
	nuevo -> enlaceSiguiente(NULL);
	tail -> enlaceSiguiente(nuevo);
}

void ListaDoble::remove(Nodo* nodo){
	Dato object = nodo -> getObject();
	remove(object);	
}

void ListaDoble::remove(Dato object){
	Nodo* ite;
	bool encontrado = false;
	ite = head;
	while ((ite != NULL) && (!encontrado)){
		encontrado = (ite -> getObject() == object);
		if (!encontrado)
		 ite = ite->siguiente();
	}
	if (ite != NULL){
		if (ite == head){
			head = ite->siguiente();
			if (ite -> anterior() != NULL)
			 ite -> anterior() -> enlaceAnterior(NULL);
		}else  if (ite -> siguiente() != NULL){
			ite -> anterior() -> enlaceSiguiente(ite ->siguiente());
			ite -> siguiente() -> enlaceAnterior (ite -> anterior());
		}
		else
			ite -> anterior() -> enlaceSiguiente(NULL);
	}
}

bool ListaDoble::contains(Dato object){
		Nodo* iterador;
		for (iterador = head; iterador != NULL; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return true;
			return false;
	
	}
	
void ListaDoble::visualizar(){
		Nodo* ite;
		int i = 0;
		ite = head;
		while (ite != NULL){
			char c;
			i++; c = (i%15 != 0 ? ' ':'\n');
			cout << ite -> getObject() << c;
			ite = ite -> siguiente();
		}
	}

Nodo* ListaDoble::cola(){
		Nodo* ite = head;
		if (ite == NULL) throw "Lista vacía";
		while (ite->siguiente() != NULL) ite = ite->siguiente();
		return ite;
	}

ListaDoble::ListaDoble(){
		head = NULL;
	}
