
typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"
class Cola
{
	protected:
		Nodo* head;
		Nodo* tail;
	public:
		Cola();
		void clear();
		bool isEmpty();
		Dato extract();
		void insert(Dato object);
		int getSize();
		bool search(Dato object);
		void visualizar();
		/*
		void sort();
		void reverse();
		*/
	};
	
	bool Cola::isEmpty(){
		return head==NULL;
	}
	
	int Cola::getSize(){
		Nodo* ite = head;
		int size;
		size = 1;
		while (ite->siguiente() != NULL){
			ite = ite -> siguiente();
			size = size + 1;
		}
		return size;
	}
	
	void Cola::insert(Dato object){
		Nodo* nuevo;
		nuevo = new Nodo(object);
		if (isEmpty()){
			head = nuevo;
		}
		else{
			tail->enlazar(nuevo);
		}
		tail = nuevo;
	}
	
	Dato Cola::extract(){
		if (isEmpty())
			throw "Cola vacia, sin elementos.";
		Dato aux = head -> getObject();
		Nodo* temp = head;
		head = head->siguiente();
		delete temp;
		return aux;
	}
	
	void Cola::clear(){
	Nodo* ite;
		while(!isEmpty()){
			ite = head;
			head = head->siguiente();
			delete ite;
		}
	}
	
	bool Cola::search(Dato object){
	Nodo* ite;
	ite = head;
	while (ite != NULL){
		if (ite->getObject() == object){
			return true;
		}else{
			return false;
		}
	}
	ite = ite->siguiente();
}
	
	void Cola::visualizar(){
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
	
	Cola::Cola(){
		head = tail = NULL;
	}
