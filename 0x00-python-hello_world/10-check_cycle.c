#include "lists.h"

/**
 * cycle - checks if linked list has a cycle
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
