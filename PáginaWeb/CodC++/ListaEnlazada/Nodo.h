typedef int Dato;

#ifndef _NODO_H
#define _NODO_H
class Nodo
{
	protected:
		Dato object;
		Nodo* next;
	public:
		Nodo (Dato t){
			object = t;
			next = 0;
		}
		Nodo (Dato objeto, Nodo* siguiente){
			object = objeto;
			next = siguiente;
		}
		Nodo (){
			object = 0;
			next = 0;
		}
		Dato getObject() const
		{
			return object;
		}
		void enlazar(Nodo* sgte){
			next = sgte;
		}
		Nodo* siguiente() const{
		return next;
		}
};
#endif
