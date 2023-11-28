#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node
 * @head: first node
 * @number: int
 * Return: int
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	
	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}
	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
