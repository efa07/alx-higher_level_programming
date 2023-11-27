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

size_t print_listint(const list_t *h);
list_t *add_nodeint(list_t **head, const int n);
void free_listint(list_t *head);
int check_cycle(list_t *list);

#endif 
