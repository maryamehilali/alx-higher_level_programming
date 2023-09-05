#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a loop in it
 * @list: head of the singly linked list
 * Return: 0 if no loop, 1 if there is a loop
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *temp = list;

	if (list == NULL)
		return (0);
	while (ptr && temp && temp->next)
	{
		ptr = ptr->next;
		temp = temp->next->next;
		if (ptr == temp)
			return (1);
	}
	return (0);
}
