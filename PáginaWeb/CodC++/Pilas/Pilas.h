
typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"
class Stack
{
	protected:
		Nodo* cima;
	public:
		Stack();
		void clear();
		bool isEmpty();
		Dato peek();
		Dato pop();
		void push(Dato object);
		int size();
		bool searchStack(Dato object);
		void sort();
		void reverse();
		void visualizar();
	};
	
	bool Stack::isEmpty()
	{
		return cima==NULL;
	}
	
	int Stack::size(){
		Nodo* ite = cima;
		int size;
		size = 1;
		while (ite->siguiente() != NULL){
			ite = ite -> siguiente();
			size = size + 1;
		}
		return size;
	}
	
	void Stack::clear(){
		Nodo* ite;
		while(!isEmpty()){
			ite = cima;
			cima = cima->siguiente();
			delete ite;
		}
	}
	
	Dato Stack::peek(){
		if (isEmpty()){
			throw "Pila vacia, sin elementos.";
		}
		return cima->getObject();
	}

	
	void Stack::push(Dato object){
		Nodo* nuevo;
		nuevo = new Nodo(object);
		nuevo -> enlazar(cima);
		cima = nuevo;
	}
	
	Dato Stack::pop(){
		if (isEmpty()){
			throw "Pila vacia, sin elementos.";
		}
		Dato aux = cima->getObject();
		cima = cima->siguiente();
		return aux;
	}

	
	bool Stack::searchStack(Dato object){
		Nodo* iterador;
		for (iterador = cima; iterador != NULL; iterador = iterador->siguiente())
			if (object == iterador ->getObject())
				return true;
			return false;
	
	}
	
	void Stack::visualizar(){
		Nodo* ite;
		int i = 0;
		ite = cima;
		while (ite != NULL){
			char c;
			i++; c = (i%15 != 0 ? ' ':'\n');
			cout << ite -> getObject() << c;
			ite = ite -> siguiente();
		}
	}
	
	Stack::Stack(){
		cima = NULL;
	}

