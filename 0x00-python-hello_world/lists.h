#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct list_s - linked list
 * @link: the next link
 * Description: linked list node structure
 */
typedef struct list_s
{
	int n;
	struct list_s *link;
} list_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif 
