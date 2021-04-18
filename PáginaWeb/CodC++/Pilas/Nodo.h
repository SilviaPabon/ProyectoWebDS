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
			next = NULL;
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
