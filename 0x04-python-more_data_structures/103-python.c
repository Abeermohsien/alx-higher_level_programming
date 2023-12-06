#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
 
/**
  * print_python_list - prints the lost
  * @p: list
  */
void print_python_list(PyObject *p)
{
	const char *t;
	int s, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < s; i++)
	{
		t = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
/**
 * print_python_bytes - print
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, s;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
		{
			printf("  [ERROR] Invalid Bytes Object\n");
			return;
		}

		printf("  size: %d\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", bytes->ob_sval);

		if (((PyVarObject *)p)->ob_size > 10)
			s = 10;
		else
			s = ((PyVarObject *)p)->ob_size + 1;

		printf("  first %d bytes: ", s);
		for (i = 0; i < s; i++)
		{
			printf("%02hhx", bytes->ob_sval[i]);
			if (i == (s - 1))
				printf("\n");
			else
				printf(" ");
		}
}	
