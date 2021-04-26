
typedef int Dato;
#ifndef _NODO_H
#define _NODO_H
class Nodo{
	protected:
		Dato object;
		Nodo* izquierda;
		Nodo* derecha;
	public:
		Nodo(Dato object){
			object = object;
			izquierda = derecha = NULL;
		}
		Nodo(Dato object, Nodo* izda, Nodo* dcha){
			object = object;
			izquierda = izda;
			derecha = dcha;
		}
		Dato getObject(){
			return object;
		}
		void setObject(Dato obj){
			object = obj;
		}
		void ramaIzquierda(Nodo* n){
			izquierda = n;
		}
		void ramaDerecha(Nodo* n){
			derecha = n;
		}
		Nodo* subArbolIzda(){
			return izquierda;
		}
		Nodo* subArbolDcha(){
			return derecha;
		}
};

#endif

