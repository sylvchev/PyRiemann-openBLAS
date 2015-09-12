#ifndef ABSMAT
#define ABSMAT

class AbsMat
{
	protected:
		//Fields
		unsigned int nbCols;
		unsigned int nbRows;

	public:

		//Virtual destructors for polymorphism
		virtual ~AbsMat() {}
};

#endif 
