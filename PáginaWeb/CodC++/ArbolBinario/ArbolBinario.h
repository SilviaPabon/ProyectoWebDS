typedef int Dato;
#include <iostream>
using namespace std;
#include "Nodo.h"
class ArbolBinario
{
	protected:
		Nodo* arbol;	
	public:
		ArbolBinario();
		Nodo* raizArbol();
		bool isEmpty();
		void insert(Nodo* subarbol,Dato object);
		void remove(Dato object);
		Nodo* remove(Nodo* subarbol,Dato object);
		Nodo* reemplazar(Nodo* remp);
		Nodo* search(Dato object);
		void preOrder(Nodo* raiz);
		void inOrder(Nodo* raiz);
		void posOrder(Nodo* raiz);
};

	bool ArbolBinario::isEmpty(){
		return arbol == NULL;
	}
	
	Nodo* ArbolBinario::search(Dato object){
		Nodo* ite;
		ite = arbol;
		while(arbol->getObject() != object && ite!=NULL){
			if (object < ite->getObject()){
				ite = ite->subArbolIzda();
			}else{
				ite = ite->subArbolDcha();
			}
			if (ite == NULL){
				return NULL;
			}
		}return ite;
	}
	
	void ArbolBinario::preOrder(Nodo* raiz){
		if (raiz!=NULL){
			cout<< raiz->getObject()<<" - ";
			preOrder(raiz->subArbolIzda());
			preOrder(raiz->subArbolDcha());
		}
	}
	
	void ArbolBinario::inOrder(Nodo* raiz){
		if (raiz!=NULL){
			inOrder(raiz->subArbolIzda());
			cout<< raiz->getObject()<<" - ";
			inOrder(raiz->subArbolDcha());
		}
	}
	
	void ArbolBinario::posOrder(Nodo* raiz){
		if (raiz!=NULL){
			posOrder(raiz->subArbolIzda());
			posOrder(raiz->subArbolDcha());
			cout<< raiz->getObject()<<" - ";
		}
	}
	
	void ArbolBinario::insert(Nodo* arbol,Dato object)
	{
		if (arbol == NULL){
			Nodo* subarbol;
			subarbol = new Nodo(object);
			arbol = subarbol;
		}
		else {
			if (object < arbol->getObject()){
				insert(arbol->subArbolIzda(),object);
			}
			else{
				insert(arbol->subArbolDcha(),object);
			}
		}
	}
	
	void ArbolBinario::remove(Dato obj){
		arbol = remove(arbol,obj);
	}
	
	Nodo* ArbolBinario::remove(Nodo* subarbol,Dato object){
		if (subarbol == NULL)
			throw "El objeto no se encuentra en el arbol";
		else if(object < subarbol->getObject()){
			Nodo* izq;
			izq = remove(subarbol->subArbolIzda(),object);
			subarbol->ramaIzquierda(izq);
		}
		else if (object > subarbol->getObject()){
			Nodo* der;
			der = remove(subarbol->subArbolDcha(),object);
			subarbol->ramaDerecha(der);
		}
		else{
			Nodo* quitar;
			quitar = subarbol;
			if (quitar->subArbolIzda()==NULL)
				subarbol = quitar->subArbolDcha();
			else if (quitar->subArbolDcha() == NULL)
				subarbol = quitar->subArbolIzda();
			else
			{
				quitar = reemplazar(quitar);
			}
		quitar = NULL;
		}
		return subarbol;
	}
	
	Nodo* ArbolBinario::reemplazar(Nodo* remp){
		Nodo *izq,*reemplazo;
		reemplazo = izq;
		izq = remp->subArbolIzda();
		while (izq->subArbolDcha()!=NULL){
			reemplazo = izq;
			izq = izq->subArbolDcha();
		}
		remp->setObject(izq->getObject());
		if (reemplazo==remp)
			reemplazo->ramaIzquierda(izq->subArbolIzda());
		else
			reemplazo->ramaDerecha(izq->subArbolDcha());
			return izq;
	}
	
	Nodo* ArbolBinario::raizArbol(){
		return arbol;
	}
	
	ArbolBinario::ArbolBinario(){
		arbol = NULL;
	}
