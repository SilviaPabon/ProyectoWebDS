typedef int Dato;
#ifndef _NODO_H
#define _NODO_H
class Nodo
{
	private:
		Dato dato;
		Nodo* next;
	public:
		
		Nodo(Dato object)
		{
			dato = object;
			next = this;
		}
		
		Nodo (Dato object, Nodo* siguiente){
			dato = object;
			next = siguiente;
		}
		
		Nodo (){
			dato = 0;
			next = 0;
		}
		
		Dato getObject() const{
		return dato;
		}
		
		void enlazar(Nodo* sgte){
			next = sgte;
		}
		
		Nodo* siguiente() const{
		return next;
		}
};
#endif
