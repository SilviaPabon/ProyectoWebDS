typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"
class Lista
{
	protected:
		Nodo* head;
	public:
		Lista();
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
	
	bool Lista::isEmpty(){
		if (head == NULL){
			return true;
		}else{
			return false;
		}
	}
	
	int Lista::getSize(){
		Nodo* ite = head;
		int size;
		size = 1;
		while (ite->siguiente() != NULL){
			ite = ite -> siguiente();
			size = size + 1;
		}
		return size;
	}
	
	void Lista::clear(){
		head = NULL;
	}
	
	Dato Lista::getHead(){
		return head -> getObject();
	}
	
	Dato Lista::getTail(){
		Nodo* tail;
		tail = cola();
		return tail -> getObject();
	}
	
	Nodo* Lista::search(Dato object){
		Nodo* iterador;
		for (iterador = head; iterador != NULL; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return iterador;
			return NULL;
	}
	
	void Lista::add(Dato object){
		insertTail(object);
	}
	
	void Lista::insert(Nodo* nodo, Dato object){
		Nodo* nuevo;
		nuevo = new Nodo(object);
		nuevo -> enlazar(nodo -> siguiente());
		nodo -> enlazar(nuevo);
	}
	
	void Lista::insert(Dato ref, Dato object){
		Nodo* referencia;
		referencia = search(ref);
		insert(referencia,object);
	}
	
	void Lista::insertHead(Dato object){
		Nodo* nuevo;
		nuevo = new Nodo(object);
		nuevo -> enlazar(head);
		head = nuevo;
	}
	
	void Lista::insertTail(Dato object){
		Nodo* cola = this -> cola();
		cola -> enlazar(new Nodo(object));
	}
	
	void Lista::remove(Nodo* nodo){
		Dato object;
		Nodo *iterador,*anterior;
		bool encontrado;
		iterador = head;
		anterior = NULL;
		encontrado = false;
		object = nodo -> getObject();
		while ((iterador != NULL) && !encontrado){
			encontrado = (iterador -> getObject() == object);
			if (!encontrado){
				anterior = iterador;
				iterador = iterador ->siguiente();
			}
		}
		if (iterador == head){
			head = iterador -> siguiente();
		}else{
			anterior -> enlazar(iterador ->siguiente());
		}
		delete iterador;
		}

	void Lista::remove(Dato object){
		Nodo *iterador,*anterior;
		bool encontrado;
		iterador = head;
		anterior = NULL;
		encontrado = false;
		while ((iterador != NULL) && !encontrado)
		{
			encontrado = (iterador -> getObject() == object);
			if (!encontrado)
			{
				anterior = iterador;
				iterador = iterador -> siguiente();
			}
		}
		if (iterador != NULL)
		{
			if (iterador == head)
			{
				head = iterador -> siguiente();
			}else{
				anterior -> enlazar(iterador ->siguiente());
			}
		delete iterador;
		}
	}
	
	bool Lista::contains(Dato object){
		Nodo* iterador;
		for (iterador = head; iterador != NULL; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return true;
			return false;
	
	}
	
	Nodo* Lista::cola(){
		Nodo* ite = head;
		if (ite == NULL) throw "Lista vacía";
		while (ite->siguiente() != NULL) ite = ite->siguiente();
		return ite;
	}

	void Lista::visualizar(){
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
	
	Lista::Lista(){
		head = NULL;
	}
