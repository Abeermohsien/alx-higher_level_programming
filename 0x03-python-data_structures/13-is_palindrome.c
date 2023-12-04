#include "lists.h"

/**
 * is_palindrome - palind or not
 * @head: head
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palind(head, *head));
}

/**
 * check_palind - if is palindrome
 * @head: head
 * @end: end
 * Return: int
 */
int check_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
