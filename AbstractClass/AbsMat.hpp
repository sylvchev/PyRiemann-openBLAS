#ifndef ABSMAT
#define ABSMAT

class AbsMat
{
	protected:

	public:
		//Fields
		unsigned int nbCols;
		unsigned int nbRows;

		//Virtual destructors for polymorphism
		virtual ~AbsMat() {}
};

#endif 
