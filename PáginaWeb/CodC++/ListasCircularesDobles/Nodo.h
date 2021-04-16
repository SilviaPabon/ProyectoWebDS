typedef int Dato;

#ifndef _NODO_H
#define _NODO_H

class Nodo
{
	protected: 
	Dato dato;
	Nodo* next;
	Nodo* previous;
	public:
		Nodo(Dato t){
			dato = t;
			next = previous = this;
		}
		
		Dato getObject() const {
		return dato;
		}
		
		Nodo* siguiente() const {
		return next;
		}
		Nodo* anterior() const {
		return previous;
		}
		
		void enlaceSiguiente(Nodo* sgte) {next = sgte;}
		void enlaceAnterior(Nodo* prev){previous = prev;}
		
};
#endif
